from app.application.decision_context import DecisionContext
from app.application.decision_questions import DECISION_QUESTIONS
from app.jev.client import JevClient
from app.jev.mapper import map_decision_result
from app.experiments.data import VARIANTS, CASES, PREVIOUS_ANSWERS
from app.domain.decisions import ChoiceDecision
from collections import defaultdict

print("DEBUG DECISION_QUESTIONS:", DECISION_QUESTIONS)
RUNS = 3

def build_variant_context(case, variant_name):
    if variant_name == "F — previous_answer":
        return {
            "context": {
                "previous_answer": PREVIOUS_ANSWERS[case["name"]],
            }
        }

    return VARIANTS[variant_name]

def evaluate_case(client: JevClient, case: dict) -> ChoiceDecision:
    context = DecisionContext(
        current_message=case["message"],
        context={
            "previous_answer": case["previous_answer"],
        },
    )

    response = client.evaluate(
        context=context,
        questions=DECISION_QUESTIONS,
    )

    decision = map_decision_result(response)

    result = decision.answers["next_action"]

    if not isinstance(result, ChoiceDecision):
        raise ValueError(
            "Expected next_action to be a ChoiceDecision"
        )

    return result

def run_experiment(client: JevClient, run_number: int):
    print()
    print("=" * 60)
    print(f"RUN {run_number}")
    print("=" * 60)

    total = 0
    correct = 0

    category_stats = defaultdict(
        lambda: {
            "total": 0,
            "correct": 0,
        }
    )

    confusion = defaultdict(int)

    metrics = []

    for case in CASES:
        result = evaluate_case(client, case)

        expected = case["expected"]
        got = result.choice
        probabilities = result.probabilities

        ordered = sorted(probabilities.values(), reverse=True)
        top_probability = ordered[0]
        second_probability = ordered[1]
        margin = top_probability - second_probability

        is_correct = got == expected

        total += 1

        if is_correct:
            correct += 1

        category_stats[expected]["total"] += 1

        if is_correct:
            category_stats[expected]["correct"] += 1

        confusion[(expected, got)] += 1

        metrics.append(
            {
                "name": case["name"],
                "expected": expected,
                "got": got,
                "correct": is_correct,
                "top_probability": top_probability,
                "margin": margin,
                "confidence": result.confidence,
            }
        )

        print(
            f"{case['name']} | "
            f"expected={expected} | "
            f"got={got} | "
            f"probs={probabilities} | "
            f"confidence={result.confidence:.2f}"
        )

        print(
            f"{case['name']} | "
            f"top={top_probability:.2f} | "
            f"margin={margin:.2f} | "
            f"confidence={result.confidence:.2f} | "
            f"correct={is_correct}"
        )

        if not is_correct:
            print(
                f"  ❌ {case['name']} | "
                f"expected={expected} | "
                f"got={got} | "
                f"p(expected)="
                f"{probabilities[expected]:.2f}"
            )

    print()
    print("Resumen:")

    accuracy = correct / total if total > 0 else 0.0

    print(
        f"  overall accuracy="
        f"{accuracy:.1%} ({correct}/{total})"
    )

    print()
    print("Por categoría:")

    for category in ("rag", "llm", "clarify"):
        stats = category_stats[category]

        category_accuracy = (
            stats["correct"] / stats["total"]
            if stats["total"] > 0
            else 0.0
        )

        print(
            f"  {category:<10} "
            f"accuracy={category_accuracy:.1%} "
            f"({stats['correct']}/{stats['total']})"
        )

    print()
    print("Matriz de confusión:")

    for expected in ("rag", "llm", "clarify"):
        for predicted in ("rag", "llm", "clarify"):
            count = confusion[(expected, predicted)]

            if count:
                print(
                    f"  expected={expected:<8} "
                    f"got={predicted:<8} "
                    f"count={count}"
                )

    return {
        "accuracy": accuracy,
        "category_stats": dict(category_stats),
        "confusion": dict(confusion),
        "metrics": metrics,
    }

def evaluate_confidence_threshold(
    metrics,
    threshold: float,
):
    correct = 0
    total = len(metrics)

    forced_clarify = 0

    for metric in metrics:
        predicted = metric["got"]

        if metric["confidence"] < threshold:
            predicted = "clarify"
            forced_clarify += 1

        if predicted == metric["expected"]:
            correct += 1

    return {
        "threshold": threshold,
        "accuracy": correct / total,
        "forced_clarify": forced_clarify,
    }

def evaluate_margin_threshold(
    metrics,
    threshold: float,
):
    correct = 0
    total = len(metrics)

    forced_clarify = 0

    for metric in metrics:
        predicted = metric["got"]

        if metric["margin"] < threshold:
            predicted = "clarify"
            forced_clarify += 1

        if predicted == metric["expected"]:
            correct += 1

    return {
        "threshold": threshold,
        "accuracy": correct / total,
        "forced_clarify": forced_clarify,
    }

def evaluate_margin_policy(
    metrics,
    threshold: float,
):
    results = []

    for metric in metrics:
        original_prediction = metric["got"]

        if metric["margin"] < threshold:
            policy_prediction = "clarify"
        else:
            policy_prediction = original_prediction

        results.append(
            {
                **metric,
                "original_prediction": original_prediction,
                "policy_prediction": policy_prediction,
                "policy_changed": (
                    original_prediction != policy_prediction
                ),
                "policy_correct": (
                    policy_prediction == metric["expected"]
                ),
                "false_fallback": (
                    original_prediction == metric["expected"]
                    and policy_prediction != metric["expected"]
                ),
            }
        )

    return results

def summarize_policy(results):
    total = len(results)

    correct = sum(
        r["policy_correct"]
        for r in results
    )

    changed = sum(
        r["policy_changed"]
        for r in results
    )

    false_fallbacks = sum(
        r["false_fallback"]
        for r in results
    )

    errors = total - correct

    return {
        "accuracy": correct / total,
        "fallback_rate": changed / total,
        "errors_remaining": errors,
        "false_fallbacks": false_fallbacks,
    }

if __name__ == "__main__":
    client = JevClient()

    results = []

    for run_number in range(1, 4):
        results.append(
            run_experiment(client, run_number)
        )


    all_metrics = [
        metric
        for result in results
        for metric in result["metrics"]
    ]
    print()
    print("=" * 60)
    print("PROMEDIO DE LAS 3 RUNS")
    print("=" * 60)

    average_accuracy = sum(
        result["accuracy"]
        for result in results
    ) / len(results)

    print(
        f"  overall accuracy={average_accuracy:.1%}"
    )
    
    def average(values):
        return sum(values) / len(values) if values else 0.0


    correct_metrics = [
        metric
        for metric in all_metrics
        if metric["correct"]
    ]

    incorrect_metrics = [
        metric
        for metric in all_metrics
        if not metric["correct"]
    ]

    print()
    print("=" * 60)
    print("CORRECTOS VS INCORRECTOS")
    print("=" * 60)

    for label, data in (
        ("CORRECTOS", correct_metrics),
        ("INCORRECTOS", incorrect_metrics),
    ):
        print()
        print(label)
        print(f"  casos={len(data)}")

        print(
            f"  top_probability="
            f"{average([x['top_probability'] for x in data]):.3f}"
        )

        print(
            f"  margin="
            f"{average([x['margin'] for x in data]):.3f}"
        )

        print(
            f"  confidence="
            f"{average([x['confidence'] for x in data]):.3f}"
        )
    
    print()
    print("=" * 60)
    print("MÉTRICAS POR CATEGORÍA")
    print("=" * 60)

    for category in ("rag", "llm", "clarify"):
        category_metrics = [
            metric
            for metric in all_metrics
            if metric["expected"] == category
        ]

        correct_category = [
            metric
            for metric in category_metrics
            if metric["correct"]
        ]

        incorrect_category = [
            metric
            for metric in category_metrics
            if not metric["correct"]
        ]

        print()
        print(f"[{category}]")

        print(
            f"  total={len(category_metrics)} | "
            f"correct={len(correct_category)} | "
            f"incorrect={len(incorrect_category)}"
        )

        if correct_category:
            print(
                f"  correct margin="
                f"{average([x['margin'] for x in correct_category]):.3f}"
            )

            print(
                f"  correct confidence="
                f"{average([x['confidence'] for x in correct_category]):.3f}"
            )

        if incorrect_category:
            print(
                f"  incorrect margin="
                f"{average([x['margin'] for x in incorrect_category]):.3f}"
            )

            print(
                f"  incorrect confidence="
                f"{average([x['confidence'] for x in incorrect_category]):.3f}"
            )
    
    print()
    print("=" * 60)
    print("CONFIDENCE THRESHOLDS")
    print("=" * 60)

    for threshold in (
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
    ):
        result = evaluate_confidence_threshold(
            all_metrics,
            threshold,
        )

        print(
            f"threshold={result['threshold']:.2f} | "
            f"accuracy={result['accuracy']:.1%} | "
            f"forced_clarify={result['forced_clarify']}"
        )
    
    print()
    print("=" * 60)
    print("MARGIN THRESHOLDS")
    print("=" * 60)

    for threshold in (
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
    ):
        result = evaluate_margin_threshold(
            all_metrics,
            threshold,
        )

        print(
            f"threshold={result['threshold']:.2f} | "
            f"accuracy={result['accuracy']:.1%} | "
            f"forced_clarify={result['forced_clarify']}"
        )

    policy_results = evaluate_margin_policy(
        all_metrics,
        threshold=0.30,
    )

    print()
    print("=" * 60)
    print("MARGIN POLICY = 0.30")
    print("=" * 60)

    for result in policy_results:
        if result["policy_changed"]:
            print(
                f"{result['name']} | "
                f"expected={result['expected']} | "
                f"original={result['original_prediction']} | "
                f"policy={result['policy_prediction']} | "
                f"margin={result['margin']:.2f} | "
                f"correct={result['policy_correct']}"
            )
    
    policy_accuracy = (
    sum(
            result["policy_correct"]
            for result in policy_results
        )
        / len(policy_results)
    )

    changed = sum(
        result["policy_changed"]
        for result in policy_results
    )

    print()
    print(
        f"policy accuracy={policy_accuracy:.1%}"
    )

    print(
        f"policy changed={changed}/{len(policy_results)} "
        f"({changed / len(policy_results):.1%})"
    )

    thresholds = [
        0.10,
        0.20,
        0.25,
        0.30,
        0.35,
        0.40,
        0.50,
        0.60,
    ]

    print()
    print("=" * 80)
    print("MARGIN POLICY ANALYSIS")
    print("=" * 80)

    for threshold in thresholds:
        results = evaluate_margin_policy(
            all_metrics,
            threshold=threshold,
        )

        summary = summarize_policy(results)

        print(
            f"threshold={threshold:.2f} | "
            f"accuracy={summary['accuracy']:.1%} | "
            f"fallback={summary['fallback_rate']:.1%} | "
            f"errors={summary['errors_remaining']} | "
            f"false_fallbacks={summary['false_fallbacks']}"
        )

    for threshold in thresholds:
        results = evaluate_margin_policy(
            all_metrics,
            threshold=threshold,
        )

        errors = [
            r
            for r in results
            if not r["policy_correct"]
        ]

        print()
        print(f"THRESHOLD {threshold:.2f}")
        print("-" * 60)

        for error in errors:
            print(
                f"{error['name']} | "
                f"expected={error['expected']} | "
                f"policy={error['policy_prediction']} | "
                f"margin={error['margin']:.2f}"
            )
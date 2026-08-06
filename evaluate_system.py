from logic_utils import classify_guess
from rag_utils import retrieve_hint
from guardrails import validate_hint


def run_test(name: str, passed: bool) -> None:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")


def main() -> None:
    tests = []

    # classify_guess accuracy
    tests.append(("classify_guess exact match", classify_guess(50, 50) == "correct"))
    tests.append(("classify_guess far low", classify_guess(20, 50) == "far_low"))
    tests.append(("classify_guess slightly high", classify_guess(58, 50) == "slightly_high"))

    # hint retrieval behavior
    hint = retrieve_hint("far_low")
    tests.append(("retrieve_hint returns a non-empty string", bool(hint and isinstance(hint, str))))

    # guardrail validation
    tests.append(("guardrail accepts matching low hint", validate_hint("far_low", "Try a slightly higher guess.")))
    tests.append(("guardrail rejects misleading low hint", not validate_hint("far_low", "Try going lower.")))
    tests.append(("guardrail rejects misleading high hint", not validate_hint("far_high", "Try going higher.")))

    for name, passed in tests:
        run_test(name, passed)

    passed_count = sum(1 for _, passed in tests if passed)
    total_count = len(tests)
    success_rate = (passed_count / total_count * 100) if total_count else 0.0
    print(f"\nOverall success rate: {passed_count}/{total_count} ({success_rate:.1f}%)")


if __name__ == "__main__":
    main()

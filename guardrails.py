def validate_hint(category, hint):
    if "low" in category:
        return not any(
            word in hint.lower()
            for word in ["lower", "decrease", "downward"]
        )

    if "high" in category:
        return not any(
            word in hint.lower()
            for word in ["higher", "increase", "upward"]
        )

    return True
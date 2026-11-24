"""PassGuard Password Analyzer Module."""


def evaluate_strength(password: str) -> dict:
    """
    Evaluates the baseline strength of a password based on simple criteria.
    Returns a dictionary containing score and rating.
    """
    if not password:
        return {
            "score": 0,
            "rating": "Empty",
            "details": ["Password is empty."],
        }

    length = len(password)
    score = min(length * 5, 50)
    rating = "Basic" if score >= 40 else "Weak"

    return {
        "score": score,
        "rating": rating,
        "details": [f"Basic length check: {length} characters."],
    }

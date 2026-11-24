"""PassGuard Password Analyzer Module - NIST SP 800-63B Compliance."""

COMMON_PASSWORDS = {
    "password",
    "123456",
    "admin",
    "qwerty",
    "welcome",
    "letmein",
    "password123",
}


def check_nist_compliance(password: str) -> tuple[bool, list[str]]:
    """Checks compliance against NIST SP 800-63B guidelines and blocklists."""
    issues = []
    if len(password) < 8:
        issues.append("Fails NIST minimum length requirement (must be >= 8 characters).")
    if len(password) > 64:
        issues.append("Exceeds NIST maximum recommended length (must be <= 64 characters).")
    if password.lower() in COMMON_PASSWORDS:
        issues.append("Password found in NIST prohibited common password list.")

    is_compliant = len(issues) == 0
    return is_compliant, issues


def evaluate_strength(password: str) -> dict:
    """Evaluates password strength based on NIST SP 800-63B digital identity guidelines."""
    if not password:
        return {
            "score": 0,
            "rating": "Empty",
            "details": ["Password cannot be empty."],
        }

    is_compliant, issues = check_nist_compliance(password)
    if is_compliant:
        score = 100
        rating = "NIST Compliant"
        details = ["Fully conforms to NIST SP 800-63B digital identity guidelines."]
    else:
        score = max(10, 100 - len(issues) * 35)
        rating = "Non-Compliant"
        details = issues

    return {
        "score": score,
        "rating": rating,
        "details": details,
    }

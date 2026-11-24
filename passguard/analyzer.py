"""PassGuard Password Analyzer Module.

Combines Information-Theoretic Shannon Entropy and NIST SP 800-63B Guidelines.
"""

import math
import string

COMMON_PASSWORDS = {
    "password",
    "123456",
    "admin",
    "qwerty",
    "welcome",
    "letmein",
    "password123",
}


def calculate_entropy(password: str) -> float:
    """Calculates Shannon entropy in bits based on character pool variety."""
    pool_size = 0
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password):
        pool_size += 26

    if pool_size == 0 or len(password) == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)


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
    """
    Evaluates password strength using both Shannon entropy and NIST SP 800-63B rules.
    Synthesizes physical entropy with practical policy validation.
    """
    if not password:
        return {
            "score": 0.0,
            "rating": "Empty",
            "entropy_bits": 0.0,
            "nist_compliant": False,
            "details": ["Password cannot be empty."],
        }

    entropy = calculate_entropy(password)
    is_compliant, nist_issues = check_nist_compliance(password)

    details = [f"Shannon Entropy: {entropy} bits"]
    if is_compliant:
        details.append("NIST SP 800-63B Compliance: Passed (meets length & blacklist criteria)")
    else:
        details.extend(nist_issues)

    # Combined composite rating
    if not is_compliant or entropy < 40:
        rating = "Weak / Non-Compliant"
    elif entropy < 60:
        rating = "Moderate"
    elif entropy < 80:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "score": entropy,
        "rating": rating,
        "entropy_bits": entropy,
        "nist_compliant": is_compliant,
        "details": details,
    }

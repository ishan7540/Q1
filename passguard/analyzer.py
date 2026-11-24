"""PassGuard Password Analyzer Module - Entropy Engine."""

import math
import string


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


def evaluate_strength(password: str) -> dict:
    """Evaluates password strength using Shannon entropy (Information Theory)."""
    if not password:
        return {
            "score": 0.0,
            "rating": "Empty",
            "details": ["Password cannot be empty."],
        }

    entropy = calculate_entropy(password)
    if entropy < 40:
        rating = "Very Weak"
    elif entropy < 60:
        rating = "Moderate"
    elif entropy < 80:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "score": entropy,
        "rating": rating,
        "details": [
            f"Shannon Entropy: {entropy} bits",
            "Evaluated using Information Theory character-space model.",
        ],
    }

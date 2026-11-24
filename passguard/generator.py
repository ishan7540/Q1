"""Password generator module using CSPRNG."""

import secrets
import string

AMBIGUOUS_CHARS = "Il1O0o5S2Z"


def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
) -> str:
    """Generate a cryptographically secure random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    pools = []
    guaranteed = []

    if use_lower:
        chars = string.ascii_lowercase
        if avoid_ambiguous:
            chars = "".join(c for c in chars if c not in AMBIGUOUS_CHARS)
        pools.append(chars)
        guaranteed.append(secrets.choice(chars))

    if use_upper:
        chars = string.ascii_uppercase
        if avoid_ambiguous:
            chars = "".join(c for c in chars if c not in AMBIGUOUS_CHARS)
        pools.append(chars)
        guaranteed.append(secrets.choice(chars))

    if use_digits:
        chars = string.digits
        if avoid_ambiguous:
            chars = "".join(c for c in chars if c not in AMBIGUOUS_CHARS)
        pools.append(chars)
        guaranteed.append(secrets.choice(chars))

    if use_symbols:
        chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        if avoid_ambiguous:
            chars = "".join(c for c in chars if c not in AMBIGUOUS_CHARS)
        pools.append(chars)
        guaranteed.append(secrets.choice(chars))

    if not pools:
        raise ValueError("At least one character set must be selected.")

    all_chars = "".join(pools)
    remaining_length = length - len(guaranteed)
    random_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]

    combined = guaranteed + random_chars
    # Cryptographic shuffle
    for i in range(len(combined) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        combined[i], combined[j] = combined[j], combined[i]

    return "".join(combined)

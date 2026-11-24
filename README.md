# PassGuard - Password Generator & Security Analyzer CLI

PassGuard is a lightweight, dependency-free Python command-line utility for generating cryptographically secure passwords and analyzing password strength.

## Features
- **Cryptographic Generation**: Uses Python's standard `secrets` module for CSPRNG security.
- **Customizable Constraints**: Configurable length, inclusion/exclusion of uppercase, lowercase, numbers, and symbols.
- **Ambiguous Character Filtering**: Eliminates easily confused characters (e.g., `l`, `1`, `I`, `0`, `O`).
- **Shannon Entropy Analysis**: Measures true cryptographic entropy in bits ($E = L \times \log_2(R)$) to assess resistance to brute-force attacks.
- **NIST SP 800-63B Compliance Engine**: Validates passwords against federal identity guidelines and known compromised dictionary blocklists.

## Installation
PassGuard uses Python's standard library with zero third-party dependencies.
Requirements: Python 3.8+

```bash
git clone https://github.com/ishan7540/Q1.git
cd Q1
```

## Basic Usage

### 1. Generate a password
```bash
python3 main.py generate --length 16 --symbols
```

### 2. Comprehensive Security Analysis (Entropy & NIST Audit)
```bash
python3 main.py analyze "MySecureP@ssw0rd123"
```

## Running Tests
```bash
python3 -m unittest discover tests
```

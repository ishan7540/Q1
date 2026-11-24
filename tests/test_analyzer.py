"""Unit tests for combined Shannon entropy & NIST compliance password analyzer."""

import unittest
from passguard.analyzer import (
    evaluate_strength,
    calculate_entropy,
    check_nist_compliance,
)


class TestAnalyzer(unittest.TestCase):
    def test_empty_password(self):
        res = evaluate_strength("")
        self.assertEqual(res["rating"], "Empty")
        self.assertEqual(res["score"], 0.0)
        self.assertFalse(res["nist_compliant"])

    def test_entropy_calculation(self):
        # 8 lowercase letters: pool=26, log2(26) ≈ 4.7004, 8 * 4.7004 ≈ 37.60
        entropy = calculate_entropy("abcdefgh")
        self.assertAlmostEqual(entropy, 37.60, places=1)

    def test_nist_short_password(self):
        is_compliant, issues = check_nist_compliance("short")
        self.assertFalse(is_compliant)
        self.assertTrue(any(">= 8" in msg for msg in issues))

    def test_nist_common_blocklist(self):
        is_compliant, issues = check_nist_compliance("password123")
        self.assertFalse(is_compliant)
        self.assertTrue(any("prohibited" in msg for msg in issues))

    def test_strong_and_compliant_password(self):
        res = evaluate_strength("C0mpl3x!P@ssw0rd99")
        self.assertTrue(res["nist_compliant"])
        self.assertGreaterEqual(res["entropy_bits"], 60.0)
        self.assertIn(res["rating"], ["Strong", "Very Strong"])


if __name__ == "__main__":
    unittest.main()

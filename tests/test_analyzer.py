"""Unit tests for NIST compliance password analyzer."""

import unittest
from passguard.analyzer import evaluate_strength, check_nist_compliance


class TestAnalyzer(unittest.TestCase):
    def test_empty_password(self):
        res = evaluate_strength("")
        self.assertEqual(res["rating"], "Empty")
        self.assertEqual(res["score"], 0)

    def test_nist_short_password(self):
        is_compliant, issues = check_nist_compliance("short")
        self.assertFalse(is_compliant)
        self.assertTrue(any(">= 8" in msg for msg in issues))

    def test_nist_common_blocklist(self):
        is_compliant, issues = check_nist_compliance("password123")
        self.assertFalse(is_compliant)
        self.assertTrue(any("prohibited" in msg for msg in issues))

    def test_nist_valid_password(self):
        res = evaluate_strength("Correct-Horse-Battery-Staple")
        self.assertEqual(res["rating"], "NIST Compliant")
        self.assertEqual(res["score"], 100)


if __name__ == "__main__":
    unittest.main()

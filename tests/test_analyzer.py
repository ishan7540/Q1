"""Unit tests for Shannon entropy password analyzer."""

import unittest
from passguard.analyzer import evaluate_strength, calculate_entropy


class TestAnalyzer(unittest.TestCase):
    def test_empty_password(self):
        res = evaluate_strength("")
        self.assertEqual(res["rating"], "Empty")
        self.assertEqual(res["score"], 0.0)

    def test_entropy_calculation(self):
        # 8 lowercase letters: pool=26, log2(26) ≈ 4.7004, 8 * 4.7004 ≈ 37.60
        entropy = calculate_entropy("abcdefgh")
        self.assertAlmostEqual(entropy, 37.60, places=1)

    def test_strong_password_entropy(self):
        res = evaluate_strength("C0mpl3x!P@ssw0rd99")
        self.assertIn(res["rating"], ["Strong", "Very Strong"])
        self.assertGreaterEqual(res["score"], 60.0)


if __name__ == "__main__":
    unittest.main()

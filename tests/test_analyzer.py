"""Unit tests for baseline password analyzer."""

import unittest
from passguard.analyzer import evaluate_strength


class TestAnalyzer(unittest.TestCase):
    def test_empty_password(self):
        res = evaluate_strength("")
        self.assertEqual(res["rating"], "Empty")
        self.assertEqual(res["score"], 0)

    def test_short_password(self):
        res = evaluate_strength("abc")
        self.assertEqual(res["rating"], "Weak")
        self.assertEqual(res["score"], 15)

    def test_medium_password(self):
        res = evaluate_strength("abcdefghijk")
        self.assertEqual(res["rating"], "Basic")
        self.assertEqual(res["score"], 50)


if __name__ == "__main__":
    unittest.main()

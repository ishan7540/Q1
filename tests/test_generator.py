"""Unit tests for password generator."""

import unittest
from passguard.generator import generate_password, AMBIGUOUS_CHARS


class TestGenerator(unittest.TestCase):
    def test_default_generation(self):
        pwd = generate_password(length=16, use_symbols=False)
        self.assertEqual(len(pwd), 16)

    def test_minimum_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_avoid_ambiguous(self):
        pwd = generate_password(length=32, avoid_ambiguous=True)
        for char in AMBIGUOUS_CHARS:
            self.assertNotIn(char, pwd)

    def test_custom_length(self):
        pwd = generate_password(length=24, use_symbols=True)
        self.assertEqual(len(pwd), 24)


if __name__ == "__main__":
    unittest.main()

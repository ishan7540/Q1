"""Unit tests for JSON exporter module."""

import json
import unittest
from passguard.exporter import export_analysis_json


class TestExporter(unittest.TestCase):
    def test_export_analysis_json(self):
        data = {"score": 85.0, "rating": "Strong", "details": ["High entropy"]}
        out = export_analysis_json(data)
        parsed = json.loads(out)
        self.assertEqual(parsed["rating"], "Strong")
        self.assertEqual(parsed["score"], 85.0)


if __name__ == "__main__":
    unittest.main()

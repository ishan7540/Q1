"""PassGuard JSON Exporter module."""

import json


def export_analysis_json(analysis_data: dict, indent: int = 2) -> str:
    """Formats password strength analysis as a formatted JSON string."""
    return json.dumps(analysis_data, indent=indent)

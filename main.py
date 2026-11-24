#!/usr/bin/env python3
"""Main entry point for PassGuard application."""

import sys
from passguard.cli import main

if __name__ == "__main__":
    main(sys.argv[1:])

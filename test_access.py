#!/usr/bin/env python
"""
Test runner for access module tests.

This script runs pytest for the access module tests.
Replaces the old nose-based testing approach.
"""

import pytest
import sys

if __name__ == "__main__":
    # Run pytest for access module tests
    sys.exit(pytest.main(["fynesse/tests/test_access.py", "-v"]))

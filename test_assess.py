#!/usr/bin/env python
"""
Test runner for assess module tests.

This script runs pytest for the assess module tests.
Replaces the old nose-based testing approach.
"""

import pytest
import sys

if __name__ == "__main__":
    # Run pytest for assess module tests
    sys.exit(pytest.main(["fynesse/tests/test_assess.py", "-v"]))

#!/usr/bin/env python
"""
Test runner for address module tests.

This script runs pytest for the address module tests.
"""

import pytest
import sys

if __name__ == "__main__":
    # Run pytest for address module tests
    sys.exit(pytest.main(["fynesse/tests/test_address.py", "-v"]))


# Libraries to modify the path
import sys
from pathlib import Path

import pytest
from src.greater_than import greater_than

# Insert the main directory of the file to be tested
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_greater_than():
    """Test the greater_than function"""
    assert greater_than(6, 5)

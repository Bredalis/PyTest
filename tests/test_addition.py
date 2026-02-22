
# Libraries to modify the path
import sys
from pathlib import Path

import pytest
from src.addition import addition

# Insert the main directory of the file to be tested
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_addition():
    """Test the addition function."""
    assert addition(2, 5) == 7


@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5, 1, 6),
        (6, addition(4, 2), 12),
        (addition(19, 1), 15, 35),
        (-7, 10, addition(-7, 10)),
    ],
)
def test_addition_parameters(input_x, input_y, expected):
    """Test the addition function with various parameters."""
    assert addition(input_x, input_y) == expected

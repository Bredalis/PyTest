
# Libraries to modify the path
import sys
from pathlib import Path

import pytest
from src.user_login import login

# Insert the main directory of the file to be tested
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def test_successful_login():
    """Test successful login"""
    username = "Bredalis"
    password = "12345"

    assert login(username, password)


def test_failed_login():
    """Test failed login"""
    username = "Lisa"
    password = "1234567"

    assert not login(username, password)

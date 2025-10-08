"""Tests for main module."""

import pytest
from src.cc_stmt_data_scrubber.utils import greet, add_numbers, multiply_numbers


def test_greet():
    """Test the greet function."""
    result = greet("Alice")
    assert result == "Hello, Alice!"
    assert isinstance(result, str)


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(0, 5) == 0


def test_add_numbers_type():
    """Test that add_numbers works with different numeric types."""
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers(10, 20) == 30

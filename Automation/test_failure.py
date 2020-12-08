import pytest
import math

def test_sqrt_failure():
    num=25
    assert math.sqrt(num) ==6

def test_square_failure():
    assert 7*7 == 40

def test_equality_failure():
    assert 10==11
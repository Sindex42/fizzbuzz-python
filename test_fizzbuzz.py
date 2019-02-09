import pytest
from fizzbuzz import *

def test_fizzbuzz_returns_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_returns_buzz():
    assert fizzbuzz(5) =='buzz'

def test_fizzbuzz_returns_x():
    assert fizzbuzz(1) == 1

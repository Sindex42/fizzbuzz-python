import pytest
from fizzbuzz import *

def test_fizzbuzz_returns_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_returns_buzz():
    assert fizzbuzz(5) =='buzz'

def test_fizzbuzz_returns_x():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_returns_fizz_when_multiple_of_3():
    assert fizzbuzz(6) == 'fizz'

def test_fizzbuzz_returns_buzz_when_multiple_of_5():
    assert fizzbuzz(10) == 'buzz'

def test_fizzbuzz_returns_fizzbuzz_when_multiple_of_3_and_5():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_fizzbuzz_returns_fizzbuzz_when_multiple_of_3_and_5():
    assert fizzbuzz(30) == 'fizzbuzz'

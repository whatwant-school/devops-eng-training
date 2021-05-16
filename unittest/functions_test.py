# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성
import pytest
import os.path
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)
import functions


def test_add():
    prediction = functions.add_function(6, 2)
    assert prediction == 8


def test_subtract():
    predict = functions.subtract_function(6, 2)
    assert predict == 4


def test_multiply():
    prediction = functions.multiply_function(6, 2)
    assert prediction == 12


def test_division():
    prediction = functions.division_function(6, 2)
    assert prediction == 3

def test_sqrt():
    prediction = functions.sqrt_function(4)
    assert prediction == 2

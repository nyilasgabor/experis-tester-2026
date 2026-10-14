import pytest
import csv
from Math import * 

def load_csv(path):
    with open(path) as f:
        return [tuple(row.values()) for row in csv.DictReader(f)]

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (10, 100, 100),
    (-1, -2, -3)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", load_csv("C:\\Users\\nyila\\repos\\experis-tester-2026\\UnitTesting\\test_data.csv"))
def test_subtract(a, b, expected):
    assert subtract(int(a), int(b)) == int(expected)

def test_multiply():
    assert multiply(2, 3) == 10

def test_divide():
    with pytest.raises(ValueError):
        divide(10, 1)



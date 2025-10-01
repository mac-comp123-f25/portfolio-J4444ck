from my_sum import *

def test_sum3_ints():
    assert sum3([1, 2, 3]) == 6
    assert sum3([14, 25, 10]) == 49

def test_sum3_floats():
    assert sum3([1.1, 2.2, 3.3]) == 6.6

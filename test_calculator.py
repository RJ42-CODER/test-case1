import pytest

from calculator import add, sub,mul,div

def test_add():
    assert add(4,5) == 9
    assert add(1,2) == 3
    assert add(0,0) == 0

def test_sub():
    assert sub(5,4) ==1
    assert sub(2,1) == 1
    assert sub(10,1) == 9

def test_mul():
    assert mul(2,3)==6
    assert mul(4,5)==20
    assert mul(0,5)==0

def test_div():
    assert div(10,2)==5
    assert div(20,4)==5
    

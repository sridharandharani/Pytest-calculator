import calculator
import pytest

@pytest.mark.parametrize("x,y,z",[(5,2,7),(6,3,9),(2,3,3)])
def test_add(x,y,z):
    res = calculator.add(x,y)
    assert res == z

@pytest.mark.parametrize("x,y,z",[(5,2,3),(6,3,3),(2,3,0)])
def test_sub(x,y,z):
    res = calculator.sub(x, y)
    assert res == z

@pytest.mark.parametrize("x,y,z",[(5,2,10),(6,3,18),(2,3,4)])
def test_mul(x,y,z):
    res = calculator.mul(x, y)
    assert res == z

@pytest.mark.parametrize("x,y,z",[(6,2,3),(6,3,2),(10,5,1)])
def test_div(x,y,z):
    res = calculator.div(x, y)
    assert res == z



import calculator

def test_add():
    x = 10
    y = 20
    res = calculator.add(x,y)
    assert res == x+y

def test_sub():
    x = 10
    y = 20
    res = calculator.sub(x, y)
    assert res == x - y

def test_mul():
    x = 10
    y = 20
    res = calculator.mul(x, y)
    assert res == x * y

def test_div():
    x = 10
    y = 20
    res = calculator.div(x, y)
    assert res == x / y



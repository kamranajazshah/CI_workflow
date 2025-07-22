from src.math_operations import add,sub
def test_add():
    assert add(2,2) ==4
    assert add(7,4)==11

def test_sub():
    assert sub(5,2)==3
    assert sub(10,4)==6
from calculator import calc
def test_calculator_add():
    assert calc(1,3,"add")==4
test_calculator_add() 

def test_calculator_sub():
    assert calc(1,3,"sub")==-2
test_calculator_add() 

def test_calculator_mul():
    assert calc(1,3,"mul")==3
test_calculator_add() 

def test_calculator_add():
    assert calc(1,3,"div")==4
test_calculator_add() 

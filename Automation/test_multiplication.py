#pytest test_multiplication.py -v --junitxml="result.xml"


import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44),(5,55)])
def test_multiplication_11(num, output):
   assert 11*num == output
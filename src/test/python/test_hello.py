# https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test

from src.main.python import hello1

def test_my_function():
    assert hello1.myFunction("5") == "param-5"

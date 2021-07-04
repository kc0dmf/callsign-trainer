# https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test

from src.main.python import hello1 as hello

def test_my_function():
    assert hello.myFunction("5") == "param-5"

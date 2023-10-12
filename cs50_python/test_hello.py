from hello2 import hello

def test_defult():
    assert hello()=="hello,world"

def test_arguments():
    assert hello("David") == "hello,David"
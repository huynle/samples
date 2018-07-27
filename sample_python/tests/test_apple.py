from other import Apple


def test_apple1():
    apple = Apple("red")
    apple.set_expire("test")
    print(apple.color())
    assert True

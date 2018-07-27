from other import Apple, YouApple


if __name__ == '__main__':
    apple = Apple("red")
    apple.set_expire("test")
    print(apple.color())

    my_apple = YouApple("Another")
    my_apple.set_expire("test")
    print(my_apple.color())

def outer_func():
    def inner_func():
        print('Inner')

    print('Out')
    inner_func()


outer_func()

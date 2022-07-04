def outer_func():
    a = 8

    def inner_func():
        nonlocal a
        print(a)
        a = 10

    print(a)
    inner_func()
    print(a)


a = 0
print(a)
outer_func()
print(a)

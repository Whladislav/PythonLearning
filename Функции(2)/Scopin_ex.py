a = 'Global'


def func():
    global a
    a = 'local'
    print(a)


func()
print(a)

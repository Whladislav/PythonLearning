def func():
    """
    строка, стоящая в самом начале функции -- это документционная строка
    """
    print('function called')


func()
print(func.__doc__)

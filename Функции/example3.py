def func(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    for i in range(-3, 4):
        y = func(i)
        print('func(', i, ')=', y, sep='')


main()

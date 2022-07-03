x = float(input('Enter num: '))
if 0 < x < 7:
    print('Значение x входит в заданный диапазон')
    y = 2 * x - 5
    if y < 0:
        print('Значение y отрицательно')
    else:
        if y > 0:
            print('Значение y положительно')
        else:
            print('y=0')

# Оператор N въехал в город N

if 0 < x < 7:
    print('Значение x входит в заданный диапазон')
    y = 2 * x - 5
    if y < 0:
        print('Значение y отрицательно')
    elif y > 0:
        print('Значение y положительно')
    else:
        print('y=0')

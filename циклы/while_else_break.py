attemps = 3
while attemps:
    attemps -= 1
    password = input()
    if password == '42':
        print('access')
        break
else:
    print('расходимся')

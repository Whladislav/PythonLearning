a = float(input('First Number: '))
b = float(input('First Number: '))
opr = input('Operation: ')

res = None

if opr == '+':
    res = a+b
elif opr == '-':
    res = a-b
elif opr == '*':
    res = a*b
elif opr == '/':
    res = a/b
else:
    print('Unsupported operation')

if res != None:
    print('Result: ', res)
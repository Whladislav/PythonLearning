p1 = 'я строка '
print(p1)
print(type(p1))

print()

p1 = 44
print(p1)
print(type(p1))

print()

a=5
b=5
print(a+b)

b='5'
try:
    print(a+b)
except TypeError:
    print('b не число, расходимся')

for i in range(10):
    print(i)

print()

for i in range(3, 10):
    print(i)

print()

for i in range(10, 0, -1):
    print(i)

print()

for i in range(10):
    print(i)
    if i == 6:
        continue
    elif i == 8:
        break

print()

for i in range(3, 1, -1):
    password = input()
    if password == '42':
        print('access')
        break
else:
    print('расходимся')

print()

for i in range(10):
    if i == 4:
        i += 1
    print(i)

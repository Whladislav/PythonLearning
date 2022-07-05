list = []

list.append(3)
list.append(5)
list.append(list[0] + list[1])

print(list)

del list[1]

print(list)

list[0] = 999

print(list)

list2 = [1, 3, 4, 69, 6, 4, 0]

for x in list2:
    print(x, x ** 2)

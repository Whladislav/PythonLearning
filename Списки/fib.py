n = 10

fibs = [1, 1]

for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])

    print(fibs)

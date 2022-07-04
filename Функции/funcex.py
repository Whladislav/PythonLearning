import Example1


def print_numbers(lim):
    for i in range(lim):
        print(i)


def main():
    Example1.hello_world()
    print_numbers(5)
    print()
    print_numbers(8)


n = int(input('n= '))
print_numbers(n)

print()
if __name__ == '__main__':
    main()

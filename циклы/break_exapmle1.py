name = None
while True:
    print("""Menu:
    1. Enter name
    2. Print Greetings
    3. Quit
    """)

    rsp = input('choose: ')
    print()

    if rsp == '1':
        name = input()
    elif rsp == '2':
        if name:
            print('Здравствуйте, ', name)
        else:
            print('Здравствуйте')
    elif rsp == '3':
        break

print(50 * '-')

while True:
    number = input("Type a number to discover if it's even or odd: ")

    while not number.isnumeric():
        if '-' in number:
            break
        elif '+' in number:
            break
        number = input(f"Error. '{number}' isn't a number, try again: ")

    number = int(number)

    if (number % 2) == 0:
        print(f"'{number}' is an even number.")
        print(50 * '-')
    elif (number % 2) == 1:
        print(f"'{number}' is an odd number.")
        print(50 * '-')

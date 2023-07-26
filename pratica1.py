# Integer numbers

number = input("Type a integer number: ")

while not number.isnumeric():
    if '-' or '+' in number:
        break
    number = input(f"'{number}' isn't a number. Try again: ")

number = int(number)

if number < 0:
    print(f"{number} is a negative integer number.")
elif number == 0:
    print(f"{number} is neither positive nor negative.")
else:
    print(f"{number} is a positive integer number.")

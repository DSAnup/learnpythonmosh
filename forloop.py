for number in range(3):
    print("Attempt", number, number + 1, (number + 1) * ".")

for number in range(1, 4):
    print(number)

for number in range(1, 10, 2):
    print(number)

successful = False

for number in range(3):
    print("hello")
    if successful:
        print("success")
        break
else:
    print("Attempted 3 times and failed")

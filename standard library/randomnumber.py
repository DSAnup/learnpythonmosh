from random import random, randint, choice, choices, shuffle
import string

print(random())
print(randint(1, 10))
print(choice([1, 3, 44, 5, 99]))
# multiple choice
print(choices([1, 3, 44, 5, 99], k=2))
# random password  generator
print("".join(choices(string.ascii_letters + string.digits, k=8)))

number = [1, 2, 3, 4]

shuffle(number)
print(number)

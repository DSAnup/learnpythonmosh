numbers = [1, 1, 3, 3, 2, 4]
uniques = set(numbers)
# unique number
print(uniques)

first = set(numbers)
second = {3, 5, 8}
# both unique number
print(first | second)
# only unique number from both
print(first & second)
# show from first accept matching number
print(first - second)
# show from both accept matching number
print(first ^ second)

# set is not support index

if 1 in first:
    print("yes")

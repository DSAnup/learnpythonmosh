letters = ["a", "b", "c"]
# with validation
if "d" in letters:
    print(letters.index("d"))

print(letters.count("b"))

numbers = [1, 4, 5, 22, 3, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 18),
]


def sort_item(item):
    return item[1]


print(sorted(items, key=sort_item))

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 18),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


# with lambda
items.sort(key=lambda item: item[1])
print(items)

items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 18),
]

mapPrice = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered2 = [item for item in items if item[1] >= 10]
print(filtered2)

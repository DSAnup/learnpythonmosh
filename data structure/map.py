items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 18),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

mapPrice = list(map(lambda item: item[1], items))
print(mapPrice)
for i in mapPrice:
    print(i)

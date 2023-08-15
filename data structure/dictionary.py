point = {"x": 1, "y": 2}
point = dict(x=1, y=3)
point["x"] = 10
point["z"] = 20

print(point.get("a", 0))  # by default 0
print(point)
del point["x"]
print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)


# comprehensions

values = [x * 2 for x in range(5)]
print(values)
values = {x: x * 2 for x in range(5)}
print(values)

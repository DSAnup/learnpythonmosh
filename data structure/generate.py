from sys import getsizeof

values = (x * 2 for x in range(10000))
print("gen tuple:", getsizeof(values))
values = [x * 2 for x in range(10000)]
print("gen list:", getsizeof(values))

# for x in values:
#     print(x)

# take the value
first = [1, 2, 4]
second = [3]
com = [*first, "a", *second, *"hello"]
print(com)

# Taken last value if same
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)

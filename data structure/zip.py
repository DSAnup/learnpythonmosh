list1 = [1, 23, 43]
list2 = [10, 20, 30]

# want to create [(1,10), (23, 20), (43, 30)]

print(list(zip("abc", list1, list2)))

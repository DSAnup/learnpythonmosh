letters = ["a", "b", "c"]
matrix = [[0, 2], [3, 4]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
# print(chars)
print(len(chars))
print(chars[0])
letters[0] = "A"
# print(letters)
print(numbers[::2])
# reverse
print(numbers[::-3])
print(chars[::-1])

# unpacking
numbers = [1, 2, 3, 4, 4, 45]
first, second, *other = numbers
print(second)
print(other)

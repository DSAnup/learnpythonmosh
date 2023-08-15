letters = ["a", "b", "c"]
letters2 = ["a", "b", "c"]

for letter in enumerate(letters):
    print(letter[0], letter[1])

for index, letter in enumerate(letters):
    print(index, letter)

# Add
letters.append("d")
print(letters)
# specific poision
letters.insert(1, "_")
print(letters)

# Remove
letters.pop()
letters.pop(0)
letters.remove("b")
print(letters)

del letters2[0:3]
letters2.clear()
print(letters2)

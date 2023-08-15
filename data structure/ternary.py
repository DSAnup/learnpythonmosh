age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

message = "El" if age >= 18 else "Not el"
print(message)

# chaining comparison age should be between 18 and 65

if 18 <= age < 65:
    print("ok")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

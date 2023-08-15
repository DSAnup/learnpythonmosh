try:
    age = int(input("Age :"))
    xfactor = 10 / age
except ValueError as ex:
    print("Please enter numeric value")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age cannot be divided by 0")
else:
    print("No exceptions were thrown.")
print("Excution continues")

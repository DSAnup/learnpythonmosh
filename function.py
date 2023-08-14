def greet(first_name, last_name):
    print("Hi there")
    print(f"My name is {first_name} {last_name}")


greet("Anup", "Mondal")


def get_greeting(name):
    return f"Hi, {name}"


message = get_greeting("Anup")
print(message)

# use of xargs/ *


def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))

# key value dictionary uses ** convert dictionary


def save_user(**users):
    print(users["name"])


save_user(id=1, name="john", age=22)

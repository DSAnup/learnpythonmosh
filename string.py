course = "  Python programming"

# string slice

print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])

# Formated string concate

First = "Anup"
Last = "Mondal"
Full = First + " " + Last
FFull = f"{First} {Last}"
print(Full)

# uppercase
print(FFull.upper())
# LowerCase
print(FFull.lower())
# Capitilized first letter
print(course.title())
# strip the remove whitespace
print(course.strip())
# get the index of a character
print(course.find("pro"))
# replace character
print(course.replace("p", "n"))
# existing in character
print("pro" in course)
print("prod" not in course)

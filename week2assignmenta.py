#In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

camelcase=input("Enter a name in camelcase:")
snake_case=""
for char in camelcase:
    if char.isupper():
        snake_case=snake_case + "_"+char.lower()
    else:
        snake_case=snake_case + char

print("snake_casez:",snake_case)

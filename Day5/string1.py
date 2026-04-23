# 6. String Formatting with f-strings
# Task: Take user input for name and age.
# Use an f-string to print:
# "My name is <name>, and I am <age> years old."
from dataclasses import replace

Name=input("Enter your name:")
age=input("Enter your age:")

print(f"My name is {Name},and I am {age} years old")


city=input("My Hometown is:")
place=input("I Live in:")
print(f"My Hometown is {city}, and I Live in {place}")


# 7. Case Conversion Methods
# Task: Write a program that takes "welcome to python" and prints:
# • Capitalized string
# • Title case string
# • Uppercase string
# • Swapcase string

y=("welcome to python")
print("capitalize():" , y.capitalize() )
print("title():" , y.title())
print("upper():" , y.upper())
print("swapcase():" , y.swapcase())


# 8. Counting and Replacing
# Task: Given string "banana", count how many times "a" appears.
# Then replace "banana" with "orange" in the string "I like banana".

s="banana"
print("count of 'a':" , s.count("a"))

e="I Like Banana"
new_e = e.replace("banana" , "Orange")
print(new_e)



y1="mangomilkshake"
print("count of 'm':" , y1.count("m"))

r1="I like strawberry"
new_r1 = r1.replace("strawberry" , "Pineapple")
print(new_r1)

# 9. Validation Check
# Task: Ask the user to input a string. Check if:
# • It contains only alphabets (isalpha())
# • It contains only digits (isdigit())
# • It is alphanumeric (isalnum())
# Print results accordingly.

j=input("Enter any word:")
print("It contains only alphabets:" , j.isalpha())
print("It contains only digits:" , j.isdigit())
print("It contains only alphanumeric:" , j.isalnum())


# 10. Split and Strip
# Task:
# • Given string " apple,banana,grape ", strip spaces.
# • Split the string by commas ,.
# • Print the list of fruits.

s = "  apple,banana,grape  "

# Strip spaces
s = s.strip()

# Split by comma
fruits = s.split(",")

print("Fruits:", fruits)



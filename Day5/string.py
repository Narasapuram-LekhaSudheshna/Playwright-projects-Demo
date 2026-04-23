# 1. Create Strings in Different Ways
# Task: Write a program to create strings using single quotes, double quotes, and str()
# constructor. Print them and check their type using type().
from operator import index

name='Lekha'
grade='A'
print(name)
print(grade)
print(type(name))

name="Apple"
fruit='banana'
print(fruit)
print(name)
print(type(fruit))

name=str()
fruit=str('mango')
print(fruit)
print(type(name))



# 2. Immutable Strings Demo
# Task: Create a string "hello", print its memory address using id().
# Now modify it (e.g., s = s + " world") and print again. Show that the address changes.

s1="Hello"
print("original string:" ,s1)
print("memory address:" ,id(s1))      #output-2461805388704
s2= s1 + ' World'
print("original string:" ,s2)
print("memory address:" ,id(s2))      # output-2005873982384


# 3. Concatenation and Repetition
# Task: Take two strings "Python" and "Rocks".
# • Concatenate them using +.
# • Repeat the string "Python" 3 times using *.


n1="Python"
n2="Rocks"
print(n1 + " " + n2)
print(n1 * 3 )

# 4. String Slicing Practice
# Task: Take a string "welcome". Print:
# • Characters from index 1 to 4
# • First 5 characters
# • Last 3 characters using negative indexing
# • Middle substring "lco" using slicing


e="Welcome"
print("print characters from index 1 to 4:" , e[1:5])
print("First 5 characters:" ,e[:5])
print("Last 3 Caharacters:" , e[-3:])
print("Middle substring using slicing:" , e[2:5])
print("last 4 characters:" , e[-5:])


# 5. Check Substring using in and not in
# Task: Write a program that asks the user to input a word.
# Check if "python" is present in that word. Print "Found" or "Not Found".

r=input("Enter a word:")

if "Python" in r:
  print("Found")
else:
    print("Not found")


word=input("Enter a word:")

if "Hyderabad" in word:
    print("Place Found")
else:
    print("Not found")













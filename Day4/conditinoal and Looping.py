#Positive, Negative, or Zero: Get a number from the user and print whether it's
# positive, negative, or zero.

 #a=10

#a=int(input(" Enter the number:"))

#if (a>0): print("Number is positive")
#elif(a<0): print("Number is negative")
#else : print("Number is Zero")


#Vowel or Consonant: Take a single letter as input and check if it's a vowel (a, e, i, o, u)
# or a consonant.

a=str(input("Enter the letter:"))
if a in "aeiou": print("letter is vowel")
else: print("Letter is consonanat")


# Grading System: Get a student's score (0-100) and assign a letter grade (A, B, C, D, or
# F) based on a simple scale.


a= int(input("Enter the number:"))

if a==100: print("Grade is A")

elif a>85: print(" Garde is B")

elif a>60: print("Grade is C")

elif a>34: print(" Grade id D")

else: print(" Grade is F")


# Even or odd numbers

a=int(input("enter a Number:"))
if a%2==0: print("Number is Even")
else: print("Number is odd")

#Voting Eligibility

a= int(input("Enter a Number:"))
if a>=18: print("person is Eligible for Voting")
else: print("Person is not eligible for Voting")

#Largest of 3numbers


a=45
b=30
c=12

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

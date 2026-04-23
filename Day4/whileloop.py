# . Sum of Digits: Get a number and calculate the sum of its digits using a while loop.
# For example, for the number 123, the sum is 1+2+3=6


a=123
total = 0
while a>0:
 digit= a%10
 total= total+digit
 a=a//10

#print(total)


# Reverse a Number: Take a number and print its reverse. For example, reversing 1234
# gives 4321.

a=123456
reverse=0
while a>0:
    digit=a%10
    reverse= reverse*10 + digit
    a=a//10
print(reverse)

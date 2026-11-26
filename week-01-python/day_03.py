#conditional operators
a = int(input('enter the number:'))

if a % 2 == 0:
    print('the given number is even')
else:
    print('the given number is odd')


# 2 checking the given number is positive or negative or zero

num = int(input('enter the number:'))

if num > 0:
    print('the given number is postive')
elif num < 0:
    print('the given number is negative')
else:
    print('the given number is zero')

# finding the largest number

a = int(input('enter the number:'))
b = int(input('enter the number:'))

if a > b:
    print('A is greater than B')
elif b > a:
    print('B is greater than A')
else:
    print('Both Are equal')

# Relational Operators
#Python Program Using All Relational Operators
a = 10
b = 5

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


# checking whether the two strings are equal or not 
str1 = input('enter the string')
str2 = input('enter the string')

if str1 == str2:
    print('both strings are equal:')
else:
    print('both strings are not equal:')

#checking the given number is btw 10 & 50 
num = int(input('enter the number:'))

if num >= 10 and num <= 50:
    print('the number is btw 10 & 50')
else:
    print('the number doesnot lie btw 10 & 50')

#Check whether a person can enter
age = int(input('enter the age:'))
has_ticket = True

if age >= 18 or has_ticket:
    print('entry is allowed')
else:
    print('entry is not allowed')
# strings problems
#Write a Python program to reverse a string.
a = 'teja'
s = a[::-1]
print(s)

#Find the length of a string without using len()
a = 'teja'
count = 0
for i in a:
    count +=1
print(count)

#Check whether a string is a palindrome
s = input('enter the string: ')
rev = ''

for ch in s:
    rev = ch + s
if s == rev:
    print('palindrome')
else:
    print('not a palindrome')

#
s = "programming"
vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
         if ch.lower() in 'aeiou':
            vowels +=1
         else:
            consonants +=1
print(f'the vowels in the given word is {vowels}')
print(f'the consonants in the given word is {consonants}')



## list problems
# check whether the given number is even or odd
num = int(input('enter the number: '))

if num % 2 == 0:
    print('even')
else:
    print('odd')

#Find the largest of three numbers
a = 10
b = 25
c = 20

if a >b or a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

#Write a Python program to find the factorial of a given number.
num = int(input('enter the number: '))
fact = 1

for i in range(1,num+1):
    fact = fact *i
print(f'the factorial of given is {fact}')

## tuple
# finding the max and min number
t = (45, 12, 89, 23, 5)

print(f'the maximum number in the given number is: {max(t)}')
print(f'the minimum number in the given number is: {min(t)}')

#Check whether an element exists
t = (10, 20, 30, 40, 50)

num = 30

if num in t:
    print("Element found")
else:
    print("Element not found")








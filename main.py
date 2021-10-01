# Use_ful string methods

# course = '  Python Programing  '
# print(course.upper())
# print(course.lower())
# print(course.title())
#
# print(course.strip())
# print(course.lstrip())
# print(course.rstrip())
#
# print(course.find("Python"))
# print(course.replace("P", '-'))
#
# print('Programing' in course)
# print('Programing' not in course)


# Numbers
# x = 10

# binary
# b = 0b10
# print(b)
# print(bin(x))

# hexadecimal
# c = 0x12c
# print(c)
# print(hex(x))

# complex_number a + bj
# d = 1 + 2j
# print(d)


# Arithmetic
# x = 10 + 3
# x = 10 - 3
# x = 10 * 3
# / get float number
# x = 10 / 3
# // get division in format of int
# x = 10 // 3
# remainder of division
# x = 10 % 3
# power
# x = 10 ** 3

# x = x + 1
# x += 1
# we dont have x++ or x--
# print(x)

# use_ful function to work with numbers
# we dont have constant variables in py and write uppercase to understand that this variable should not change
# for all functions https://docs.python.org/3/library/functions.html
# for all math modules https://docs.python.org/3/library/math.html
# PI = -3.14
# print(round(PI))
# print(abs(PI))
#
# import math
#
# print(math.floor(PI))


# Convert type
# x = input('x: ')
#
# print(int(x))
# print(float(x))
# print(bool(x))
# str()

# Falsy value
# ""
# 0
# []
# None (null)

# Conditional statement

# age = 10
# == != >= ...
# if age >= 18:
#     print('Adult')
#     # pass ==> for empty if
# elif age >= 13:
#     print('Teenager')
# else:
#     print('Child')

# Logical operators
# and or not

# name = " "
# if not name.strip():
#     print('name in Empty')
#
# age = 22
# if 18 <= age < 50:
#     print('ok')
# instead of and operator

# Ternary operator (liner conditional)
# age = 22
# message = 'eligible' if age > 18 else 'not eligible'
# print(message)

# Loops

for x in 'Python':
    print(x)

for x in ['a', 'b', 'c']:
    print('x')

for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
#             start, end, step
for x in range(1, 10, 2):
    print(x)
# range is not a list try type() function

# for - else
names = ["John", "Mosh"]
for name in names:
    if name.startswith('J'):
        print('Found')
        break
else:
    print('not Found')

# instead of
found = False
for name in names:
    if name.startswith('J'):
        print('Found')
        found = True
        break
if not found:
    print('not Found')

# while

guess = 0
current = 3

while guess != 3:
    guess = int(input('guess: '))
else:
    pass

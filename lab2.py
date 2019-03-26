import math

#0 Use alternative way of reading inputs - using library (0.5p)
from cs50 import get_int
from cs50 import get_float

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
print("-+"*40, "task 1")

def perimeter(r):
    return 2*math.pi*r

def field(r):
    return math.pi*r**2

x = get_float("Radius X for the first circle: ")
while x < 0:
    print("X must be grater than or equal to 0")
    x = get_float("X: ")

y = get_float("Radius Y for the second circle: ")
while y < 0:
    print("X must be grater than or equal to 0")
    y = get_float("Y: ")

print("1st circle:")
print("Perimeter: ", perimeter(x))
print("Field: ", field(x))
print("2nd circle:")
print("Perimeter: ", perimeter(y))
print("Field: ", field(y))


#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
print("-+"*40, "task 2")

x = get_int("X: ")
while x < 0:
    print("X must be grater than or equal to 0")
    x = get_int("X: ")

y = get_int("Y: ")
while y <= 0:
    print("Y must be greater than 0")
    y = get_int("Y: ")

true = 1
noteven = 0
while true:
    while (x % y) != 0:
        print(x, " is not divisible by ", y)
        x = get_int("X: ")
        y = get_int("Y: ")
        while y <= 0:
            print("Y must be greater than 0")
            y = get_int("Y: ")
    if x % 2 != 0:
        print(x, " is not even")
        noteven = 1
    if y % 2 != 0:
        print(y, " is not even")
        noteven = 1
    if noteven == 0:
        true = 0
    if noteven == 1:
        x = get_int("X: ")
        y = get_int("Y: ")
        while y <= 0:
            print("Y must be greater than 0")
            y = get_int("Y: ")
        noteven = 0

print(x, "is divisible by", y, "\nX & Y are even")

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
print("-+"*40, "task 3")
x = get_int("X: ")
y = get_int("Y: ")
while y <= 0:
    print("Y must be greater than 0")
    y = get_int("Y: ")

isXdivisiblebyY = "X is divisible by Y" if x % y == 0 else "X is not divisible by Y"
print(isXdivisiblebyY)

#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number
# of decimals". (1p)
print("-+"*40, "zadanie 4")
print(x, "/", y, "=")
print("%.6f" % (x/y))

#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with
# different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)

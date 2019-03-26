from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

#1: calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
for x in range(56, 101):
    y=2*(x**2)+2*x+2
    print(y)

#def function(x):
#    return 2*x**2+2*x+2

#for i in range(56, 101):
#    print(function(i))

#2: ask the user for a number and print its factorial (1p)

def factorial(n):
    a = 1
    n = float(n)
    n = int(n)
    if n < 0:
        print ("podales liczbe mniejsza od 0, brak silni")
    elif (n%1!=0):
        print ("hola")
    else:
        for i in range(1, n+1):
            a = a*i
        return a

print("Insert a integer: ")
n = (input())
print('Factorial of ', n, " is ", factorial(n))

#3: write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
print("Insert a size of an array:")
s=int(input())
tab = []
print("Insert numbers to an array:")
for i in range(0, s):
    tab.append(int(input()))

print("Inserted array: ", tab)

def find_lowest_value(tab):
    min = tab[0]
    minIndices = []
    #amount = 0
    for i in range(0, len(tab)):
        if (tab[i] < min):
            min = tab[i]

    print("The lowest value is ", min, "state on position (counting from 0): ")

    for i in range(0, len(tab)):
        if (tab[i] == min):
            minIndices.append(i)

    print(minIndices)


   # print("\nThere are ", amount, " the same min numbers")

find_lowest_value(tab)

#4
f = open("input.txt")
data = int(f.read())
x = linspace(0, 6.28, data)
y = sin(x)
plot(x, y)
show()
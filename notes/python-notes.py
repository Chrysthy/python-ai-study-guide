# 🧠 Python Study Notes

#This document contains structured notes based on curated materials and AI-assisted learning.

# Variables

# Variables are used to store data in Python.

name = "Chrystine"
age = 34
is_active = True


# Data Types

# Common data types:

# Integer → 10
# Float → 10.5
# String → "Hello"
# Boolean → True / False]


# Lists vs Tuples

# List (mutable)
numbers = [1, 2, 3]
numbers.append(4)

# Tuple (immutable)
numbers = (1, 2, 3)

# Use lists when data can change
# Use tuples when data should remain constant


# Control Structures

# If / Else
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Loops
#For loop 

for i in range(5):
    print(i)


# While loop
count = 0

while count < 5:
    print(count)
    count += 1

# Use for when you know the number of iterations
# Use while when the condition controls the loop


# Functions

# Functions allow code reuse and organization.

def greet(name):
    return f"Hello, {name}"

print(greet("Maria"))

# Functions improve readability and avoid repetition


# Object-Oriented Programming (OOP)

#Basic example:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Ana")
print(p.greet())

# OOP helps organize complex programs
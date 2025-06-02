"""
Assignment: Exploring Python Concepts

This script covers three foundational topics in Python programming: variables, operators,
and conditional statements. It is designed as an introductory assignment to reinforce
basic syntax, logical thinking, and output formatting.

Tasks included:
1. Variables – Stores and prints a personalized message using a name, age, and height.
2. Operators – Performs arithmetic operations (addition, subtraction, multiplication, division)
   between two numbers and displays the results with explanatory messages.
3. Conditional Statements – Prompts the user to enter a number and determines whether it is
   positive, negative, or zero using if-elif-else logic.

Jordan Wang
6/2/2025
"""

# Task 1 - Variables: Your First Python Intro

name = "Jordan"
age = 23
height = 6.6

print(f"Hello! My name is {name}. I am {age} years old and my height is {height} feet.")
print("I play basketball and like to wear jersey number 6. I’m passionate about the game and always aim to improve.")


# Task 2 - Operators: Playing with Numbers

# Define two numbers to work with
num1 = 8
num2 = 4

# Perform basic arithmetic operations and print the results

# Addition
print(f"The sum of {num1} and {num2} is {num1 + num2}")

# Subtraction
print(f"The difference between {num1} and {num2} is {num1 - num2}")

# Multiplication
print(f"{num1} multiplied by {num2} equals {num1 * num2}")

# Division
print(f"{num1} divided by {num2} equals {num1 / num2}")


# Task 3: The Number Checker - Using Conditional Statements

# Ask the user to input a number.
num = float(input("Enter a number and I’ll tell you its vibe: "))

# then we will check whether the number is positive, negative, or zero
if num > 0:
    print("This number is positive. Awesome!")
elif num < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")

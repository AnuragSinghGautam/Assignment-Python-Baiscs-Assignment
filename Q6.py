#  How do conditional statements work in Python? Illustrate with examples
Python's conditional statements, if, elif, and else, execute code based on whether a condition is true or false.

1.If Statement:

The if statement checks if a condition is true, and if it is, the code block within the if statement is executed.
Ex:
x = 10
if x > 5:
    print("x is greater than 5")

2. If-else Statement:

The if-else statement is a conditional statement that executes an alternative block of code if the condition is false.
Ex:
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

3.If-elif-else Statement:

The if-elif-else statement enables sequential checking of multiple conditions, with the first condition evaluating to true being executed.
Ex:
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")

Conditional statements in Python enable dynamic and flexible program execution by executing code blocks based on whether specified conditions are true or false.


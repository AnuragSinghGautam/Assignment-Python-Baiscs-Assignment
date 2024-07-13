#  Describe the different types of loops in Python and their use cases with examples.
Python has two main types of loops: for loops and while loops, each serving different purposes and suitable for different scenarios.

1. for Loop

A for loop is a method used to iterate over a sequence or other iterable objects, particularly when the number of iterations is known beforehand.
Ex:
#list example
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

#strings example
word = "hello"
for char in word:
    print(char)

#dictionary example
fruits = {'apple': 1, 'banana': 2, 'cherry': 3}
for key, value in fruits.items():
    print(f"{key}: {value}")
Use Cases for for Loop:
    
This text explains the functions for iterating over elements in a list, tuple, set, or dictionary, repeating code, accessing elements and indices, and iterating over multiple sequences.

2. while Loop

A while loop is a code execution method that repeatedly executes a block of code if a certain condition is true.
Ex:
# Counting 
count = 0
while count < 5:
    print(count)
    count += 1

Use Cases for while Loop:
This involves repeatedly executing a code block until a specific condition is met, executing indefinite loops that require a condition to be met before termination.

3. Nested Loops:

Loops can be nested within each other to create more complex iterations.
Ex:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()

4. Control Statement:
Python offers control statements to modify loop flow, including break, continue, and else, which exit the loop prematurely, skip iterations, or execute code if the loop is not terminated.
Ex:
# Using break
for num in range(10):
    if num == 5:
        break
    print(num)

# Using continue
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# Using else with loop
for num in range(5):
    print(num)
else:
    print("Loop completed")

The loop is best for iterating over a known sequence of elements or a fixed number of times, while the loop is best when the number of iterations is unknown and depends on a condition. Nested loops are used for complex iterations over multi-dimensional data structures.




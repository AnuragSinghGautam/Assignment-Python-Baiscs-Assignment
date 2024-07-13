# Explain the concept of type casting in Python with examples
Type casting in Python is the conversion of one data type into another, a useful operation that uses built-in functions for specific data types.

Implicit Typecasting:
Python can automatically convert one data type to another through implicit type casting.
Ex:
a = 10
b = 3.14
c = a + b
print(c)

Explicit Type casting:
Expressive type casting is a manual conversion method used by programmers to use built-in functions.
Ex:
a = "100"
b = int(a)
print(b)



1. To convert to an integer
Ex:
a = "56"
b = 3.14
c = int(a)
d = int(b)
print(c)  
print(d)  

2. To convert to a float
Ex:
a = "763.223"
b = 5
c = float(a)
d = float(b)
print(c)  
print(d)  

3.To convert to a String
Ex:
a = 123
b = 45.67
c = str(a)
d = str(b)
print(c)  
print(d)  

4.To convert to list
Ex:
a = "hello"
b = (1, 2, 3)
c = list(a)
d = list(b)
print(c)  
print(d)  

5.To convert to dictionary
Ex:
a = [("name", "Alice"), ("age", 25)]
c = dict(a)
print(c)  





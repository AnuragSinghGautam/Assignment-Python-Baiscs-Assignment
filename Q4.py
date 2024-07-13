#  Discuss the different types of operators in Python and provide examples of how they are used

There are different types of operators in python. Some of them are listed below:
1. Arithmetic Operators:
Used for mathematical Operations
These include addition(+),substraction(-),multiplication(*),division(/),modulus(%),floor division(//),exponential(**)

Example:
a = int(input("Enter first num: "))
b = int(input("Enter second num: "))

print(a + b)  
print(a - b)  
print(a * b)  
print(a / b)  
print(a % b)  
print(a ** b) 
print(a // b) 

2.Comparison OPerator:
Used for comaprison between two or more things
These include == (Equal to),!= (Not equal to),> (Greater than),< (Less than),>= (Greater than or equal to),<= (Less than or equal to)

Example:
a = 26
b = 14
print(a == b)  
print(a != b)  
print(a > b) 

3.Logical Operators:
Used for combining conditional statements
These include and,or,not

Example:
a = True
b = False
print(a and b)  
print(a or b)   
print(not a)  

4.Bitwise Operators:
Used for bitwise Operations
Include &,^,|,~,>>,<<

Example:
a = 5  
b = 8 
print(a & b)  
print(a | b)  
print(a ^ b)  
print(~a)     
print(a << 1) 
print(a >> 1) 

5.Assignment Operators:
Used in assigning values to variables
Include =,+=,-+,*=,/=,%=

Example:
a = 6
a += 5  

6.Identity Operator:
Used to compare the memory locations (kind of like pointers)
Includes is and is not

Example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)    
print(a is c)    
print(a is not c) 

7.Membership Operators:
Used to check if something is present in or not
Includes in and not in

Example:
a = [1, 2, 3]
print(2 in a)      
print(4 in a)       
print(4 not in a)   

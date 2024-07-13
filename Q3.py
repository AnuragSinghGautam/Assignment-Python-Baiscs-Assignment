#  Compare and contrast mutable and immutable objects in Python with examples

# Answers:

# Mutable Objects:
# Mutable objects, like lists, dictionaries, and sets, can be modified post-creation, allowing for addition, removal, or change of elements, and maintaining the same memory location.

# Example:

list = [1, 2, 3]
print(list)  
 
list[1] = 10
print(list)  

# Immutable Objects:
# Immutable objects, like strings, tuples, and numbers, cannot be altered post-creation. Any modification results in a new object, and any change to the value assigns a new memory location.

# Example:

my_string = "hello"
print(my_string)  


new_string = string[0]='a' //showcases error
print(new_string)  
print(my_string)   
  
# Key Differences:
#  Mutable objects can be modified in place, while immutable objects cannot. They use the same memory location for updates and create new objects with new locations for each modification. Immutable objects are more efficient for read-only operations.
# Mutable Objects are useful for dynamic object modification, like dynamic list building, while Immutable Objects are suitable for fixed data structures and avoiding unwanted side effects.
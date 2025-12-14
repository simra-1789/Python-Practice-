# TOPIC: VARIABLES , DATATYPES AND OPERATORS
# SOURCE: Codewithharry

# Variable
a = 1 
b = 3 
c = 5
name = "simra" # string 

print(a + b - c)
print(a + c)
print(b - c)
print(name)

# Datatypes
a = 2  # a is a integer
b = 1.33  # b is a floting point number
c = "simra"  # c is a string 
d = True  # d is a boolean variable
e = None  # e is a none type variable

# Rules for variables

aaa = 33   # valid
harry = 45   # valid 
_simra = 10   # valid
s9_ = 32   # valid 

# 4s = 4  invalid due to starting digit 
# @simra = 55  invalid due to special character @ symbol
# h@rry  invalid due to @ symbol

# Operators
# Arithmetic operators
a = 1
b = 3 
c = a + b 
d = b - a
print(c)
print(d)

# Assignment operators
a = 4-2 # assign 4-2 in a 
print(a)

b = 6
b += 3  # Increment the value of b by 3 and then assign it to b  
b -= 3  # Decrement the value of b by 3 and then assign it to b 
print(b)

# Comparison operators
d = 5==5
print(d)

d = 5 < 4 
print(d)

d = 5 > 4
print(d)

d = 5 <= 4
print(d)

d = 5 >= 5
print(d)

d = 5 != 5
print(d)

# Logical operators
e = True or False 
print (e)

# Truth table of 'or'
print("True or False is " , True or False)
print("True or True is ", True or True) 
print("False or True is ", False or True)
print("False or False is", False or False)

# Truth table of 'and'
print("True and False is", True and False)
print("True and True is", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

# Not operator
print(not(True))
print(not(False))


# Type() Function to know the type of a variable
a = 31
t = type(a)  # class <int>
print(t)

a = 31.2
t = type(a)  # class <float>
print(t)

a = "simra"
t = type(a)  # class <str>
print(t)

# Convert one type to another
a = "13.2"
b = float(a) # a is a string but the type should be float
t = type(b)   # string to float conversion
print(t)

a = 31.2
b = int(a)  # float to integer conversion
t = type(b)
print(t)

# Input numbers
a = input ("Enter number 1: ")
b = input ("Enter number 2: ")

print("Number a is: ", a)   # a is 45
print("Number b is: ", b)   # b is 25
print("Sum is ", a + b)    # sum is 4525. it won't sum numbers unless we give it an integer type

a = int(input ("Enter number 1: "))
b = int(input ("Enter number 2: "))
print("Number a is: ", a)   # a is 45
print("Number b is: ", b)   # b is 25
print("Sum is ", a + b)    # sum is 70 
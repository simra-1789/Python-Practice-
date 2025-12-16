# TOPIC: VARIABLES , DATATYPES AND OPERATORS
# SOURCE: Codewithharry

# Problem1
# Add two numbers
a = 3
b = 5
print(a + b)

# Problem2
# Find remainder when 'a' is divided by 'b'
a = 34
b = 5
print("Remainder when a is divided by b is", a % b)

# Problem3
# Find the type of 'a' by using input() function 
a = input(" Enter the value of a: ")
print(type(a))

# Problem4
# Find if 'a' is greater than 'b' or not by using comparison operator
a = 34
b = 80
print(a > b)

a = int(input("Enter number 1: ")) 
b = int(input("Enter number 2: "))  
print("a is greater than b is", a > b)

# Problem5
# Find the average of two numbers
a = int(input("Enter number 1: ")) 
b = int(input("Enter number 2: "))  
print(" The average of these two number is", (a+b)/2)

# Problem6
# Find the square of the number
a = int(input("Enter your number ")) 
print("The square of the number is", a**2)

# Problem7
# Print this line 'name likes color.' using input()
name = input("what is your name ")
color = input("what is your favourite color ")
print( f"{name}  likes  {color}." )   # new style prefered here f is a formatted string which insert the value of variable dynamically
print( name + " likes " + color)      # old style not ideal

# Problem8
# Input side of a square and print the area
side = float(input("enter square side: "))
print(" area = ", side * side)

# Problem9
# Input 2 floating point numbers and print their average
first = float(input("Enter number 1: "))
second = float(input("Enter number 2: "))
print(" the average is ", (first + second)/2)

# Problem10
# Input 2 int numbers and print if 'a' is greater than or equal to 'b'
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
print("a is greater than or equal to b = ", a >= b ) 
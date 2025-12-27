# TOPIC: Functions & Recursions 
# SOURCE: Codewithharry

#Function Definition
def avg():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))

    average = (a + b + c)/3
    print(average)

avg()  #Function Call
print("Thank you!")
avg() 

#Quick Quiz:  Write a program to greet a user with “Good day” using functions.
def greet():
    name = input("Enter name: ")

    print(f"Good Day {name}")
    print("Have a nice day")

greet()

#Function with arguments
def greet(name , ending):     #name & ending in the parentheses are called parameters
    print(f"Good Day {name}")
    print(ending)

greet("simra", "Thank you")    #Here strings are called arguments 
greet("saira", "Thank you")

#With return value
def greet(name , ending):     
    print(f"Good Day {name}")
    print(ending)
    return "OK"

a = greet("simra", "Thank you")
print(a)

#Default parameter value
def greet(name , ending = "Thank you"):  #Here ending has it's default value    
    print(f"Good Day {name}")
    print(ending)

greet("simra", "Thanks")
greet("saira")

#Recursive Function
def show(n):
    if(n==0):    #Here this condition is called Base case, which is imporatnt to stop program
        return
    
    print(n)
    show(n-1)

show(5)

#2nd example
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x n-1 x....3 x 2 x 1

factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

#3rd example
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n-1 + n
sum(n) = sum(n-1) + n
'''
def total(n):
    if(n == 1):
        return 1
    return n + total(n-1)

print(total(5))

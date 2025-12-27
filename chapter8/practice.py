# TOPIC: Functions & Recursions 
# SOURCE: Codewithharry

#Problem1
#Write a program using functions to find greatest of three numbers.
def greatest(a , b , c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = 2
b = 34
c = 33
print(greatest(a, b, c)) 

#Problem2
#Write a python program using function to convert Celsius to Fahrenheit.
def c_to_f(c):
    return (c * 9/5) + 32

c = float(input("Enter temperature in C: "))
f = c_to_f(c)
print(f"{f}°F")

#Fahrenheit to Celsius
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

#Problem3
#How do you prevent a python print() function to print a new line at the end.
print("a")
print("b", end="")
print("c", end="")

#Problem4
#Write a recursive function to calculate the sum of first n natural numbers.
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
    if(n==1):
        return 1
    return total(n-1) + n

print(total(4))

#Problem5
# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 
def pattern(n):
    if(n==0):
        return
    print("*"* n)
    pattern(n-1)

pattern(3) 

#Problem6
#Write a python function which converts inches to cms. 
def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cm is: {inch_to_cm(n)}")

#Problem7
#Write a python function to remove a given word from a list and strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["simra", "saira", "muniba", "hamzan", "fasih", "n"] 
print(rem(l, "n")) 

#Problem8
#Write a python function to print multiplication table of a given number.
def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter number: "))
multiply(n)        

#Practice1
#WAF to print the length of a"" list. (list is the parameter)
cities = ["karachi","lahore","islamabad","hyderabad","gujranwala","peshawar"]

def print_len(city):
    print(len(city))

print_len(cities)    

#Second way
def calc_length(l):
    return len(l)

length = calc_length([1,3,4,5,6,7,8,9,2])
print(length)

#Practice2
#WAF to print the elements of a list in a single line. ( list is the parameter)
marks = ["simra", 98, "saira", 89]
cities = ["karachi","lahore","islamabad","hyderabad","gujranwala","peshawar"]

def print_list(l):
    for item in l:
        print(item, end=" ")

print_list(marks)
print_list(cities)        

#Practice3
#WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact) 

cal_fact(5)       

#Second way
def factorial(n):
    if(n == 0 or n==1):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
fact = factorial(n)
print(fact)

#Practice4
#WAF to convert USD to PKR.
'''
1 USD = 280 PKR
PKR = USD x 280
'''
def usd_to_pkr(usd):
    pkr =  usd * 280
    print( usd, "USD =", pkr, "PKR")

usd = float(input("Enter amount in USD: "))
usd_to_pkr(usd) 

#WAF to convert PKR to USD.
'''
1 USD = 280 PKR
USD = PKR ÷ 280
'''
def pkr_to_usd(pkr):
    usd =  pkr / 280
    print( pkr, "PKR =", round(usd), "USD")

pkr = float(input("Enter amount in PKR: "))
pkr_to_usd(pkr)

#Practice5
#WAP to find if number is odd or even using function.
def finding():
    if(n%2 == 0):
        print("Number is Even")

    else:
        print("Number is Odd")

n = int(input("Enter number: "))
finding()

#Practice6
#Write a recursive function to print all elements in a list. Hint : use list & index as parameters.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", "banana", "mango", "strawberry"]
print_list(fruits)     
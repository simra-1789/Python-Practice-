# TOPIC: Loops in Python 
# SOURCE: Codewithharry

#Problem1
#WAP to print multiplication table of a given number using for_loop
n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#Problem2
#Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 
l = ["Hamza", "Simra", "Saira", "Muniba"] 

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

#Problem3
#Attempt problem 1 using while loop. 
n = int(input("Enter number: "))

i = 1
while(i<11):
    print(f"{n} x {i} = {n * i}")
    i += 1

#Problem4    
#Write a program to find whether a given number is prime or not.
n = int(input("Enter number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break

else:
    print("Number is prime")

#Problem5
#Write a program to find the sum of first n natural numbers using while loop.
n = int(input("Enter number: "))

i = 1
total = 0
while(i <= n):
    total += i
    i += 1

print("total sum =", total)

#Problem6
##Write a program to find the factoial of first n natural numbers using for loop.
n = int(input("Enter number: "))
product = 1

for i in range(1, n+1):
    product *= i

print(f"the factoial of {n} is {product}")

#Problem7
#Write a program to print the following star pattern. 
#    * 
#   *** 
#  ***** for n = 3 
n = int(input("Enter number: "))

for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

#Problem8
# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3
n = int(input("Enter number: "))

for i in range(1, n+1):
    print("*"* i, end="")
    print("")

#Problem9
#Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 
n = int(input("Enter number: "))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*"* n, end="")

    else:
        print("*" , end="")
        print(" "* (n-2), end="")
        print("*", end="")    
    
    print("")

#Problem10
# Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter number: "))

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n*i}")

#Second way
n = int(input("Enter number: "))

for i in range(1 , 11):
    print(f"{n} x {11 -i} = {n*(11-i)}")

#Practice1
#Print numbers from 1 to 100.
i = 1
while(i <= 100):
    print(i)
    i += 1

#Practice2
#Print numbers from 100 to 1.
i = 100
while(i >= 1):
    print(i)
    i -= 1

#Practice3
#Print the multiplication table of number n.
n = int(input("Enter number: "))

i = 1
while(i <= 10):
    print(f"{n} x {i} = {n * i}")
    i += 1

#Practice4
#Print the elements of the following list using while loop.
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while(idx < len(l)):
    print(l[idx])
    idx += 1

#Practice5
#Search for a number x in this tuple using while loop.
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36
i = 0
while(i < len(t)):
    if(t[i] == x):
        print("Found at idx", i)
    else:
        print("Finding..")
    i += 1 

#Practice6
#Print the elements of the following list using for loop. 
l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in l:
    print(i)

#Practice7
#Search for a number x in this tuple using for loop.
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
idx = 0
for i in t:
    if(i == x):   #Linear search 
        print("number found at idx", idx)
    idx += 1  

#Practice8
#Print the numbers from 1 to 100 using for and range.
for i in range(1, 100):
    print(i)      

#Practice9
#Print the numbers from 100 to 1 using for and range.
for i in range(101, 0, -1):
    print(i)     

#Practice10
#Print the multiplication table of number n.
n = int(input("Enter number: "))

for i in range(1 , 11):
    print(f"{n} x {i} = {n * i}")

#Practice11
#WAP to find the sum of first natural numbers by using for loop.
n = int(input("Enter number: "))
total = 0

for i in range(1, n+1):
    total += i
print("total sum =", total) 

#Practice12
#WAP to find factorial of first natural numbers using for and while loop.
n = int(input("Enter number: "))
fact = 1
i = 1
while(i <= n):
    fact *= i
    i += 1
print("factorial =", fact) 

n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact *= i
print("factorial =", fact) 
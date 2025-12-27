# TOPIC: LIST and TUPLE 
# SOURCE: Codewithharry

# Problem1
# Ask user to input 7 fruits in a list 
fruits = []
f1 = input("Enter fruit : ")
fruits.append(f1)
f2 = input("Enter fruit : ")
fruits.append(f2)
f3 = input("Enter fruit : ")
fruits.append(f3)
f4 = input("Enter fruit : ")
fruits.append(f4)
f5 = input("Enter fruit : ")
fruits.append(f5)
f6 = input("Enter fruit : ")
fruits.append(f6)
f7 = input("Enter fruit : ")
fruits.append(f7)

print(fruits)

# Problem2
# Ask 6 students to input marks in sort list 
marks = []
f1 = int(input("Enter marks : "))
marks.append(f1)
f2 = int(input("Enter marks : "))
marks.append(f2)
f3 = int(input("Enter marks : "))
marks.append(f3)
f4 = int(input("Enter marks : "))
marks.append(f4)
f5 = int(input("Enter marks : "))
marks.append(f5)
f6 = int(input("Enter marks : "))
marks.append(f6)
f7 = int(input("Enter marks : "))
marks.append(f7)

marks.sort()
print(marks)

# Problem3
a = (3, 78 ,"simra")
a[2] = "samra"   # here it will show error because tuple is immutable

# Problem4 
a = [1, 4, 6, 7]
print(sum(a))

# Problem5
# Write a program to count 0 in the tuple 
a = (2, 0 , 4, 0 , 5 , 0)
n = a.count(0)
print(n)

#Problem6
#WAP to ask user put 3 movies names and print them in the list
movie = []
m1 = input("enter first movie name: ")
movie.append(m1)
m2 = input("enter second movie name: ")
movie.append(m2)
m3 = input("enter third movie name: ")
movie.append(m3)

print(movie)

#Problem7
#WAP to check if list is a palindrome or not using copy method
list1 = [1,2,1,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome") 

#Problem8
# WAP to count number of students with "A" grade in the tuple  
grade = ('C' , 'D' , 'A', 'A', 'B' , 'A')
print(grade.count('A'))

#Problem9
#store the above values in a list and sort them from 'A' to 'D'
Grade = ['C', 'D', 'A', 'A', 'B', 'A']
Grade.sort()
print(Grade)  

#Problem1
# Ask the user to enter 5 favorite movies and store them in a list. Print the final list
movies = []

movie1 = input("Enter movie 1 name: ")
movies.append(movie1)
movie2 = input("Enter movie 2 name: ")
movies.append(movie2)
movie3 = input("Enter movie 3 name: ")
movies.append(movie3)
movie4 = input("Enter movie 4 name: ")
movies.append(movie4)
movie5 = input("Enter movie 5 name: ")
movies.append(movie5)

print(movies)    # Output: ['chucky', 'harry potter', 'conjuring', 'All of us are dead', 'Zombie night']

#Problem2
# Take 6 numbers from the user, store them in a list, and: Print the list, Print the maximum and minimum number
numbers = []

num1 = int(input("Enter number 1: "))
numbers.append(num1)
num2 = int(input("Enter number 2: "))
numbers.append(num2)
num3 = int(input("Enter number 3: "))
numbers.append(num3)
num4 = int(input("Enter number 4: "))
numbers.append(num4)
num5 = int(input("Enter number 5: "))
numbers.append(num5)
num6 = int(input("Enter number 6: "))
numbers.append(num6)

print(numbers)     # Output: [3, 2, 6, 13, 7, 8]
print(max(numbers), min(numbers))    # Output: 13 2

#Problem3
# Write a program to check whether a tuple can be modified or not.
# (Show this by trying to change a value and explain using a comment.)
tup = (1, 2, 3, 4, 5) 

tup[1] = 6   # This will give us error like TypeError: 'tuple' object does not support item assignment. it's because tuples are immutable and we can't change values by index once added like strings and sets.
print(tup)

#Problem4
# Create a list of 4 integers entered by the user and print: The sum of all elements, The average of the list
integers = []

No1 = int(input("Enter number 1: "))
integers.append(No1)
No2 = int(input("Enter number 2: "))
integers.append(No2)
No3 = int(input("Enter number 3: "))
integers.append(No3)
No4 = int(input("Enter number 4: "))
integers.append(No4)

print("Sum: ",sum(integers))          # Output: Sum: 18 
print("Average: ",sum(integers)/4)   # Output: Average:  4.5

#Problem5
# Given a tuple: t = (1, 0, 2, 0, 3, 0, 4). Count how many times 0 appears in the tuple.
t = (1, 0, 2, 0, 3, 0, 4)

print("Count of 0 in a tuple is: ",t.count(0))  # Output: Count of 0 in a tuple is:  3

#Problem6
# Ask the user to enter 5 numbers, store them in a list, and display the list in: Original order, Sorted order (ascending)
L = []

L1 = int(input("Enter number 1: "))
L.append(L1)
L2 = int(input("Enter number 2: "))
L.append(L2)
L3 = int(input("Enter number 3: "))
L.append(L3)
L4 = int(input("Enter number 4: "))
L.append(L4)
L5 = int(input("Enter number 5: "))
L.append(L5)

print(L)  # Output: [32, 12, 4, 23, 8]
L.sort()
print(L)  # Output: [4, 8, 12, 23, 32]

#Problem7
# Create a list with mixed data types: [item_name, price, quantity], Print each element with its data type.
item = ["Iphone",999.99,1 ]

print(item[0], type(item[0]))  # Output: Iphone <class 'str'>
print(item[1], type(item[1]))  # Output: 999.99 <class 'float'>
print(item[2], type(item[2]))  # Output: 1  <class 'int'>

#Problem8
# Write a program to check if a number entered by the user exists in a list: numbers = [10, 20, 30, 40, 50], Print True or False.
numbers = [10, 20, 30, 40, 50]

print(20 in numbers)  # Output: True and if I put 60 instead of numbers exits in a list will give me False.

#Problem9 Extra for practice.
#WAP to show positive and negetive slicing.

num = [1, 2, 3, 4, 5]   #last_index always excluded  
    #  0  1  2  3  4

t = (1, 2, 3, 4, 5)     #negative slicing start from -1 and since it's last so it's also excluded
  # -5  -4 -3 -2 -1

print(num[1:3])    #Output: [2, 3]
print(t[-3:-1])    #Output: (3, 4) 
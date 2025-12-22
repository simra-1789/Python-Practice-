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

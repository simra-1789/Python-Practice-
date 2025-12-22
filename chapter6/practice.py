# TOPIC: Conditional Expression
# SOURCE: Codewithharry

#Problem1
#WAP to find the greatest of 4 numbers entered by the user.
a1 = int(input("Enter number: "))
a2 = int(input("Enter number: "))
a3 = int(input("Enter number: "))
a4 = int(input("Enter number: "))

if( a1>a2 and a1>a3 and a1>a4 ):
    print("Greatest number is a1 :", a1)

elif( a2>a1 and a2>a3 and a2>a4 ):
    print("Greatest number is a2 :", a2)

elif( a3>a1 and a3>a2 and a3>a4 ):
    print("Greatest number is a3 :", a3)

elif( a4>a1 and a4>a2 and a4>a3 ):
    print("Greatest number is a4 :", a4) 

#Problem2
#WAP to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. assume 3 subjects and take marks as an input by the user.
sub1 = int(input("Enter sub1 marks: "))           
sub2 = int(input("Enter sub2 marks: "))           
sub3 = int(input("Enter sub3 marks: "))

#Check for total percentage
total_Percentage = (100*(sub1 + sub2 + sub3))/300

if(total_Percentage > 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("You have passed exam: ", total_Percentage)

else:
    print("You failed: ", total_Percentage)

#Problem3
#A spam comment is defined as a text containing following keywords: "Make a lot of money" , "Buy now" , "Subscribe this" , "Click this". WAP to detect these spams.
p1 = "Make a lot of money"        
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

comment = input("Enter your comment: ")

if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("this comment is a spam")

else:
    print("this comment is not a spam")

#Problem4
#WAP to find whether given username contains less than 10 characters or not.
username = input("Enter username: ")

if(len(username) < 10):
    print("Your username contains less than 10 characters")

else:
    print("Your username contains more than or equal to 10 characters")

#Problem5
#Find whether given name exits in list or not.
l = ["simra", "saira", "muniba", "hamza"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")

else:
    print("Your name is not in the list")    

#Problem6
#WAP to calculate the grade of a student from his marks from the following scheme.
marks = int(input("Enter your marks: "))

if(marks <= 100 and marks > 90):
    grade = "Ex"

elif(marks < 90 and marks >= 80):
    grade = "A" 

elif(marks < 80 and marks >= 70):
    grade = "B" 

elif(marks < 70 and marks >= 60):
    grade = "C" 

elif(marks < 60 and marks >= 50):
    grade = "D" 

elif(marks < 50 ):
    grade = "F"    

print("Your grade is: ", grade)

#Problem7
#WAP to find out whether a post is talking about simra or not.
post = input("Enter your post: ")

if("simra" in post.lower()):
    print("This post is talking about simra")

else:
    print("This post is not talking about simra") 

#Problem8
#WAP to check if a number entered bu the user is odd or even
number = int(input("Enter number : "))

if(number % 2 == 0):
    print("number is even")

else:
    print("number is odd")

#Problem9
#WAP to find the greatest of 3 numbers entered by the user  
num1 = int(input("Enter number 1: "))       
num2 = int(input("Enter number 2: "))       
num3 = int(input("Enter number 3: "))

if(num1 > num2 and num1 > num3):
    print("num1 is greater: ", num1)

elif(num2 > num1 and num2 > num3):
    print("num2 is greater: ", num2)

elif(num3 > num1 and num3 > num2):
    print("num3 is greater: ", num3)

#Problem10
#WAP to check if a number is multiple of 7 or not.
no = int(input("Enter number : "))

if(no % 7 == 0):
    print("number is multiple of 7: ", no)

else:
    print("number is not multiple of 7: ", no)    
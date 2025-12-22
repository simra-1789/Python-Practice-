# TOPIC: Conditional Expression  
# SOURCE: Codewithharry

# if else statement
age = int(input("Enter your age: "))

if(age >= 18):
    print("You can vote")  # Here 4 spaces is called indentation.
else:
    print("You cannot vote")    

# if_elif_else ladder
a = int(input("Enter your age: "))

# if statement no: 1.
if(a%2 == 0):
    print("a is even")
# End of if statement no: 1.    

# if statement no: 2.
if(a >= 18):
    print("You can vote")

elif(a < 0):
    print("You are entering invalid age")

elif(a == 0):
    print("You are entering 0 which is not a valid age")  

else:
    print("You cannot vote")   
#End of if statement no: 2.

print("End of the program")

# if_elif statement
light = "color"      # Assign values to variables or ask for input from user.
light = input("Enter traffic light color: ")

if(light == "red"):
    print("Stop")

elif(light == "green"):
    print("Go")

elif(light == "yellow"):
    print("Look or wait")

print("End of code") 

# Use 'if' multiple times
number = 5

if(number > 3):   # 'if' always checks for condition but elif & else is ignored whether 'if' condition is True or not than it checks for 'elif' & 'else'.
    print("Greater than 3")

if(number > 2):
    print("Greater than 2") 

if(number > 4):
    print("Greater than 4") 

#Grade system
marks = int(input("Enter your marks: "))

if(marks >= 90):
    grade = "A"

elif(marks >= 80 and marks < 90):
    grade = "B"

elif(marks >= 70 and marks < 80):
    grade = "C"

elif(marks >= 60 and marks < 70):
    grade = "D"

else:
    grade = "F"

print("Your grade is: ", grade)

#Nesting or nested if_else
age = 70

if(age >= 18):

    if(age >= 70):
        print("cannot drive")

    else:
        print("can drive")

else:
    print("cannot drive")                
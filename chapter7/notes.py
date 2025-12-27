# TOPIC: Loops in Python 
# SOURCE: Codewithharry

# for_loop
for i in range(1,6): #(start, stop) condition # range(6) can also be used. 
    print(i)

# while_loop 
i = 1             #Here 'i' is call iterater and the operation it does calls iteration
while(i <= 5):    #The block keeps executing until the condition is true
    print(i)
    i += 1 # or i = i + 1

i = 5
while(i >= 1 ):    
    print(i)
    i -= 1

#Infinite loop example which we don't need to write even by mistake.
# i = 5
# while(i < 6 ):    
#     print(i)
#     i -= 1    

#Quick quiz: write a program to print 1 to 50 using while loop.
i = 1
while(i < 51):    #The block keeps executing until the condition is true
    print(i)
    i += 1 

#Quick quiz: write a program to print content of a list using while loop.
l = [1, "simra", True,"saira",12.0]
i = 0

while(i<len(l)):
    print(l[i])
    i += 1

#for loop with lists
l = [1, 34, 45, 21, 12]

for i in l:
    print(i)

#for loop with tuples
t = (2, 34 , 55, 12, 11)

for i in t:
    print(i)

#for loop with strings
s = "simra"

for i in s:
    print(i)

#step_size
for i in range(0 , 11 , 2):  #range(start, stop , step_size) step size is for increaseing number by 1 , 2, 3, 4 like this.
    print(i)                            #range_condition

#for loop with else
l = [1, 2, 34, 56]

for i in l:
    print(i)

else:
    print("done")   #this is printed when loop is exhausts! 

#Break in loops
for i in range(100):
    if(i == 36):
        break     # It instructs to Exist the loop right now
    print(i) 

t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36
i = 0
while(i < len(t)):
    if(t[i] == x):
        print("Found at idx", i)
        break
    else:
        print("Finding..")
    i += 1      

#Continue in loops
for i in range(100):
    if(i == 34):
        continue     # It instructs to Skip this iteration
    print(i)

i = 0
while(i <= 5):
    if(i == 3):
        i += 1
        continue 
    print(i)
    i += 1

i = 0
while(i <= 10):
    if(i%2 == 0):
        i += 1
        continue 
    print(i)
    i += 1 

i = 0
while(i <= 10):
    if(i%2 != 0):
        i += 1
        continue 
    print(i)
    i += 1         

#Pass in loops
for i in range(51):
    pass   # pass is a null statement in python. It instructs to “do nothing”. 

i = 0
while(i < 46):
    print(i)
    i += 1
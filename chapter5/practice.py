# TOPIC: Dictionary And Sets  
# SOURCE: Codewithharry

#Problem1
# WAP to create a dictionary of urdu words as their english translation. provide user with an option to look it up.
words = {
    "madad": "help",
    "kursi": "chair",
    "billi": "cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])

#Problem2
#Ask user to input 8 numbers and print all the unique numbers
s = set()
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))
no = input("Enter number: ")
s.add(int(no))

print(s)

#Problem3
# Can we have a set with 18 as int and "18" as string value in it. 
t = set()
t.add(18)
t.add("18")
print(t)

#Problem4
#what will be the length of following set si
si = set()
si.add(20)
si.add(20.0)
si.add("20")
print(len(si))

#Problem5
#What will be the type of this 
a = {}
print(type(a))

#Problem6
#WAP to ask user to put their favourite language as a value in dictionary and the key should be unique
d = {}
name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)

#Problem7
#if the names of 2 friends are same; what will happen to the program in problem 6.
di = {}
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di.update({name: lang})

print(di)

#Problem8
#if the language of 2 friends are name; what will happen to problem 6.
di1 = {}
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di1.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di1.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di1.update({name: lang})
name = input("Enter friend name: ")
lang = input("Enter language name: ")
di1.update({name: lang})

print(di1)

#Problem9
#Can you change the values inside a list which is contained in set S.
S = {8, 7, 12, "simra", [1,2]}  # LIst are not allowed in sets because list is mutable and unhashable. 
# S[4][1] = 9
# print(S)  #This will give us type error like unhashable type list. instead we can use tuple becuase it is immutable and hashable.

#Problem10
#Store word and meaning in dictionary
D = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}
print(D)

#Problem11
#You are given a list of subjects for students. Assume that 1 classroom is required for 1 subject. how many classrooms are needed by all students.
sets = {"Python","Java","C++","Python","Javascript","Java","Python","Java","C++","C"}
print(len(sets))

#Problem12
#WAP to enter marks of 3 subjects by the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as key & marks as values.
sub = {}
subject = input("Enter subject: ")
marks = int(input("Enter your marks: "))
sub.update({subject: marks})
subject = input("Enter subject: ")
marks = int(input("Enter your marks: "))
sub.update({subject: marks})
subject = input("Enter subject: ")
marks = int(input("Enter your marks: "))
sub.update({subject: marks})

print(sub)

#Second way
sub1 = {}

marks = int(input("Enter python marks: "))
sub1.update({"python": marks})

marks = int(input("Enter javascript marks: "))
sub1.update({"javascript": marks})

marks = int(input("Enter html marks: "))
sub1.update({"Html": marks})

print(sub1)

#Problem13
#find a way to store 9 & 9.0 in a set as different values
values = {9 , "9.0"}
 
print(values)

#Second way
value = {("int", 9),("float", 9.0)}
print(value)

#Problem1
# Create a dictionary with 5 country names as keys and their capitals as values.
# Ask the user to enter a country name and display its capital.
countries = {
    "South Korea": "Seoul",
    "Pakistan": "Islamabad",
    "USA": "Washington, D.C.",
    "Japan": "Tokyo",
    "China": "Beijing"
}
capital = input("Enter country name: ")

print(countries[capital])   # Output: Enter country name: South Korea 
                            # Seoul

#Problem2
# Take 5 numbers from the user and store them in a list.
# Convert the list into a set and print the set to show only unique numbers.
numbers = []

no1 = int(input("Enter number 1: "))
numbers.append(no1)
no2 = int(input("Enter number 2: "))
numbers.append(no2)
no3 = int(input("Enter number 3: "))
numbers.append(no3)
no4 = int(input("Enter number 4: "))
numbers.append(no4)
no5 = int(input("Enter number 5: "))
numbers.append(no5)

number = set(numbers) 

print(number.union())  #Output: #Enter number 1: 2
                                #Enter number 2: 3
                                #Enter number 3: 2
                                #Enter number 4: 5
                                #Enter number 5: 4
                                #{2, 3, 4, 5}

#Problem3
# Create a set containing the following values: 10, 10.0, "10"
# Print the set and explain the output using a comment.
s = {10, 10.0, "10"}

print(s)  #Output: {10, '10'} there is 3 datatype values in a set int, float , str. why the output not displaying the float value is becuase python understand integer and floating values as same so to print all values we can write something like value = {("int", 10),("float", 10.0)} print(value)

#Problem4
# What will be the output of the following code? (Write your answer in comments)
s = set()
s.add(5)
s.add(5.0)
s.add("5")
print(len(s))  #Output: 2 first .add will add the values in an empty set and then counts the length of set. why the output is 2 becuase python understand int and float values as same so it counts it as 1 not 2 diffrent values and the str counts as different so that's why the output is 2.

#Problem5
# Create an empty dictionary.
# Ask the user to enter names and ages of 3 people, then store them in the dictionary and print it.
dictionary = {}

name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))
dictionary.update({name1:age1})
name2 = input("Enter your name: ")
age2 = int(input("Enter your age: "))
dictionary.update({name2:age2})
name3 = input("Enter your name: ")
age3 = int(input("Enter your age: "))
dictionary.update({name3:age3})

print(dictionary)   #Output: Enter your name: simra
                           # Enter your age: 20
                           # Enter your name: saira
                           # Enter your age: 20
                           # Enter your name: muniba
                           # Enter your age: 22
                           # {'simra': 20, 'saira': 20, 'muniba': 22}

#Problem6
# If two users enter the same name as a key in a dictionary, what happens?
# Demonstrate this using a small program and explain with comments.
friends = {
    "simra": "20",
    "hamza": "22",
    "hamza": "20"
}
print(friends)   #Output: {'simra': '20', 'hamza': '20'} python skiped the same name key in a dictionary why because same keys can't be repeated in dict it'a a rule in python we can add same values in different keys but keys can't be same.

#Problem7
# Create a dictionary of 4 programming languages and their creators.
# Print: all keys, all values, all key-value pairs
languages = {
    "Python": "Guido van Rossum",
    "Javascript": "Bjarne Stroustrup",
    "C++": "Brendan Eich",
    "C#": "Anders Hejlsberg"
}
print(languages.keys())    #Output: dict_keys(['Python', 'Javascript', 'C++', 'C#'])
print(languages.values())  #Output: dict_values(['Guido van Rossum', 'Bjarne Stroustrup', 'Brendan Eich', 'Anders Hejlsberg'])
print(languages)          #Output: {'Python': 'Guido van Rossum', 'Javascript': 'Bjarne Stroustrup', 'C++': 'Brendan Eich', 'C#': 'Anders Hejlsberg'}

#Problem8
# Take 5 favorite colors from the user and store them in a set.
# Check if the color "black" exists in the set and print True or False.
colors = set()

color1 = input("Enter color 1: ")
colors.add(color1)
color2 = input("Enter color 2: ")
colors.add(color2)
color3 = input("Enter color 3: ")
colors.add(color3)
color4 = input("Enter color 4: ")
colors.add(color4)
color5 = input("Enter color 5: ")
colors.add(color5)

print("Black exists or not: ","black" in colors)   #Output: Enter color 1: red
                                                            # Enter color 2: blue
                                                            # Enter color 3: purple
                                                            # Enter color 4: black
                                                            # Enter color 5: white
                                                            # Black exists or not:  True

#Problem9
# Given a dictionary: Update Sara’s marks to 95 and print the updated dictionary.
marks = {
    "Ali": 85,
    "Sara": 90,
    "John": 78
}
marks.update({"Sara": 95})
print(marks)    #Output: {'Ali': 85, 'Sara': 95, 'John': 78}

#Problem10
# Create a set of numbers from 1 to 10.
# Remove any 3 numbers of your choice from the set and print the final set.
Numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Numbers.remove(2)
Numbers.remove(4)
Numbers.remove(6)
print(Numbers)    #Output: {1, 3, 5, 7, 8, 9, 10}

#Bonus one
# Create a dictionary where: keys = student names , values = a list of their 3 subject marks, Print the dictionary neatly.
subjects = {
    "Simra": [75, 80, 90],
    "Saira": [60, 70, 80],
    "Muniba": [70, 80, 90]
}
print(subjects)  #Output: {'Simra': [75, 80, 90], 'Saira': [60, 70, 80], 'Muniba': [70, 80, 90]}
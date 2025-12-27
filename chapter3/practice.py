# TOPIC: STRINGS
# SOURCE: Codewithharry

# Problem1
# Use input() to take name from user followed by Good Afternoon
name = input("Enter Your Name: ")
print(f"Good Afternoon {name}")   # f string is a formatted string to dynamically inserts the value of variables

# Problem2
# Replace Name and Date in the Letter
letter = '''Dear <|Name|>
You are Selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Simra").replace("<|Date|>", "10 Dec 2025"))

# Problem3
# Detect double space in the program
name = "simra is  learning"
print(name.find("  "))

# Problem4
# Replace double space with the single space
name = "simra is  learning"
print(name.replace("  ", " "))
print(name)   # strings are immutable which means that you can't change it by running functions on them 

# Problem5
# Format the following by escape sequence
letter = "Dear Simra,\n\tYour are doing well \nKeep going."
print(letter)

#Problem1
# Ask the user for their name and print: “Good Evening, <name>”
name = input("Enter your name: ")
print("Good Evening", name)

#Problem2
# Ask the user for their name and city, then print a sentence using f-string.
name = input("Enter your name: ")
city = input("Enter your city name: ")
print(f"My name is {name} and i am from {city}")

#Problem3
# Write a program to detect triple spaces in a string entered by the user.
space = input("Enter message: ")

print(space.find("   "))

#Problem4
# Replace all double spaces in a string with single spaces.
find_space = "hello  i am  simra"

print(find_space.replace("  ", " ")) 

#Problem5
# Ask the user for a sentence and print: the sentence in uppercase, the sentence in lowercase
sentence = input("Enter sentence: ")
print(sentence.upper())
print(sentence.lower())

#Problem6
# Write a program to check whether a string starts with the word "Hello".
start_with = "Hello world"
print(start_with.startswith("Hello"))

#Problem7
# Write a program to count the length of a string entered by the user.
length = input("Enter note: ")
print(len(length))

#Problem8
# Write a program to replace the word "bad" with "good" in a sentence.
change = "I am bad at programming"
print(change.replace("bad", "good"))

#Problem9
# Create a letter template and fill it using input:
# Dear <name>,
# Welcome to Python programming.
# You joined on <date>. 
Name = input("Enter name: ")
date = input("Enter date: ")

print(f"Dear {Name},\nWelcome to Python programming.\nYou joined on {date}.")

#Problem10
# Format the following sentence using escape sequences so it prints in 3 lines: Python is fun. I am learning it. I love coding.
line = "Python is fun.\nI am learning it.\nI love coding."
print(line)
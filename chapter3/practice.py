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


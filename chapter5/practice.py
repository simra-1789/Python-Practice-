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
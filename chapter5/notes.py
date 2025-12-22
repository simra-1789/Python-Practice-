# TOPIC: Dictionary And Sets  
# SOURCE: Codewithharry

d = {}    # Empty Dictionary
marks = {
    "simra": 100,
    "saira": 95,
    "muniba": 90
}

print(marks, type(marks))
print(marks["simra"])

# Dictionary Methods
mark = {
    "simra": 100,
    "saira": 95,
    "muniba": 90
}
print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"saira": 97 , "hamza": 90})
print(mark)
print(mark.get("muniba"))
print(mark.pop("simra"))
print(mark)
print(mark.popitem())
print(mark)
print(mark.get("simra2"))   # Prints None
print(mark["simra2"])       # Returns Error

# Sets
s = {1, 2, 3, 2, 2}  # Sets can't contain duplicate values 
e = set()   # Don't use s = {} as it will create an empty dictionary
print(s)

# Sets Methods
sets = {1, 2, 3, 4, 5}
sets.add(6)
print(sets, type(sets))
sets.remove(2)
print(sets)
# sets.clear() # Clear empties your set 
# pop() removes random value from the set
s1 = {1, 5, 34, 6}
s2 = {1, 5, 35, 7}  
print(s1.union(s2))   # Union gives all the values from both sets but not repeated ones
print(s1.intersection(s2))  #Intersection gives same values from both sets

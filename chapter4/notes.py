# TOPIC: LIST and TUPLE 
# SOURCE: Codewithharry

friends = ["simra", "saira", 20, 10.2, True , "muniba"]
print(friends[0])

friends[0] = "samra"   # Unlike strings lists are mutable
print(friends[0])
print(friends[1:4])

# List methods
friends.append("hamza")
print(friends)

list = [1, 4, 5, 67, 45 , 34] 
list.sort()
list.reverse()
list.insert(3,10)  #insert 10 such that it's index in the list is 3
list.pop(4)
list.remove(4)
print(list)

# Tuple 
tup = (1 , 3, "simra" , 3 , False , 12.0)  #Tuple is immutable just like string we can't change it like list
print(tup)
print(type(tup))

# Tuple methods
no = tup.count(3)
print(no)
t = tup.index(3)
print(t)
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
list.remove(5)
print(list)



# TOPIC: STRINGS
# SOURCE: Codewithharry

name = "simra"     # positive slicing or indexing [0,1,2,3,4]
      # 01234

nameshort = name[0:3]    # start from index 0 till 3 (excluding 3)
print(nameshort) 

character = name[0]    # printing character of the string by index 
print(character)


name = "simra"      # Negative Slicing or Indexing
print(name[-4:-1])
print(name[1:4])

print(name[:4])   # is same as print(name[0:4])
print(name[1:])   # is same as print(name[1:5])
print(name[1:5])
print(name[0:len(name)])   # this means we want full lenth of word

word = "amazing"   # Slicing with skip value
print(word[1:6:2])

word = "abcdefghij"
print(word[1:9:4])

# String methods
name = "Simra zafar"
print(len(name))      # len() is a function
print(name.startswith("si"))
print(name.endswith("mra"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.count("a"))
print(name.replace("zafar", "khan"))




# Escape Sequence
a = "simra is a good girl \nbut not a bad girl"
print(a)
b = "Good\tday"
print(b)
c = "python is an easy \"language\""
print(c)
d = 'I am \'20\' year old'
print(d)
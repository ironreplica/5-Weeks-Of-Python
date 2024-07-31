# Immutable Data Types 
# Trevor Childs 7/30/2024

a = 10
# Id value of object stored in memory
print(id(a))

a = 30
# Different place in memory, showing that the object is a different int object a as defined before
print(id(a))

s = 'hello'
print(id(s))

s = 'world'
print(id(s))
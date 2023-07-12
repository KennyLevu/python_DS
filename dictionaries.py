# Dictionaries
# Python dictionaries are like hashtables with key:value pairs
print("\nPython dictionaries are like hashtables with key:value pairs")
print("\nkeys must be of hashable types, which are immutable objects")
print("\nKey value pairs can be of mixed types")

# Create Dictionary
print("\n Creating Dictionary: ")
Dict = {'String':'another string', 'int key':2, 69:420, 'list':['I', 'am', 22]}
print(Dict)

# Access element by key
print("\n Accessing dictionary by list key")
print(Dict['list'])

# Access element by get
print("\n Accessing dictionary by get list")
print(Dict.get('list'))

# Dictionary comprehension
print("\n Create a dictionary of multiples of 3 using dictionary comprehension")
Dict2 = {x:x*3 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
print(Dict2)


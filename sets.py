# Sets are mutable and use hashing to execute inserts, deletes, and traversals
print("\n Sets are mutable and use hashing to execute inserts, deltes, and traversals")

# Set with mixed types
print("\n Set with mixed types")
Set = set(["hello", "world", 22, 42, "ooga booga"])
print(Set)

# Traversal of a set
print("\n Traversal of sets using a for loop")
for i in Set:
    print(i, end ="  ")
print()

# Elements with duplicate index values are appended as a linked list
print("\n Elements with dupliate index values are appended as a linked list")

#Bytearrays

#Bytearrays give a mutable sequence of ints from 0<=x<256
print("\nBytearrays give a mutable sequence of ints from 0<=x<256 ")

print("\nCreating bytearray")
a = bytearray((0,1,2,10,11))
print(a)

# accessing byte arrays
print("\nAccessing a[2]")
print(a[2])

# modifying byte arrays
print("\nModifying a[2] to 13")
a[2]=13
print(a)

# Appending bytearrays
print("\n Appending to bytearray")
a.append(30)
print(a)

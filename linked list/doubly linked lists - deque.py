from collections import deque
ll = deque()
print(ll)

## populating the ll
print('populating the ll')
ll = deque(['a','b','c'])
print(ll)

# string input | you can pass any iterable as an input 
print('string input')
ll = deque('abc')
print(ll)

# append
print('appending element')
ll.append('d')
print(ll)

# pop
print('pop an element')
ll.pop()
print(ll)

# left handed operations
print('pop left')
ll.popleft()
print(ll)

print('append left')
ll.appendleft('a')
print(ll)


from collections import deque
# stacks with deque (doubly linked list)
print('Stacks with deque (doubly linked list)\n')

history = deque()
# Using a stack to emulate browser history which is a LIFO operation
print('Using a stack to emulate browser history which is a LIFO operation\n')

# append left to add to the head of the linked list
print('Visited youtube')
history.appendleft('https://youtube.com/')
print(history)

print('\nClicked on video')
history.appendleft('https://youtube.com/cool-cats')
print(history)

print('\nAnother video')
history.appendleft('https://youtube.com/mean-cats')
print(history)

print('\nReturn to last page')
# pop left to remove the last item in the stack
history.popleft()
print(history)

print('\nGo backwards again')
history.popleft()
print(history)

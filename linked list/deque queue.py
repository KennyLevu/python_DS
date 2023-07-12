# implementing a queue using a deque (doubly linked list)
from collections import deque
queue = deque()
print(queue)

# add objects arriving to queue
# append right to add to end of linked list
queue.append('Kenny')
print('Kenny has arrived')
print(queue)
queue.append('Brandon')
print('Brandon has arrived')
print(queue)
queue.append('Andy')
print('Andy has arrived')
print(queue)

# dequeue is a FIFO operation
print('\nDequeue is a fifo operation')
queue.popleft()
print('Next person please')
print(queue)
queue.popleft()
print('Next person please')
print(queue)



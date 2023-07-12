# linked list
# Node class
class Node:
    # Function initailizing a node object
    def __init__(self, data):
        self.data = data # data assisnged to node object
        self.next = None # pointer to next node

# Linked list class
class LinkedList:
    # Function to inialize linked list object
    def __init__(self):
        self.head = None

    # Function to traverse linked list
    def printList(self):
        _temp = self.head
        while (_temp):
            print(_temp.data)
            _temp = _temp.next
if __name__=='__main__':
    # initialize ll object
    llist = LinkedList()

    # create a head node object
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # link the nodes
    llist.head.next = second;
    second.next = third

    llist.printList()

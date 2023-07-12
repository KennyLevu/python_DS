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
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # Function to traverse linked list
    def printList(self):
        _temp = self.head
        while (_temp):
            print(_temp.data)
            _temp = _temp.next

    # Text representation of linked list
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # iterator
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
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
    print(llist)

    #initalize with list
    print('initailizing with list [a,b,c,d,420]')
    llist = LinkedList(['a','b','c','d',420])
    print(llist)

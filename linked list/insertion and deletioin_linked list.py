# linked list insertion / deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

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

    print(llist)


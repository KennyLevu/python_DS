class BinaryTree:
    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.key = key

    class BinaryTree:
        def __init__(self):
            self.root = None

    def add(self, value):
        if self.key is None:
            self.key = value
        if self.key == value:
            return
        if value < self.key:
            if self.left_child:
                self.left_child.add(value)
            else:
                self.left_child = BinaryTree(value)
        else:
            if self.right_child:
                self.right_child.add(value)
            else:
                self.right_child = BinaryTree(value)

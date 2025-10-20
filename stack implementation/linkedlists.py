from node import Node


class linkedlist:
    def __init__(self, first, last):
        self.first = None
        self.last = None
        self.size = 0


    def add(self, node):
        node = Node(node)
        if self.first is None:
            self.first = node
        self.last = node
        self.size += 1

    def get(self, index):


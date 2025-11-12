from node import Node


class linkedlist:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0


    def add(self, node):
        if self.first is None:
            self.first = node
        else:
            self.last.next = node
            node.previous = self.last
        self.last = node
        self.size += 1
        print (self.size)



    def get(self, index):
        if index >= 0 and index < self.size:
            current = self.first
            if index >= self.size/2:
                for i in range(index-1, -1, -1):
                    current = current.next

            else:
                for i in range(index):
                    current = current.next

            return current
        else: return "Error: out of bounds"

    def insert(self, index, data):

        current = self.first
        for i in range(index):
            current = current.next
        x = current.next
        #x.previous =
        current.next.previous = current


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return self.data.__str__()
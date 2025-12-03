import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.edges = []
        self.distance = sys.maxsize
        # is the node in the open list?
        self.in_open_list = False
        # has the node been actively removed from the open list?
        self.removed = False


    def add_edge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return f"{self.data} ({self.distance})"

    def __lt__(self, other_node):
        return self.distance < other_node.distance

from edge import Edge
import heapq
from heapq import heappush, heappop

class Graph:
    def __init__(self):
        # dictionary of routes to different destinations
        self.routes = { }

    # Add an edge to the graph
    # Create both a forward edge (start-end) and
    # a reverse edge (end-start)
    def add_edge(self, start, end, weight):
        forward_edge = Edge(start, end, weight)
        reverse_edge = Edge(end, start, weight)
        start.add_edge(forward_edge)
        end.add_edge(reverse_edge)

    # The actual Dijkstra algorithm
    def dijkstra(self, start, end):
        open_list = []
        heappush(open_list, start)
        start.in_open_list = True
        current_node = None

        while len(open_list) > 0 and current_node != end:
            current_node = heappop(open_list)
            current_node.in_open_list = False
            current_node.removed = True
            for edge in current_node.edges:
                pass

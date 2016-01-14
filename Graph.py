class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def find_shortest_path(self, start, end):
        foo = 6

    def print_nodes(self):
        print("Printing Graph")
        for elem in self.nodes:
            print(str(elem))
class Node:

    def __init__(self):
        self.name = ""
        self.neighbors = []
        self.prev = ""
        self.is_in_queue = False

    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.prev = ""
        self.is_in_queue = False

    def setName(self, name):
        self.name = name

    def add_neighbors(self, neighbors):
        for elem in neighbors:
            self.neighbors.append(elem)

    def __str__(self):
        rtnstr = "Node: "+self.name+"\nEdges: "
        for elem in self.neighbors:
            rtnstr += elem.name+" "
        return rtnstr+"\n"

    def clear_path_data(self):
        self.prev = ""
        self.is_in_queue = False
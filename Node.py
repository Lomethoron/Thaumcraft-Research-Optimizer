class Node:

    def __init__(self):
        self.name = ""
        self.neighbors = []

    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def setName(self, name):
        self.name = name

    def add_neighbors(self, neighbors):
        for elem in neighbors:
            self.neighbors.append(elem)

    def __str__(self):
        rtnstr = "Node: "+self.name+"Edges: "
        for elem in self.neighbors:
            rtnstr += elem.name+" "
        return rtnstr+"\n"
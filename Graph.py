from collections import deque
from Node import Node
class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def find_shortest_path(self, start_name, end_name):
        nodes_to_visit = deque()
        #identify start
        start = Node("foo")
        end = Node("foo")
        break_to_end = 2
        for elem in self.nodes:
            if elem.name == start_name:
                start = elem
                break_to_end -= 1
            if elem.name == end_name:
                end = elem
                break_to_end -= 1
            if break_to_end == 0:
                break

        for elem in start.neighbors:
            elem.prev = start
            elem.is_in_queue = True
            start.is_in_queue = True
            nodes_to_visit.append(elem)

        while (len(nodes_to_visit)-1)>0:
            curr_node = nodes_to_visit.popleft()
            # print("Current Node is: "+ curr_node.name)
            if curr_node.name == end_name:
                while curr_node.name != start_name:
                    # print("Name: "+curr_node.name)
                    # print("Prev: "+curr_node.prev.name)
                    print curr_node.name
                    curr_node = curr_node.prev
                print start_name
                for elem in self.nodes:
                    elem.clear_path_data()
                break
            for elem in curr_node.neighbors:
                #make sure element is not in queue
                # print "Looking at element: "
                # print elem
                if elem.is_in_queue:
                    # print("Skipping Element: "+elem.name)
                    continue
                elem.prev = curr_node
                elem.is_in_queue = True
                nodes_to_visit.append(elem)
                # print("Adding "+elem.name+" to queue. Prev is: "+elem.prev.name)



    def print_nodes(self):
        print("Printing Graph")
        for elem in self.nodes:
            print(str(elem))
from Graph import Graph
from Node import Node

thaum_data = open('research.thaum')
counter = 0
primal_amount = int(thaum_data.readline())
print "Creating Primal Instances"
print primal_amount
graph = Graph()
while counter<primal_amount:
    #create Nodes
    elementName = thaum_data.readline()
    element = Node(elementName)
    graph.addNode(element)
    counter += 1

print(graph.print_nodes())

#create secondary aspects
counter = 0
constructed_amount = int(thaum_data.readline())
print "Creating Constructed Instances"
while counter<constructed_amount:
    #create nodes
    foo = thaum_data.readline()
    counter += 1
thaum_data.close()
print "Closing file"
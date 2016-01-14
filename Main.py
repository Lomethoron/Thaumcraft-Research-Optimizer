from Graph import Graph
from Node import Node

thaum_data = open('research.thaum')
counter = 0
primal_amount = int(thaum_data.readline())
print "Creating Primal Instances"
graph = Graph()
while counter<primal_amount:
    #create Nodes
    element_name = thaum_data.readline()
    element = Node(element_name.strip())
    graph.add_node(element)
    counter += 1

#create secondary aspects
counter = 0
constructed_amount = int(thaum_data.readline())
print "Creating Constructed Instances"
while counter<constructed_amount:
    #create nodes
    element_data = thaum_data.readline().strip().split(" ")
    element = Node(element_data[0])
    graph.add_node(element)
    element_builder_name_1 = element_data[1]
    element_builder_name_2 = element_data[2]

    #first node
    does_elem_1_exist = False
    for elem in graph.nodes:
        print("Elem name: "+elem.name)
        print("Elem1 name: "+element_builder_name_1)
        print("is equal:"+str(elem.name == element_builder_name_1)+"\n")
        if(elem.name == element_builder_name_1):
            does_elem_1_exist = True
            elem.add_neighbors([element])
            element.add_neighbors([elem])
    if(not does_elem_1_exist):
        element_1 = Node(element_builder_name_1)
        element_1.add_neighbors([element])
        element.add_neighbors([element_1])
        graph.add_node(element_1)

    #second node
    does_elem_2_exist = False
    for elem in graph.nodes:
        print("Elem name: "+elem.name)
        print("Elem1 name: "+element_builder_name_2)
        print("is equal:"+str(elem.name == element_builder_name_2)+"\n")
        if(elem.name == element_builder_name_2):
            does_elem_2_exist = True
            elem.add_neighbors([element])
            element.add_neighbors([elem])
    if(not does_elem_2_exist):
        element_2 = Node(element_builder_name_2)
        element_2.add_neighbors([element])
        element.add_neighbors([element_2])
        graph.add_node(element_2)
    counter += 1
thaum_data.close()
print "Closing file"
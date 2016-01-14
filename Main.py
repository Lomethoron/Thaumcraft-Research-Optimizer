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
# print counter
# print primal_amount
#create secondary aspects
counter = 0
constructed_amount = int(thaum_data.readline())
print "Creating Constructed Instances"
while counter<constructed_amount:
    #create nodes
    element_data = thaum_data.readline().strip().split(" ")
    does_elem_exist = False
    element_name = element_data[0]
    element_builder_name_1 = element_data[1]
    element_builder_name_2 = element_data[2]
    # print("Current line is: "+ element_name)
    for elem in graph.nodes:
        if elem.name == element_name:
            does_elem_exist = True
            element_1 = Node(element_builder_name_1)
            element_2 = Node(element_builder_name_2)
            elem.add_neighbors([element_1, element_2])
            element = elem
    if not does_elem_exist:
        element = Node(element_name)
        graph.add_node(element)
    element_builder_name_1 = element_data[1]
    element_builder_name_2 = element_data[2]

    #first node
    does_elem_1_exist = False
    for elem in graph.nodes:
        if(elem.name == element_builder_name_1):
            # print("Elem name: "+elem.name)
            # print("Elem1 name: "+element_builder_name_1)
            # print("Adding "+ elem.name+" to "+element.name)
            # print("Adding "+ element.name+" to "+elem.name)
            # print("Element already exists"+"\n")
            does_elem_1_exist = True
            elem.add_neighbors([element])
            element.add_neighbors([elem])
    if(not does_elem_1_exist):
        # print("Elem1 name: "+element_builder_name_1)
        # print("Adding "+ element_builder_name_1+" to "+element.name)
        # print("Adding "+ element.name+" to "+element_builder_name_1)
        # print("Element does not already exist"+"\n")
        element_1 = Node(element_builder_name_1)
        element_1.add_neighbors([element])
        element.add_neighbors([element_1])
        graph.add_node(element_1)

    #second node
    does_elem_2_exist = False
    for elem in graph.nodes:
        if(elem.name == element_builder_name_2):
            # print("Elem name: "+elem.name)
            # print("Elem1 name: "+element_builder_name_2)
            # print("Adding "+ elem.name+" to "+element.name)
            # print("Adding "+ element.name+" to "+elem.name)
            # print("Element already exists"+"\n")
            does_elem_2_exist = True
            elem.add_neighbors([element])
            element.add_neighbors([elem])
    if(not does_elem_2_exist):
        # print("Elem1 name: "+element_builder_name_2)
        # print("Adding "+ element_builder_name_2+" to "+element.name)
        # print("Adding "+ element.name+" to "+element_builder_name_2)
        # print("Element does not already exist"+"\n")
        element_2 = Node(element_builder_name_2)
        element_2.add_neighbors([element])
        element.add_neighbors([element_2])
        graph.add_node(element_2)
    counter += 1
# print(counter)
# print constructed_amount
# print graph.print_nodes()
thaum_data.close()
print "Closing file"
while(True):
    print("Enter aspects or \"quit\" to exit the program")
    input1 = raw_input("Aspect 1: ")
    if input1 in ("exit", "e", "q", "quit"):
        break
    input2 = raw_input("Aspect 2: ")
    if input2 in ("exit", "e", "q", "quit"):
        break
    graph.find_shortest_path(input1, input2)
print("Exiting Program")
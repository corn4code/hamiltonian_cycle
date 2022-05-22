from itertools import permutations
from graph import * # --> graph needs to be a class from this
    
def valid_connection(graph,node1,node2):
    """checks if the connection between two nodes is existing/valid"""
    if node2 in graph.edges(node1):
        return True
    else:
        return False

def get_permutations(liste):
    """creates a list of lists for all permutations based on the given list"""
    all_per = []
    for x in permutations(liste):
        all_per.append(list(x))
    return all_per

def ham_c_final(graph,start_v=None):
    """finds all hamiltonian cycles for a given graph from the given starting node"""
    vortexes = list(graph.all_vertices()) # creates list of all nodes
    for nodes in vortexes:
        if len(graph.edges(nodes))<2: # if any node has less than two edges, no ham. cycle is possible --> stops 
            return "There is no hamiltonian cycle for this graph"
    if start_v == None: # sets starting node as first in vortexes, if it wasn't given yet 
        start_v = vortexes[0]
    vortexes.remove(start_v) # starting node gets removed, so that it won't be affected / shuffeled by permutations
    possibilitys = get_permutations(vortexes)
    valid = True
    ham_cycles = []
    for liste in possibilitys: # adds starting node to start and end of list
        liste.append(start_v)
        liste.insert(0,start_v)
    
    for possibility in possibilitys: # goes through all permutations and checks for each neighbored nodes, if they are connected
        for nodes in possibility:
            if valid_connection(graph,nodes,possibility[possibility.index(nodes)+1]) == False:
                valid = False
                break
            else:
                valid = True
        if valid: # if all nodes in the checked permutation were connected, the permutation is a hamiltonian cycle and therefore it will be added to the list of all ham. cycles 
            ham_cycles.append(possibility) 
    return ham_cycles if len(ham_cycles)>0 else "There is no hamiltonian cycle for this graph"


test = Graph()
test.add_vertex("0")
test.add_vertex("1")
test.add_vertex("2")
test.add_vertex("3")
test.add_vertex("4")
test.add_vertex("5")
test.add_vertex("6")
test.add_vertex("7")
test.add_edge(("0","1"))
test.add_edge(("1","2"))
test.add_edge(("2","0"))
test.add_edge(("0","4"))
test.add_edge(("1","5"))
test.add_edge(("0","5"))
test.add_edge(("2","3"))
test.add_edge(("2","4"))
test.add_edge(("6","1"))
test.add_edge(("6","5"))
test.add_edge(("3","0"))
test.add_edge(("3","4"))
test.add_edge(("7","0"))
test.add_edge(("7","1"))
test.add_edge(("7","4"))

print(ham_c_final(test,"0"))

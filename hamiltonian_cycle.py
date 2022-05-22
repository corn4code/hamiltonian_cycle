from itertools import permutations
from tracemalloc import start
from graph import *
    
def valid_connection(graph,node1,node2):
    if node2 in graph.edges(node1):
        return True
    else:
        return False

def get_permutations(liste):
    all_per = []
    for x in permutations(liste):
        all_per.append(list(x))
    return all_per

def ham_c_final(graph,start_v):
    vortexes = list(graph.all_vertices())
    vortexes.remove(start_v)
    possibilitys = get_permutations(vortexes)
    valid = True
    ham_cycles = []
    for liste in possibilitys:
        liste.append(start_v)
        liste.insert(0,start_v)
    
    for possibility in possibilitys:
        for nodes in possibility:
            if valid_connection(graph,nodes,possibility[possibility.index(nodes)+1]) == False:
                valid = False
                break
            else:
                valid = True
        if valid:
            ham_cycles.append(possibility)
    return ham_cycles


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

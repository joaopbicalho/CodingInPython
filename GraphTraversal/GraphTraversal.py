import numpy as np

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False


def connect(node1, node2, weight):
    node1.connections.append({"node": node2, "weight": weight})
    node2.connections.append({"node": node1, "weight": weight})


def BFS(node):
    q = [node]
    node.visited = True
    while len(q) > 0:
        cur = q.pop(0) # remove q[0] from q and put it in cur
        print(cur.name)
        for con in cur.connections:
            if not con["node"].visited:
                q.append(con["node"])
                con["node"].visited = True



def get_all_nodes(node):
    x = []
    q = [node]
    node.visited = True
    while len(q) > 0:
        cur = q.pop(0)

        x.append(cur)
        for con in cur.connections:
            if not con["node"].visited:
                q.append(con["node"])
                con["node"].visited = True
    return x




def unvisit_all(node):
    '''Change all n.visited to False in all the nodes in the graph of nodes
    connected to node. Use BFS to find all the nodes'''
    q = [node]
    node.visited = False
    while len(q) > 0:
        cur = q.pop(0) # remove q[0] from q and put it in cur
        for con in cur.connections:
            if con["node"].visited:
                q.append(con["node"])
                con["node"].visited = False



# def DFS_rec(node):
#     '''Print out the names of all nodes connected to node using a
#     recursive version of DFS'''
#     if not node.visited:
#         print (node.name)
#         node.visited = True
#         for neighbour in node.connections:
#             DFS_rec(neighbour["node"])

def DFS_rec(node):
    '''Print out the names of all nodes connected to node using a
    recursive version of DFS'''
    print (node.name)
    node.visited = True
    reversed_connections = reversed(node.connections)
    for con in reversed_connections:
        cur = con["node"]
        if not cur.visited:
            DFS_rec(cur)

################################################################################

def DFS_nonrec(node):
    '''Print out the names of all nodes connected to node using a non-recursive
    version of DFS. Make it so that the nodes are printed in the same order
    as in DFS_rec'''

    s = [node]
    node.visited = True
    while len(s) > 0:
        cur = s.pop() # remove s[-1] from stack and put it in cur
        print(cur.name)
        for con in cur.connections:
            if not con["node"].visited:
                s.append(con["node"])
                con["node"].visited = True


################################################################################



if __name__ == '__main__':
    TO = Node("TO")
    NYC = Node("NYC")
    DC = Node("DC")
    CDMX = Node("CDMX")
    SF = Node("SF")

    connect(TO, NYC, 3)
    connect(TO, SF, 6)
    connect(TO, CDMX, 7)
    connect(NYC, DC, 2)
    connect(SF, DC, 5)

    BFS(TO)
    L = get_all_nodes(TO)
    DFS(TO)
    #DFS_rec(TO)
    unvisit_all(TO)
    DFS(TO)

    # print("\nget_all_nodes\n")
    # L = get_all_nodes(TO)
    # for node in L:
    #     print(node.name, node.visited)

    print("\nDFS_nonrec\n")
    DFS_nonrec(TO)
    print("\nDFS_rec\n")
    unvisit_all(TO)
    DFS_rec(TO)
    print("\nunvisited all\n")
    unvisit_all(TO)
    # for node in L:
    #     print(node.name, node.visited)
    # # DFS(TO)

import random

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        node.insert(5) is the same as BST.insert(node, 5)
        We use this when recursively calling, e.g. self.left.insert
        '''
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def __repr__(self):
        '''The string representation of a node.
        Here, we convert the value of the node to a string and make that
        the representation.
        We can now use
        a = Node(4)
        print(a) # prints 4
        '''
        return str(self.value)

    def height(self):


        if self.right == None and self.left == None:
            return 1
        if self.right == None:
            return self.left.height() + 1
        if self.left == None:
            return self.right.height() + 1
        u = self.left.height() +1
        v = self.right.height() +1
        return (u if u > v else v )

    def BFS_tree(node):
        L = []
        L.append(node)
        h = node.height()
        for i in range(h):
            L2 = []
            for elem in L:
                print(elem.__repr__())
                if(elem.left != None):
                    L2.append(elem.left)
                if(elem.right != None):
                    L2.append(elem.right)
            L = L2

a = BST(4)
a.insert(2)
a.insert(5)
a.insert(10)
a.insert(3)
a.insert(15)
a.insert(20)

def make_random_tree(n_nodes):
    '''Make a tree with n_nodes nodes by inserting nodes with values
    drawn using random.random()
    '''
    tree = BST(random.random())
    for i in range (n_nodes - 1):
        tree.insert(random.random())
    return tree

def height_random_tree(n_nodes):
    '''Generate a random tree with n_nodes nodes, and return its height'''
    tree = make_random_tree(n_nodes)
    height = tree.height()
    return height

def make_data(max_nodes):
    '''Make two lists representing the empirical relationship between
    the number of nodes in a random tree and the height of the tree.
    Generate N_TREES = 40 trees with each of
    n_nodes = 5, int(1.2*5), int(1.2^2*5), .....

    return n (a list of values of n_nodes) and h (a list of heights)

    '''

    n = []
    h = []
    N_TREES = 40
    n_nodes = 5
    for i in range(N_TREES):
        h.append(height_random_tree(n_nodes))
        n.append(n_nodes)
        n_nodes = int(5*1.2**i)

    return n, h

n, h = make_data(10000)
import matplotlib.pyplot as plt
plt.scatter(n, h)
plt.show()
#plt.savefig("trees.png") can save the data to disk


class Graph:

    def __init__(self):
        self.edge = []
        self.node = []

    def Add_Edge(self, edge):
        self.edge.append(edge)

    def Add_Node(self, node):
        self.node.append(node)

    def Get_Node(self):
        return self.node


class Region:

    def __init__(self,x_low, x_up, y_low, y_up):
        Region.x_low = x_low
        Region.x_up = x_up
        Region.y_low = y_low
        Region.y_up = y_up


class Point:

    def __init__(self, x, y):
        self.X = [x, y]
        self.g = 0
        self.lmc = 0
        self.parent = -1

    def xy(self):
        return self.X

    def Add_g(self, g):
        self.g = g

    def Add_lmc(self, lmc):
        self.lmc = lmc

    def Add_parent(self, parent):
        self.parent = parent
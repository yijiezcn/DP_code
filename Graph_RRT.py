
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


    def xy(self):
        return self.X
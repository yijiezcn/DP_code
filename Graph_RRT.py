class Graph:

    def __init__(self):
        self._edge = []
        self._node = []

    def Delete_Edge(self):
        self._edge = []

    def Add_Edge(self, edge):
        self._edge.append(edge)

    def Add_Node(self, node):
        self._node.append(node)

    def Get_Nodes(self):
        return self._node

    def Get_Edges(self):
        return self._edge

    def succ(self, x):
        succ = []
        for edge in self._edge:
            if edge[0] == x:
                succ.append(edge[1])
        return succ

    def pred(self, x):
        pred = []
        for edge in self._edge:
            if edge[1] == x:
                pred.append(edge[0])
        return pred


class Region:

    def __init__(self, x_low, x_up, y_low, y_up):
        self.x_low = x_low
        self.x_up = x_up
        self.y_low = y_low
        self.y_up = y_up


class Point:

    def __init__(self, x, y, g=float('inf'), lmc=float('inf'), parent=-1):
        self._X = [x, y]
        self._g = g
        self._lmc = lmc
        self._parent = parent

    def xy(self):
        return self._X

    def g(self):
        return self._g

    def lmc(self):
        return self._lmc

    def parent(self):
        return self._parent

    def Add_g(self, g):
        self._g = g

    def Add_lmc(self, lmc):
        self._lmc = lmc

    def Add_parent(self, parent):
        self._parent = parent



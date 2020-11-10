
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


class Region:

    def __init__(self,x_low, x_up, y_low, y_up):
        Region.x_low = x_low
        Region.x_up = x_up
        Region.y_low = y_low
        Region.y_up = y_up


class Point:

    def __init__(self, x, y, g=float('inf'), lmc=float('inf'), parent=float('inf')):
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


class Queue():

    def __init__(self):
        self.list = []

    def insert(self, x, key):
        if self.serach(x):
            print("We already have one")
            return False
        q = [x, key]
        self.list.append(q)

    def serach(self,x):
        for q in self.list:
            if q[0] == x:
                return True
        else:
            return False

    def update(self, x, key):
        for q in self.list:
            if q[0] == x:
                q[1] = key
                return True
        return False

    def delete(self, x):
        for index, q  in enumerate(self.list):
            if q[0] == x:
                self.list.pop(index)
                return True
        return False


    def Get_key(self, x):
        for q in self.list:
            if q[0] == x:
                return q
            return None
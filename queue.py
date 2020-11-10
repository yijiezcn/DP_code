import RRT_Function as RF

class Queue():

    def __init__(self):
        self.list = []

    def Que(self):
        return self.list

    def insert(self, x, key):
        if self.search(x):
            print("We already have one")
            return False
        q = [x, key]
        self.list.append(q)

    def search(self, x):
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

    def findmin(self):
        if len(self.list) == 0:
            return None, None
        min = self.list[0]
        for q in self.list:
            if Key_LQ(q[1], min[1]):
                min = q
        return min[0], min[1]


def h(P, goal_region):
    x_goal = (goal_region.x_low + goal_region.x_up)/2
    y_goal = (goal_region.y_low + goal_region.y_up)/2
    goal = [x_goal, y_goal]
    h = RF.Distance_Points(P.xy(), goal)
    return h


def Key(P, goal_region):
    k = [P.lmc() + h(P, goal_region), P.lmc()]
    return k


def Key_LQ(key1, key2):
    if key1 == None:
        return False
    if key1[0] < key2[0] or (key1[0] == key2[0] and key1[1] < key2[1]):
        return True
    else:
        return False


def Update_Queue(x, queue, points, goal):
    point = points[x]
    if point.g() != point.lmc() and queue.search(x):
        queue.update(x, Key(point, goal))
    elif point.g() != point.lmc() and not queue.search(x):
        queue.insert(x, Key(point, goal))
    elif point.g() == point.lmc() and queue.search(x):
        queue.delete(x)


def Replan(queue, G, points, goal):
    x_min, key_min = queue.findmin()
    nodes = G.Get_Nodes()
    key_goal = [float('inf'), float('inf')]
    flag = 0
    print(nodes)
    for node in nodes:
        if RF.Region_Check(goal, points[node].xy()):
            flag = 1
            key_g = [points[node].lmc(), points[node].lmc()]
            if Key_LQ(key_g, key_goal):
                key_goal = key_g
                print(key_goal)
    if flag == 0:
        key_goal = [0, 0]
    while Key_LQ(key_min, key_goal):
        points[x_min].Add_g(points[x_min].lmc())
        # print(points[x_min].g())
        queue.delete(x_min)
        succ = G.succ(x_min)
        print("Succ", succ)
        for next_node in succ:
            if points[next_node].lmc() > \
                points[x_min].g() + RF.Distance_Points(points[next_node].xy(),points[next_node].xy()):
                points[next_node].Add_lmc \
                (points[x_min].g() + RF.Distance_Points(points[next_node].xy(), points[next_node].xy()))
                points[next_node].Add_parent(x_min)
                Update_Queue(next_node, queue,points, goal)
        x_min, key_min = queue.findmin()


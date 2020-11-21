from Graph_RRT import *
import random
import numpy as np
from Constant import *
from animation import Animation
import sys

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


def Sample_Region(region):
    """Generate a random sample given a region 

    Args:
        region (class): Contains the position info of the region

    Returns:
        list: Coordinates of the generated point
    """
    x = random.uniform(region.x_low, region.x_up)
    y = random.uniform(region.y_low, region.y_up)
    # if x < 20 and y > 80: # TODO just to check spaning problem
    #     print('a point')
    X = [x, y]
    return X


def Distance_Points(X1, X2):
    """Evaluate l2 norm between two points 

    Args:
        X1 (list): Coordinates of the first point 
        X2 (list): Coordinates of the second point 

    Returns:
        float: the l2 distance
    """
    A = np.square(X1[0] - X2[0]) + np.square(X1[1] - X2[1])
    D = np.sqrt(A)
    return D


def Nearest(G, points, point_random):
    """[summary]

    Args:
        G ([type]): [description]
        points ([type]): [description]
        point_random ([type]): [description]

    Returns:
        [type]: [description]
    """
    nodes = G.Get_Nodes()
    D = 10000000
    x_nearest = -1
    for node in nodes:
        if Distance_Points(points[node].xy(), point_random) < D:
            D = Distance_Points(points[node].xy(), point_random)
            x_nearest = node
    return x_nearest


def Steer(x_nearest, point_random, points):
    x_n = points[x_nearest].xy()
    x_delta = np.array(point_random[0] - x_n[0]) 
    y_delta = np.array(point_random[1] - x_n[1])
    xy = np.sqrt(np.square(x_delta)+np.square(y_delta))
    if xy < min_edge:
        points.append(Point(point_random[0], point_random[1]))
    else:
        x_new_x = x_n[0] + min_edge*x_delta/xy # 
        x_new_y = x_n[1] + min_edge*y_delta/xy
        points.append(Point(x_new_x, x_new_y))                                       
    x_new = len(points) - 1                
    return x_new

# def Steer(x_nearest, point_random, points): #TODO previous steer
#     x_n = points[x_nearest].xy()
#     x_delta = np.abs(x_n[0]-point_random[0]) # TODO should we use abs?
#     y_delta = np.abs(x_n[1]-point_random[1])
#     xy = np.sqrt(np.square(x_delta)+np.square(y_delta))
#     x_new_x = x_n[0] + min_edge*y_delta/xy # TODO x,y in wrong position
#     x_new_y = x_n[1] + min_edge*x_delta/xy
#     points.append(Point(x_new_x, x_new_y))                                       
#     x_new = len(points) - 1                
#     return x_new


def Near(G, x_new, points):
    nodes = G.Get_Nodes()
    near_nodes = []
    for node in nodes:
        if Distance_Points(points[node].xy(), points[x_new].xy()) <= Near_r(len(nodes)+100):
            near_nodes.append(node)
    return near_nodes

def Near_r(n):
    gamma = 20000
    kesai_d = math.pi
    lamda = 5
    const_1 = math.sqrt((gamma/kesai_d) * (math.log(n)/n))
    # print('math.log(%i)/%i=%i'%(n,n,math.log(n)/n))
    # print('const_1=',const_1)
    const_2 = lamda
    return min(const_1, const_2)

def Initialize(x_1, x_2, points, goal):
    p1 = points[x_1]
    p2 = points[x_2]
    if Region_Check(goal, p1.xy()) and Region_Check(goal, p2.xy()): 
        p1.Add_g(float('inf'))
        p1.Add_lmc(p2.g() + Distance_Points(p1.xy(), p2.xy()))
        return
    p1.Add_g(float('inf'))
    p1.Add_lmc(p2.g()+Distance_Points(p1.xy(), p2.xy()))
    p1.Add_parent(x_2)


def Extend(G, Obstacles, points, point_random, queue, goal, R):
    x_nearest = Nearest(G, points, point_random)
    # print("x_nearest is", x_nearest, points[x_nearest].xy())
    x_new = Steer(x_nearest, point_random, points) 
    if not Region_Check(R, points[x_new].xy()):
        return False
    # if Region_Check(goal, points[x_new].xy()):
    #     print("Yes")
    # print("x_new is",x_new, points[x_new].xy())
    if Obstacles_Free(Obstacles, points[x_nearest].xy(), points[x_new].xy()):
        Initialize(x_new, x_nearest, points, goal)
        # print("lmc of x_new is", points[x_new].lmc())
        near_nodes = Near(G, x_new, points) 
        # print(near_nodes)
        # print("Now have points", len(points))
        # print("_________________________")
        for node in near_nodes:
            if Obstacles_Free(Obstacles, points[node].xy(), points[x_new].xy()):
                if points[x_new].lmc() > points[node].g() + Distance_Points(points[node].xy(), points[x_new].xy()):
                    points[x_new].Add_lmc(points[node].g() + Distance_Points(points[node].xy(), points[x_new].xy()))
                    if not Region_Check(goal, points[node].xy()) or not Region_Check(goal, points[x_new].xy()): 
                        points[x_new].Add_parent(node)
                G.Add_Edge([node, x_new])
                G.Add_Edge([x_new, node])
        G.Add_Node(x_new)
        Update_Queue(x_new, queue, points, goal)

        return True
    return False

def Obstacles_Free(Obstacles, X1, X2):
    sum = 0
    for Obstacle in Obstacles:
        if Obstacle_Free(Obstacle, X1, X2):
            sum = sum + 1
    if sum == len(Obstacles):
        return True
    else:
        return False

def Obstacle_Free(Obstacle, X1, X2):
    if ( X1[0] >= Obstacle.x_low and  X1[0] <= Obstacle.x_up and X1[1] >= Obstacle.y_low and X1[1] <= Obstacle.y_up ) \
        or ( X2[0] >= Obstacle.x_low and  X2[0] <= Obstacle.x_up and X2[1] >= Obstacle.y_low and X2[1] <= Obstacle.y_up ):
        return False
    else:
        p1 = [Obstacle.x_low, Obstacle.y_low]
        p2 = [Obstacle.x_up, Obstacle.y_up]
        p3 = [Obstacle.x_up, Obstacle.y_low]
        p4 = [Obstacle.x_low, Obstacle.y_up]
    if segment(X1, X2, p1, p2) or segment(X1, X2, p3, p4):
        return False
    else:
        return True

def segment(p1, p2, p3, p4):
    if (max(p1[0], p2[0]) >= min(p3[0], p4[0])
            and max(p3[0], p4[0]) >= min(p1[0], p2[0])
            and max(p1[1], p2[1]) >= min(p3[1], p4[1])
            and max(p3[1], p4[1]) >= min(p1[1], p2[1])):
        if (cross(p1, p2, p3) * cross(p1, p2, p4) <= 0
                and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0):
            D = 1
        else:
            D = 0
    else:
        D = 0
    return D

def cross(p1,p2,p3):
    x1=p2[0]-p1[0]
    y1=p2[1]-p1[1]
    x2=p3[0]-p1[0]
    y2=p3[1]-p1[1]
    return x1*y2-x2*y1

def Region_Check(region, point):
    if point[0] >= region.x_low and point[0] <= region.x_up and point[1] >= region.y_low and point[1] <= region.y_up:
        return True
    return False

def RRT_Body(R_info,obs_info,goal_info,P_init_info,N_iteration=2000,PLOT_INTERVAL=500):
    """Main body of RRT#

    Args:
        R_info (list): Shape=(1,4). Center based coordinates of the region.
        obs_info (list): Shape=(n_obs,4). Each row is the center based coordinates of the obstacles.
        goal_info (list): Shape=(1,4). Center based coordinates of the goal.
        P_init_info ([list]): Shape=(1,2). Coordinates of the initial point.
        N_iteration (int): Number of iteration.

    Returns:
        [type]: [description]
    """

    G_container = [] # TODO
    points_container = []
    opt_node_list_container = []
    min_lmc_container = []

    # working domain
    R_info = coor_converter(R_info)
    R = Region(R_info[0], R_info[1], R_info[2], R_info[3])

    # obstacle
    # o1 = Region(50, 60, 50, 60)
    obs_info = coor_converter(obs_info)
    obstacles = []
    for obs_ind in range(obs_info.shape[0]):
        single_obs_info = obs_info[obs_ind]
        obstacles.append(Region(single_obs_info[0],single_obs_info[1],single_obs_info[2],single_obs_info[3]))
    # o1 = Region(10, 20, 10, 20)
    # o2 = Region(60,70,30,50)
    # obstacles = [o1,o2]
    # obstacles = [o1]

    # goal
    goal_info = coor_converter(goal_info)
    goal = Region(goal_info[0],goal_info[1],goal_info[2],goal_info[3])
    # goal = Region(90, 100, 90, 100)

    # graph
    G = Graph()

    # initial point
    G.Add_Node(0)
    P0 = Point(P_init_info[0], P_init_info[1], 0, 0) # TODO right way to initilize?
    points = [P0]

    q = Queue()

    goal_set = []

    for i in range(N_iteration): 
        flag = False
        while not flag:
            point_rand = Sample_Region(R)
            flag = Extend(G, obstacles, points, point_rand, q, goal, R)
        x_new = len(points) - 1 

        if Region_Check(goal, points[x_new].xy()): 
            goal_set.append(x_new)
        print(points[x_new].xy())

        # if i > 2:
        #     print("LMC is", points[2].lmc())

        Replan(q, G, points, goal)

        # if i > 2:
        #     print("LMC is", points[2].lmc())
        print(i)
        print("_________________________")
        if (i+1)%PLOT_INTERVAL == 0 and (i+1)!=0:
            if goal_set == []: # TODO just delete to see if now the tree spans the whole space
                print("Haven't get any sample in goal region, increase iteration number")
                sys.exit()
            G_temp = Graph()
            egdes = G.Get_Edges()
            nodes = G.Get_Nodes()
            for edge in egdes:
                G_temp.Add_Edge(edge)
            for node in nodes:
                G_temp.Add_Node(node)
            
            G_temp.Delete_Edge()

            nodes = G_temp.Get_Nodes()

            for node in nodes:
                if points[node].parent() != -1:
                    G_temp.Add_Edge([points[node].parent(), node])

            print("Edges in the returned tree:",G_temp.Get_Edges())
            print("Goal_set:",goal_set)
    

            min_lmc = float('inf')
            min_index = 0
            for g in goal_set:
                if points[g].lmc() < min_lmc:
                    min_lmc = points[g].lmc()
                    min_index = g
                # print("Point ", g, " lmc is ", points[g].lmc())

            path_index = min_index
            opt_node_list = []
            while path_index != -1:
                print("Path: ",path_index, points[path_index].xy(),"; Lmc is", points[path_index].lmc())
                opt_node_list.append(path_index)
                path_index = points[path_index].parent()
                if path_index in opt_node_list:
                    return None, None, None, None
            points_temp = points.copy()
            opt_node_list_temp = opt_node_list.copy()
            G_container.append(G_temp)
            points_container.append(points_temp)
            opt_node_list_container.append(opt_node_list_temp)
            min_lmc_container.append(min_lmc)
    return G_container, points_container, opt_node_list_container,min_lmc_container

def h(P, goal_region):
    x_goal = (goal_region.x_low + goal_region.x_up)/2
    y_goal = (goal_region.y_low + goal_region.y_up)/2
    goal = [x_goal, y_goal]
    h = Distance_Points(P.xy(), goal)
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
    # print(nodes)
    for node in nodes:
        if Region_Check(goal, points[node].xy()):
            flag = 1
            key_g = [points[node].lmc(), points[node].lmc()]
            if Key_LQ(key_g, key_goal):
                key_goal = key_g
                # print(key_goal)
    if flag == 0:
        key_goal = [0, 0]
    while Key_LQ(key_min, key_goal):
        points[x_min].Add_g(points[x_min].lmc())
        # print(points[x_min].g())
        queue.delete(x_min)
        succ = G.succ(x_min)
        # print("Succ", succ)
        for next_node in succ:
            if points[next_node].lmc() > \
                points[x_min].g() + Distance_Points(points[next_node].xy(),points[next_node].xy()):
                points[next_node].Add_lmc \
                (points[x_min].g() + Distance_Points(points[x_min].xy(), points[next_node].xy()))
                points[next_node].Add_parent(x_min)
                Update_Queue(next_node, queue,points, goal)
        x_min, key_min = queue.findmin()

def coor_converter(coor):
    """Convert coordinates from center based to boundary based

    Args:
        coor (list/array): shape=(n_quad,4). Each row represents a quad.
                           First two coordinates are center, last two are width, height.

    Returns:
        list/array: shape=(n_quad,4). Each row represents a quad.
                    Coordinates in boundary form. First two are x limits, last two are y limits.
    """
    coor = np.array(coor)
    new_coor = np.zeros(shape=(coor.shape))
    if coor.ndim == 1:
        new_coor[0] = coor[0] - coor[2]/2
        new_coor[1] = coor[0] + coor[2]/2
        new_coor[2] = coor[1] - coor[3]/2
        new_coor[3] = coor[1] + coor[3]/2
    elif coor.ndim == 2:
        for row in range(coor.shape[0]):
            new_coor[row,0] = coor[row,0] - coor[row,2]/2
            new_coor[row,1] = coor[row,0] + coor[row,2]/2
            new_coor[row,2] = coor[row,1] - coor[row,3]/2
            new_coor[row,3] = coor[row,1] + coor[row,3]/2
    else:
        print("Wrong dimention, should be 1 or 2")
        sys.exit()
    return new_coor

def main():
    RRT_Body()

if __name__ == '__main__':

    # new_coor = coor_converter([[50,50,20,20],[50,50,20,20]])
    # new_coor = coor_converter([50,50,30,20])
    # print(new_coor)

    region_info = [50,50,100,100]
    P_init_info = [50,50]
    goal_info   = [50,90,20,20]
    obs_info    = [[15,15,10,10],[65,30,10,20],[40,60,40,10],[90,70,10,30],[70,70,10,10]]

    for test_num in range(50):
        G_container, points_container, opt_node_list_container, min_lmc_container =\
             RRT_Body(region_info,obs_info,goal_info,P_init_info)
        if G_container == None:
            continue
        for plot_ind in range(len(points_container)):
            print('------------------------------')
            print("%ith plot"%plot_ind)
            print('opt_node_list=',opt_node_list_container[plot_ind])
            plot = Animation(region_info,[P_init_info[0],P_init_info[1],3,3],goal_info,obs_info)
            nodes_coor = []
            for node_inx in range(len(G_container[plot_ind]._node)):
                node = G_container[plot_ind]._node[node_inx]
                nodes_coor.append(points_container[plot_ind][node]._X)
            plot.draw_multi_nodes(nodes_coor,color='#008000')

            total_edge_count = 0 # TODO just to see tree expansion
            for edge_ind in G_container[plot_ind]._edge:
                edge = [points_container[plot_ind][edge_ind[0]].xy()[0],points_container[plot_ind][edge_ind[0]].xy()[1],\
                            points_container[plot_ind][edge_ind[1]].xy()[0],points_container[plot_ind][edge_ind[1]].xy()[1]]
                plot.draw_edge(edge,lw=0.2,color='green') 
                if total_edge_count%200 == 0:
                    print('plotting %i in %i edges'%(total_edge_count+1,len(G_container[plot_ind]._edge)))
                total_edge_count += 1

            for opt_node_ind in range(len(opt_node_list_container[plot_ind])-1):
                opt_edge_ind = [opt_node_list_container[plot_ind][opt_node_ind],opt_node_list_container[plot_ind][opt_node_ind+1]]
                opt_edge = [points_container[plot_ind][opt_edge_ind[0]].xy()[0],points_container[plot_ind][opt_edge_ind[0]].xy()[1],\
                            points_container[plot_ind][opt_edge_ind[1]].xy()[0],points_container[plot_ind][opt_edge_ind[1]].xy()[1]]
                plot.draw_edge(opt_edge,lw=1,color='red') 
            plot.save(path='./Result/Test%ifig%i.pdf'%(test_num,plot_ind))
        np.savetxt('./Result/Test%i'%(test_num),min_lmc_container)

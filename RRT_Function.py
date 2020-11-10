from Graph_RRT import *
import random
import numpy
from Constant import *
from queue import *

def Sample_Region(region):
    x = random.uniform(region.x_low, region.x_up)
    y = random.uniform(region.y_low, region.y_up)
    X = [x, y]
    return X


def Distance_Points(X1, X2):
    A = numpy.square(X1[0] - X2[0]) + numpy.square(X1[1] - X2[1])
    D = numpy.sqrt(A)
    return D


def Nearest(G, points, point_random):
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
    x_delta = numpy.abs(x_n[0]-point_random[0])
    y_delta = numpy.abs(x_n[1]-point_random[1])
    xy = numpy.sqrt(numpy.square(x_delta)+numpy.square(y_delta))
    x_new_x = x_n[0] + min_edge*y_delta/xy
    x_new_y = x_n[1] + min_edge*x_delta/xy
    points.append(Point(x_new_x, x_new_y))
    x_new = len(points) - 1
    return x_new


def Near(G, x_new, points):
    nodes = G.Get_Nodes()
    near_nodes = []
    for node in nodes:
        if Distance_Points(points[node].xy(), points[x_new].xy()) <= Near_r:
            near_nodes.append(node)
    return near_nodes


def Initialize(x_1, x_2, points):
    p1 = points[x_1]
    p2 = points[x_2]
    p1.Add_g = float('inf')
    p1.Add_lmc(p2.g()+Distance_Points(p1.xy(), p2.xy()))
    p1.Add_parent(x_2)



def Extend(G, Obstacles, points, point_random, queue, goal):
    x_nearest = Nearest(G, points, point_random)
    print("x_nearest is", x_nearest, points[x_nearest].xy())
    x_new = Steer(x_nearest, point_random, points)
    print("x_new is",x_new, points[x_new].xy())
    if Obstacles_Free(Obstacles, points[x_nearest].xy(), points[x_new].xy()):
        Initialize(x_new, x_nearest, points)
        print("lmc of x_new is", points[x_new].lmc())
        near_nodes = Near(G, x_new, points)
        print(near_nodes)
        print("Now have points", len(points))
        print("_________________________")
        for node in near_nodes:
            if Obstacles_Free(Obstacles, points[node].xy(), points[x_new].xy()):
                if points[x_new].lmc() > points[node].g() + Distance_Points(points[node].xy(), points[x_new].xy()):
                    points[x_new].Add_lmc(points[node].g() + Distance_Points(points[node].xy(), points[x_new].xy()))
                    points[x_new].Add_parent(node)
                G.Add_Edge([node, x_new])
                G.Add_Edge([x_new, node])
        G.Add_Node(x_new)
        Update_Queue(x_new, queue, points, goal)


def Obstacles_Free(Obstacles, X1, X2):
    for Obstacle in Obstacles:
        if not Obstacle_Free(Obstacle, X1, X2):
            return False
    return True


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
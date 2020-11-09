import Graph_RRT as GR
import random
import numpy
from Constant import *
from Graph_RRT import *


def Sample_Region(region):
    x = random.uniform(region.x_low, region.x_up)
    y = random.uniform(region.y_low, region.y_up)
    X = [x, y]
    return X


def Distance_Points(X1, X2):
    A = numpy.square(X1[0] - X2[0]) + numpy.square(X1[1] - X2[1])
    D = numpy.sqrt(A)
    return D


def Nearest(G, points, x_random):
    nodes = G.Get_Node()
    D = 10000000
    x_nearest = -1
    for node in nodes:
        if Distance_Points(points[node].xy(), x_random) < D:
            D = Distance_Points(points[node].xy(), x_random)
            x_nearest = node
    return x_nearest


def Steer(x_nearest, x_random, points):
    x_n = points[x_nearest].xy()
    x_delta = numpy.abs(x_n[0]-x_random[0])
    y_delta = numpy.abs(x_n[1]-x_random[1])
    xy = numpy.sqrt(numpy.square(x_delta)+numpy.square(y_delta))
    x_new_x = x_n[0] + min_edge*y_delta/xy
    x_new_y = x_n[1] + min_edge*x_delta/xy
    points.append(Point(x_new_x, x_new_y))
    x_new = len(points) - 1
    return x_new



def Near(G, x_new, points):
    nodes = G.Get_Node()
    near_nodes = []
    for node in nodes:
        if Distance_Points(points[node].xy(), points[x_new].xy()) <= Near_r:
            near_nodes.append(node)
    return near_nodes




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


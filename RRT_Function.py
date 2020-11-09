import Graph_RRT as GR
import random
import numpy


def Sample_Region(region):
    x = random.uniform(region.x_low, region.x_up)
    y = random.uniform(region.y_low, region.y_up)
    X = [x, y]
    return X


def Distance_Points(X1, X2):
    A = numpy.sqrt(X1[0] - X2[0]) + numpy.sqrt(X1[1] - X2[1])
    D = numpy.square(A)
    return D


def Nearest(G, points, x_random):
    nodes = G.Get_Node()
    D = 10000000
    x_nearest = -1
    for node in nodes:
        if Distance_Points(points[node], x_random) < D:
            D = Distance_Points(points[node], x_random)
            x_nearest = node
    return x_nearest


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


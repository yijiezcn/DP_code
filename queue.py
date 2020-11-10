from Graph_RRT import *
from RRT_Function import *


def h(P, goal_region):
    x_goal = (goal_region.x_low + goal_region.x_up)/2
    y_goal = (goal_region.y_low + goal_region.y_up)/2
    goal = [x_goal, y_goal]
    h = Distance_Points(P.xy(), goal)
    return h


def Key(P, goal_region):
    k = [P.lmc() + h(P, goal_region), P.lmc()]
    return k


def Update_Queue(x, queue, points, goal):
    point = points[x]
    if point.g() != point.lmc() and queue.serach(x):
        queue.update(x, Key(point, goal))
    elif point.g() != point.lmc() and not queue.serach(x):
        queue.insert(x, Key(point, goal))
    elif point.g() == point.lmc() and queue.serach(x):
        queue.delete(x)
from Graph_RRT import *
from RRT_Function import *
from queue import *

# # domain
# R = Region(0, 100, 0, 100)
#
# # obstacle
# o1        = Region(50, 60, 50, 60)
# obstacles = [o1]
#
# # goal
# goal   = Region(10, 20, 10, 20)
# # goal = Region(90, 100, 90, 100)
#
# # graph
# G = Graph()
#
# # initial point
# G.Add_Node(0)
# P0     = Point(0, 0, 0, 0)
# points = [P0]
#
# # initial queue
# q = Queue()
# q.search(0)

RRT_Body()

# for i in range(15):
#     point_rand = Sample_Region(R)
#     Extend(G, obstacles, points, point_rand, q, goal)
#     Replan(q, G, points, goal)
#     print("que,", q.Que())
#     print("_________________________")
#
#
#
# print(q.Que())
# print(G.Get_Edges())
# print(G.Get_Nodes())





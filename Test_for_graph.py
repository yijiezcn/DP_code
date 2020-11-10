from Graph_RRT import *
from RRT_Function import *
from queue import *

# domain
R = Region(0, 100, 0, 100)

# obstacle
o1 = Region(30, 60, 30, 60)
obstacles = [o1]

# goal
goal = Region(90, 100, 90, 100)

# graph
G = Graph()

# initial point
G.Add_Node(0)
P0 = Point(0, 0, 0, 0)
points = [P0]


# for i in range(10):
#     point_rand = Sample_Region(R)
#     Extend(G, obstacles, points, point_rand)

# print(G.Get_Edges())
# print(G.Get_Nodes())




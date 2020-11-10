from Graph_RRT import *
from RRT_Function import *

R = Region(0, 100, 0, 100)
o1= Region(30, 60, 30, 60)
obstacles = [o1]
G = Graph()
G.Add_Node(0)
P0 = Point(0, 0, 0, 0)
points = [P0]



for i in range(10):
    point_rand = Sample_Region(R)
    Extend(G, obstacles, points, point_rand)

print(G.Get_Edges())
print(G.Get_Nodes())


# for i in range(20):
#
#     point_random = Sample_Region(R)
#     # print("x_random is ", x_random)
#
#     x_nearest = Nearest(G, points, point_random)
#     print("x_nearest is", x_nearest, points[x_nearest].xy())
#
#     x_new = Steer(x_nearest, point_random, points)
#     # print("x_new is",x_new, points[x_new])
#     G.Add_Node(x_new)
#
#     print(Near(G, x_new, points))
#
#     print("________________")

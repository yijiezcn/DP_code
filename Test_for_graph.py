from Graph_RRT import *
from RRT_Function import *

R = Region(0, 100, 0, 100)
G = Graph()
G.Add_Node(0)
P = Point(0, 0)
points = [P]




for i in range(20):

    x_random = Sample_Region(R)
    # print("x_random is ", x_random)

    x_nearest = Nearest(G, points, x_random)
    print("x_nearest is", x_nearest, points[x_nearest].xy())

    x_new = Steer(x_nearest, x_random, points)
    # print("x_new is",x_new, points[x_new])
    G.Add_Node(x_new)

    print(Near(G, x_new, points))

    print("________________")

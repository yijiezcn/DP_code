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




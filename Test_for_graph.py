from Graph_RRT import *
from RRT_Function import *

R = Region(0, 100, 0, 100)
G = Graph()

points = []

for i in range(10):
    points.append(Sample_Region(R))
    G.Add_Node(i)

print(Nearest(G, points, [0, 0]))

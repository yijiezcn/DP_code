import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
plt.ion()
line_1  = plt.plot([1, 2, 3])
plt.pause(1)
# line_2  = plt.plot([2, 4, 6])
# plt.pause(1)
# node = plt.plot(3,3,'bo')
# plt.pause(2)
# # plt.show()
# line_1.pop(0).remove()
# plt.pause(2)
# node.pop(0).remove()
# plt.pause(2)
# fig = plt.figure()
# ax = plt.gca()
node = np.array([[1,1],[1,2],[2,2],[2,1]])
# plt.pause(2)
# quad = Polygon(node, True,color = 'red', fill=1)
# ax.add_patch(quad)
quad = plt.fill([1,2,2,1],[3,3,4,4])
plt.pause(2)
quad.pop(0).remove()
plt.pause(2)

a,b = 2,1

a = [[1,2],[3,4]]
for item in a:
    print(item)

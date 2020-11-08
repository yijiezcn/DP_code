import numpy as np
from draw_maze import DrawMaze

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    obs_pos = np.transpose(np.nonzero(maze))
    plot    = DrawMaze(maze.shape[0],maze.shape[1],start=start,end=end)
    plot.draw_obstacles(obs_pos)
    plot.win.update()

    # Create start and end node
    start_node   = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node     = Node(None, end)
    end_node.g   = end_node.h   = end_node.f   = 0

    # Initialize both open and closed list
    open_list   = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node  = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list): # Choose the node with smallest f value as current node
            if item.f < current_node.f: 
                current_node  = item
                current_index = index

        plot.draw_cell(current_node.position[0],current_node.position[1],color="#008000")
        plot.win.after(300)
        plot.win.update()

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path    = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            # for closed_child in closed_list: 
            #     if child == closed_child: # ???
            #         continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            # for open_node in open_list:
            #     if child == open_node and child.g > open_node.g: # ???
            #         continue

            # Add the child to the open list
            open_list.append(child)
    plot.show()
    

def main():

    width = 20
    height = 20
    start = (0, 0)
    end = (5, 15)

    obs_pos = np.random.randint(1,height-1,size=[100,2])

    # Create maze, fist initialize with 0, then set obstcle to 1.
    maze = np.zeros((width, height))
    for single_obs in obs_pos:
        maze[single_obs[0]][single_obs[1]] = 1

    astar(maze, start, end)
    # print(path)


if __name__ == '__main__':
    main()
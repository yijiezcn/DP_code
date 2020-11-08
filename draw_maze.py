import tkinter as tk
import numpy as np

class DrawMaze():
    """Draw a maze

    Remember to call show() to display the plot.
    """
    CELL_SIZE = 20
    START_COLOR = "#0000FF" # Blue
    END_COLOR = "#FF0000" # Red
    OBS_COLOR = "#000000" # Black
    TRAJ_COLOR = "#008000" # Green

    def __init__(self, R, C, **kwargs):
        """Plot background and starting/ending point. 
        If no kwargs passed, default starting and ending point will be top-left and bottom-right.
        To customize starting/ending point, make sure you pass both 'start' and 'end'.

        Args:
            R (int): Number of row
            C (int): Number of column 

            Keyword Arguments:
            * *start* (list): Position of starting point 
            * *end* (list): Position of ending point 
        """
        self.R = R
        self.C = C
        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, width=C*self.CELL_SIZE, height=R*self.CELL_SIZE, )
        self.canvas.pack()

        if kwargs == {}: # Defualt starting and ending point to be top-left and bottom-right
            self.start = [0, 0]
            self.end = [self.R - 1, self.C - 1]
        else:
            self.start = kwargs['start']
            self.end = kwargs['end']
            
        # Plot background
        for ri in range(self.R):
            for ci in range(self.C):
                self.draw_cell(ci, ri)
        
        # Plot starting and end point
            self.draw_cell(self.start[0], self.start[1], color=self.START_COLOR) # Blue
            self.draw_cell(self.end[0], self.end[1], color=self.END_COLOR) # Red

        self.win.update()

    def draw_cell(self, r, c, color="#CCCCCC"):
        """Draw a single cell on canvas

        Args:
            c (int): Column number, starts from 0.
            r (int): Row number, starts from 0.
            color (str, optional): color. Defaults to "#CCCCCC"(light grey).
        """
        x0 = c * self.CELL_SIZE
        y0 = r * self.CELL_SIZE
        x1 = c * self.CELL_SIZE + self.CELL_SIZE
        y1 = r * self.CELL_SIZE + self.CELL_SIZE
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2)
        
    def draw_obstacles(self, obs_pos, color=OBS_COLOR):
        """Draw obstacles, default color is black 

        Args:
            obs_pos (2d list): Obstacles' position. Each row is an obstacle, first column-row number, second column-column number.
            color (str, optional): Obstacle color. Defaults to "#000000"(black).
        """
        obs_pos = np.array(obs_pos)
        for current_position in obs_pos:
            if (current_position != [self.start[0], self.start[1]]).any() and\
                 (current_position != [self.end[0], self.end[1]]).any(): # Starting and end point can't be obstacle

                 self.draw_cell(current_position[0], current_position[1], color=color)

    def erase_draw(self, era_pos, draw_pos, draw_clolor):
        """Erase and then draw 

        Args:
            era_pos (2d list): Cells that need to be erased.
            draw_pos (2d list): Cells that need to be draw.
            draw_clolor (str): Color to draw
        """
        for cell in era_pos:
            self.draw_cell(cell[0], cell[1])
        for cell in draw_pos:
            self.draw_cell(cell[0], cell[1], color=draw_clolor)

    def show(self):
        """Display the plot
        """
        self.win.mainloop()


def main():
    plot = DrawMaze(10,10,start=[1,1],end=[4,5])

    obs_pos = [[0, 0],[0, 4],[1, 4],[2, 4],[3, 4],[4, 4],[5, 4],[5, 5],[6, 4],[7, 4],[8, 5],[9, 9]]
    
    plot.draw_obstacles(obs_pos)

    plot.show()

if __name__ =="__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np

class Animation():
    PAUSE_TIME = 0.01
    FIG_SIZE = 5
    def __init__(self,domain_info,start_info,end_info,obs_info):
        """Plot start,end and obstacles

        Args:
            domain_info (list): Infor of the doamin, see self.draw_quad.
            start_info (list): Info of start_zone, see self.draw_quad.
            end_info (lsit): Info of end_zone, see self.draw_quad.
            obs_info (2d list): Each row is the info for an obstacle.
        """
        plt.ion()
        self.fig = plt.figure(figsize=(self.FIG_SIZE,self.FIG_SIZE))
        self.draw_quad(domain_info, color='white')
        self.draw_quad(start_info, color='yellow')
        self.draw_quad(end_info, color='blue')
        for info in obs_info:
            self.draw_quad(info, color='red',PAUSE=1)


    def draw_quad(self, info, color='red', PAUSE=1):
        """Draw quadralateral

        Args:
            info (list): [center_x, center_y, width, height]
            color (str, optional): Defaults to 'red'.
            PAUSE (bool, optional): Flat for pause after plot. Pause if TRUE.

        Returns:
            [type]: Plotted quad
        """
        center = info[:2]
        size = info[2:]
        x_coor, y_coor = self.quad_coor_conv(center, size)
        quad = plt.fill(x_coor, y_coor, color=color)
        if PAUSE:
            plt.pause(self.PAUSE_TIME)
        # quad.pop(0).remove
        # plt.pause(2)
        return quad

    def draw_node(self, center, marker='o', ms=5, color='#acf800', PAUSE=1):
        """Draw node 

        Args:
            center (list): [x_coor, y_coor]
            marker (str, optional): markerstyle. Defaults to 'o'.
            ms (int, optional): Markersize . Defaults to 5.
            color (str, optional): Defaults to '#acf800'--light green.
            PAUSE (bool, optional): Flat for pause after plot. Pause if TRUE.

        Returns:
            [type]: Plotted node
        """
        node = plt.plot(center[0],center[1],marker=marker,ms=ms,color=color)
        if PAUSE:
            plt.pause(self.PAUSE_TIME)
        return node

    def draw_edge(self, info, lw=1, color='green', PAUSE=1):
        """Draw edge

        Args:
            info (list): [start_x,start_y,end_x,end_y]
            lw (int, optional): linewidth. Defaults to 1.
            color (str, optional): Defaults to 'green'.
            PAUSE (bool, optional): Flat for pause after plot. Pause if TRUE.

        Returns:
            [type]: Plotted node
        """
        edge = plt.plot([info[0],info[2]],[info[1],info[3]])
        if PAUSE:
            plt.pause(self.PAUSE_TIME)
        return edge

    def erase(self, obj, single=1, PAUSE=1):
        """erase plotted elements 

        Args:
            obj (plotted element or list): If list, will erase everythin in the list.
            single (int, optional): Erase single obj if TRUE, otherwise multiple.
            PAUSE (bool, optional): Flat for pause after plot. Pause if TRUE.
        """
        if single:
            obj.pop(0).remove()
            if PAUSE:
                plt.pause(self.PAUSE_TIME)
        else:
            for _ in obj:
                _.pop(0).remove()
                if PAUSE:
                    plt.pause(self.PAUSE_TIME)
            
    def quad_coor_conv(self, center, size):
        """Covert [center, sieze] of quad into x,y coordinates 

        Args:
            center (list): Center of quad 
            size (list): width and height of quad 

        Returns:
            list: x,y coordinates
        """
        x_low, x_high = center[0] - size[0]/2, center[0] + size[0]/2
        y_low, y_high = center[1] - size[1]/2, center[1] + size[1]/2
        x_coor = np.array([x_low, x_high, x_high, x_low])
        y_coor = np.array([y_low, y_low, y_high, y_high])
        return x_coor, y_coor

def main():
    domain_info = [0,0,5,5]
    start_info  = [0,0,1,1]
    end_info    = [4,4,1,1]
    obs_info    = [[-1,-1,1,1],[1,-1,1,1]]
    plot        = Animation(domain_info,start_info,end_info,obs_info)

    # plot = Animation()
    quad = plot.draw_quad([3,2,2,4])
    # # plot.draw_quad([3,2],[2,4],'white')
    # # plot.erase(quad)
    node = plot.draw_node([5,5])
    edge = plot.draw_edge([1,1,7,8])
    plot.erase([quad,node,edge],0)
    # a, b = plot.quad_coor_conv([3,2],[2,4])
    # print(a)
    # print(b)


if __name__ == '__main__':
    main()
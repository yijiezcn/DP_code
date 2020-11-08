import tkinter as tk
 
cell_size = 30
C = 12
R = 20
height = R * cell_size
width = C * cell_size
 
 
def draw_cell_by_cr(canvas, c, r, color="#CCCCCC"):
    """
    :param canvas: 画板，用于绘制一个方块的Canvas对象
    :param c: 方块所在列
    :param r: 方块所在行
    :param color: 方块颜色，默认为#CCCCCC，轻灰色
    :return:
    """
    x0 = c * cell_size
    y0 = r * cell_size
    x1 = c * cell_size + cell_size
    y1 = r * cell_size + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2)
 
 
# 绘制空白面板
def draw_blank_board(canvas):
    for ri in range(R):
        for ci in range(C):
            draw_cell_by_cr(canvas, ci, ri)
 

# 定义形状
SHAPES = {
    "O": [(-1, -1), (0, -1), (-1, 0), (0, 0)],
}
 
# 定义形状的颜色
SHAPESCOLOR = {
    "O": "blue",
}
 
def draw_cells(canvas, c, r, cell_list, color="#CCCCCC"):
    """
    绘制指定形状指定颜色的俄罗斯方块
    :param canvas: 画板
    :param r: 该形状设定的原点所在的行
    :param c: 该形状设定的原点所在的列
    :param cell_list: 该形状各个方格相对自身所处位置
    :param color: 该形状颜色
    :return:
    """
    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c + c
        ri = cell_r + r
        # 判断该位置方格在画板内部(画板外部的方格不再绘制)
        if 0 <= c < C and 0 <= r < R:
            draw_cell_by_cr(canvas, ci, ri, color)
 
 
# 下面这行代码放在draw_blank_board(canvas) 下面
# 任取一个位置，如（3,3）绘制一个ｏ型俄罗斯方块，用于展示

 
win = tk.Tk()
canvas = tk.Canvas(win, width=width, height=height, )
canvas.pack()
 
draw_blank_board(canvas)
 
draw_cells(canvas, 3, 3, SHAPES['O'], SHAPESCOLOR['O'])
# 上面这行代码放在win.mainloop()上面

FPS = 500  # 刷新页面的毫秒间隔
def game_loop():
    win.update()
 
    # ===用于展示刷新，后续会删掉===
    import time
    print(time.ctime())
    # ===========================
 
    win.after(FPS, game_loop)


win.update()
for i in range(5):      
    draw_cells(canvas, 3, 3 + 3*i, SHAPES['O'], SHAPESCOLOR['O'])
win.update()

win.mainloop()


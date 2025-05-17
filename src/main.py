from tkinter import Tk, BOTH, Canvas
from constants import *

class Window():
    def __init__(self, width, heigth, title):
        self.__root = Tk()
        self.__root.title = title
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.minsize(width, heigth)
        self.__root.maxsize(width, heigth)
            
    def __repr__(self):
        return f"WIDTH={self.width}, HEIGTH={self.heigth}"
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        while self.running:
            self.redraw()
            self.__root.update()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2
        )

class Cell():
    def __init__(self, window):
        self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        __x1 = -1
        __y1 = -1
        __x2 = -1
        __y2 = -1
        __win = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)).draw(self.window.canvas, "Black")
        if self.has_right_wall:
            Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)).draw(self.window.canvas, "Black")
        if self.has_top_wall:
            Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)).draw(self.window.canvas, "Black")
        if self.has_bottom_wall:
            Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)).draw(self.window.canvas, "Black")

    def draw_move(self, to_cell, undo=False):
        fill_color = "Red"
        self_avg_x = (self.__x1 + self.__x2) / 2
        self_avg_y = (self.__y1 + self.__y2) / 2

        to_cell_avg_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_cell_avg_y = (to_cell.__y1 + to_cell.__y2) / 2

        if undo:
            fill_color = "Grey"
        Line(Point(self_avg_x, self_avg_y), Point(to_cell_avg_x, to_cell_avg_y)).draw(self.window.canvas, fill_color)
    
    def __repr__(self):
        return f"Cell"

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.__cells = []
        
        self.__create_cells()
        self.__draw_cell()
    
    def __repr__(self):
        return print(self.__cells)
        
    def __create_cells(self):
        for column in range(self.num_cols):
            self.__cells.append([])
            for row in range(self.num_rows):
                self.__cells[column].append(Cell(self.window))
    
    def __draw_cell(self):
        for column in range(self.num_cols):
            for row in range(self.num_rows):
                print(self.__cells[column][row])

def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE)
    
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell3 = Cell(window)
    cell4 = Cell(window)

    cell1.draw(100,100,150,150)
    cell2.draw(200,100,250,150)
    cell3.draw(200,200,250,250)
    cell4.draw(100,200,150,250)

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)
    cell3.draw_move(cell4)
    cell4.draw_move(cell1, True)

    maze = Maze(20, 20, 5, 5, 15, 15, window)
    window.wait_for_close()
    

main()
import time
import random
from shapes import Cell




class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.__cells = []

        if not seed:
            seed = random.seed(seed)
                

    def generate(self):
        self.__create_cells()
        self.__draw_cell()
        self.__break_entrance_and_exit()
        
    def __create_cells(self):         
        for column in range(self.num_cols):
            self.__cells.append([])
            for row in range(self.num_rows):
                self.__cells[column].append(Cell(self.window))
    
    def __draw_cell(self):
        if not self.window:
            return
        
        x = self.x1
        y = self.y1
        for column in range(len(self.__cells)):
            for row in range(len(self.__cells[column])):
                self.__cells[column][row].draw(x + self.cell_size_x, y + self.cell_size_y, x, y)
                x += self.cell_size_x + 1
                self._animate()
            x = self.x1
            y += self.cell_size_y + 1
    
    def __break_entrance_and_exit(self):
        start = self.__cells[0][0]
        exit = self.__cells[self.num_cols - 1][self.num_rows - 1]

        start.has_top_wall = False
        start.redraw()
        exit.has_bottom_wall = False
        exit.redraw()

    def __break_walls(self, start_vertex):
        visited = []
        

    def __break_walls_r(self):
        pass

    def _animate(self):
        self.window.redraw()
        time.sleep(0.04)

    
import time
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
        x = self.x1
        y = self.y1
        for column in range(self.num_cols):
            for row in range(self.num_rows):
                self.__cells[column][row].draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
                x += self.cell_size_x + 1
                self._animate()
            x = self.x1
            y += self.cell_size_y + 1
    
    def _animate(self):
        self.window.redraw()
        time.sleep(0.04)
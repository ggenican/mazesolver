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
                

    def generate(self, test=None):
        self.__create_cells()
        if self.window:
            self.__draw_cell()
            self.__break_entrance_and_exit()
        
        if test == "CELL_WALLS":
            return
        self.__break_walls_r(0,0)
        self.__reset_visited()
        
    def __create_cells(self):         
        for row in range(self.num_rows):
            self.__cells.append([])
            for column in range(self.num_cols):
                self.__cells[row].append(Cell(self.window))
    
    def __draw_cell(self):        
        x = self.x1
        y = self.y1
        for row in range(len(self.__cells)):
            for column in range(len(self.__cells[row])):
                self.__cells[row][column].draw(x + self.cell_size_x, y + self.cell_size_y, x, y)
                x += self.cell_size_x + 1
                self._animate()
            x = self.x1
            y += self.cell_size_y + 1
    
    def __break_entrance_and_exit(self):
        start = self.__cells[0][0]
        exit = self.__cells[self.num_rows - 1][self.num_cols - 1]

        start.has_top_wall = False
        start.redraw()
        exit.has_bottom_wall = False
        exit.redraw()      

    def __break_walls_r(self, row, column):
        cells = self._Maze__cells
        vertex = cells[row][column]
        vertex.visited = True
        possible_directions = []

        #Checking left side
        if column != 0 and cells[row][column - 1].visited == False:
            possible_directions.append((row, column - 1, "LEFT"))

        #Checking right side
        if column != self.num_cols - 1 and cells[row][column + 1].visited == False:
            possible_directions.append((row, column + 1, "RIGHT"))

        #Checking top side
        if row != 0 and cells[row - 1][column].visited == False:
            possible_directions.append((row - 1, column, "TOP"))

        #Checking bottom side
        if row != self.num_rows - 1 and cells[row + 1][column].visited == False:
            possible_directions.append((row + 1, column, "BOTTOM"))
        
        while possible_directions:
            next_vertex_indexes = random.choice(possible_directions)
            next_vertex = cells[next_vertex_indexes[0]][next_vertex_indexes[1]]
            possible_directions.remove(next_vertex_indexes)

            if next_vertex.visited == False:
                match next_vertex_indexes[2]:
                    case "LEFT":
                        vertex.has_left_wall = False
                        next_vertex.has_right_wall = False
                    case "RIGHT":
                        vertex.has_right_wall = False
                        next_vertex.has_left_wall = False
                    case "TOP":
                        vertex.has_top_wall = False
                        next_vertex.has_bottom_wall = False
                    case "BOTTOM":
                        vertex.has_bottom_wall = False
                        next_vertex.has_top_wall = False
                
                if self.window:
                    vertex.redraw()
                    next_vertex.redraw()
                    self._animate()
                self.__break_walls_r(next_vertex_indexes[0], next_vertex_indexes[1])
        return       

    def __reset_visited(self):
        for row in range(len(self.__cells)):
            for column in range(len(self.__cells[row])):
                self.__cells[row][column].visited = False

    def solve(self):
        row = 0
        column = 0
        self.__solve_r(row, column)

    def __solve_r(self, row, column):
        cells = self._Maze__cells
        vertex = cells[row][column]
        vertex.visited = True
        possible_directions = []

        if row == self.num_rows - 1 and column == self.num_cols - 1:
            print("Maze solved!")
            return True
        
        left_way = False
        right_way = False
        top_way = False
        bottom_way = False
        
        if vertex.has_left_wall == False and cells[row][column - 1].has_right_wall == False:
            left_way = True
        if vertex.has_right_wall == False and cells[row][column + 1].has_left_wall == False:
            right_way = True
        if vertex.has_top_wall == False and cells[row - 1][column].has_bottom_wall == False:
            top_way = True
        if vertex.has_bottom_wall == False and cells[row + 1][column].has_top_wall == False:
            bottom_way = True

        #Checking left side
        if column != 0 and left_way and cells[row][column - 1].visited == False:
            possible_directions.append((row, column - 1, "LEFT"))

        #Checking right side
        if column != self.num_cols - 1 and right_way and cells[row][column + 1].visited == False:
            possible_directions.append((row, column + 1, "RIGHT"))

        #Checking top side
        if row != 0 and top_way and cells[row - 1][column].visited == False:
            possible_directions.append((row - 1, column, "TOP"))

        #Checking bottom side
        if row != self.num_rows - 1 and bottom_way and cells[row + 1][column].visited == False:
            possible_directions.append((row + 1, column, "BOTTOM"))

        while possible_directions:
            next_vertex_indexes = random.choice(possible_directions)
            
            next_vertex = cells[next_vertex_indexes[0]][next_vertex_indexes[1]]
            possible_directions.remove(next_vertex_indexes)

            if next_vertex.visited == False:
                if self.window:
                    vertex.draw_move(next_vertex)
                    self._animate()
                if self.__solve_r(next_vertex_indexes[0], next_vertex_indexes[1]):
                    return True

            vertex.draw_move(next_vertex, True)    
        
    def _animate(self):
        self.window.redraw()
        time.sleep(0.04)

    
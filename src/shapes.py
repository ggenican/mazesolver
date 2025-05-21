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
    def __init__(self, window=None):
        self.window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        __x1 = -1
        __y1 = -1
        __x2 = -1
        __y2 = -1
        __win = False

    def __repr__(self):
        return f"Walls: Left={self.has_left_wall}, Right={self.has_right_wall}, Top={self.has_top_wall}, Bottom={self.has_bottom_wall}"

    def draw(self, x1, y1, x2, y2):
        if not self.window:
            return
        
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        self._draw_walls()

    def redraw(self):
        self._draw_walls()

    def _draw_walls(self):
        if self.has_left_wall:
            Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)).draw(self.window.canvas, "Black")
        else:
            Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)).draw(self.window.canvas, "White")

        if self.has_right_wall:
            Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)).draw(self.window.canvas, "Black")
        else:
            Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)).draw(self.window.canvas, "White")

        if self.has_top_wall:
            Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)).draw(self.window.canvas, "Black")
        else:
            Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)).draw(self.window.canvas, "White")

        if self.has_bottom_wall:
            Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)).draw(self.window.canvas, "Black")
        else:
            Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)).draw(self.window.canvas, "White")
            
    def draw_move(self, to_cell, undo=False):
        fill_color = "Red"
        self_avg_x = (self.__x1 + self.__x2) / 2
        self_avg_y = (self.__y1 + self.__y2) / 2

        to_cell_avg_x = (to_cell.__x1 + to_cell.__x2) / 2
        to_cell_avg_y = (to_cell.__y1 + to_cell.__y2) / 2

        if undo:
            fill_color = "Grey"
        Line(Point(self_avg_x, self_avg_y), Point(to_cell_avg_x, to_cell_avg_y)).draw(self.window.canvas, fill_color)
    
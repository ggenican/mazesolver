from constants import *
from window import Window
from maze import Maze



def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    maze = Maze(
        x1=20,
        y1=20,
        num_rows=10,
        num_cols=10,
        cell_size_x=35,
        cell_size_y=35,
        window=window
        )
    maze.generate()

    maze._Maze__break_walls_r(0, 0)
    window.wait_for_close()
    
main()
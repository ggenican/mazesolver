from constants import *
from window import Window
from maze import Maze



def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGTH, SCREEN_TITLE)

    maze = Maze(
        x1=20,
        y1=20,
        num_rows=10,
        num_cols=10,
        cell_size_x=35,
        cell_size_y=35,
        window=window
        )
    
    window.wait_for_close()
    
main()
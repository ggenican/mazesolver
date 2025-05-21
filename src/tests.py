import unittest
from maze import Maze



class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.generate()
        
        self.assertEqual(
            len(m1._Maze__cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_cols,
        )

    def test_maze_cell_walls(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.generate("CELL_WALLS")

        for row in range(len(m1._Maze__cells)):
            for column in range(len(m1._Maze__cells[row])):
                self.assertEqual(
                    m1._Maze__cells[row][column].has_left_wall,
                    True
                )
                self.assertEqual(
                    m1._Maze__cells[row][column].has_right_wall,
                    True
                )
                self.assertEqual(
                    m1._Maze__cells[row][column].has_top_wall,
                    True
                )
                self.assertEqual(
                    m1._Maze__cells[row][column].has_bottom_wall,
                    True
                )
    
    def test_maze_explored(self):
        num_cols = 25
        num_rows = 25
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.generate()

        explored = True
        reseted = True

        for row in range(len(m1._Maze__cells)):
            for column in range(len(m1._Maze__cells[row])):
                if m1._Maze__cells[row][column].has_left_wall and \
                   m1._Maze__cells[row][column].has_right_wall and \
                   m1._Maze__cells[row][column].has_top_wall and \
                   m1._Maze__cells[row][column].has_bottom_wall:
                    explored = False

                if m1._Maze__cells[row][column].visited:
                    reseted = False

        self.assertEqual(
            explored,
            True,
            "Maze is not fully explored"
        )
        self.assertEqual(
            reseted,
            True,
            "Maze is not fully reseted"
        )
    
    def test_maze_path_finding(self):
        pass
        # Test that the solver can find a path from start to end
        # Test behavior when there is no solution


if __name__ == "__main__":
    unittest.main()

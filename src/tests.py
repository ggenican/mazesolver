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
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_cell_walls(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.generate()

        for column in range(len(m1._Maze__cells)):
            for row in range(len(m1._Maze__cells[column])):
                self.assertEqual(
                    m1._Maze__cells[column][row].has_left_wall,
                    True
                )
                self.assertEqual(
                    m1._Maze__cells[column][row].has_right_wall,
                    True
                )
                self.assertEqual(
                    m1._Maze__cells[column][row].has_top_wall,
                    True
                )
                self.assertEqual(
                    m1._Maze__cells[column][row].has_bottom_wall,
                    True
                )
    
    def test_maze_generation(self):
        pass
        # Test that after generation, there is a path from the entrance to the exit
        # Test that all cells are reachable (no isolated areas)
        # Verify that the maze doesn't have any cycles (if using a spanning tree algorithm)
    
    def test_maze_path_finding(self):
        pass
        # Test that the solver can find a path from start to end
        # Test behavior when there is no solution


if __name__ == "__main__":
    unittest.main()

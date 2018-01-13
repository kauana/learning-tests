import unittest
from mars_rover import MarsRover

class MarsRoverTest(unittest.TestCase):
    def test_initial_state(self):
        rover = MarsRover(1, 1, "N", 8, 8)
        self.assertEqual(rover.get_x(), 1)
        self.assertEqual(rover.get_y(), 1)
        self.assertEqual(rover.get_direction(), "N")

        rover2 = MarsRover(5, 6, "S", 8, 8)
        self.assertEqual(rover2.get_x(), 5)
        self.assertEqual(rover2.get_y(), 6)
        self.assertEqual(rover2.get_direction(), "S")

    def test_change_direction_right(self):
        rover = MarsRover(4, 1, "N", 8, 8)
        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "E")
        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "S")
        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "W")
        rover.change_direction("R")
        self.assertEqual(rover.get_direction(), "N")

    def test_change_direction_left(self):
        rover = MarsRover(3, 2, "N", 8, 8)
        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "W")
        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "S")
        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "E")
        rover.change_direction("L")
        self.assertEqual(rover.get_direction(), "N")

    def test_move_north(self):
        rover = MarsRover(3, 5, "N", 8, 8)
        rover.move()
        self.assertEqual(rover.get_y(), 6)
        rover.move()
        self.assertEqual(rover.get_y(), 7)

    def test_move_south(self):
        rover = MarsRover(2, 7, "S", 8, 8)
        rover.move()
        self.assertEqual(rover.get_y(), 6)
        rover.move()
        self.assertEqual(rover.get_y(), 5)

    def test_move_east(self):
        rover = MarsRover(2, 5, "E", 8, 8)
        rover.move()
        self.assertEqual(rover.get_x(), 3)
        rover.move()
        self.assertEqual(rover.get_x(), 4)

    def test_move_west(self):
        rover = MarsRover(4, 8, "W", 8, 8)
        rover.move()
        self.assertEqual(rover.get_x(), 3)
        rover.move()
        self.assertEqual(rover.get_x(), 2)

    def test_plateau_boundaries(self):
        rover = MarsRover(4, 8, "E", 4, 8)
        rover.move()
        self.assertEqual(rover.get_x(), 4)
        rover = MarsRover(0, 8, "W", 4, 8)
        rover.move()
        self.assertEqual(rover.get_x(), 0)
        rover = MarsRover(4, 8, "N", 4, 8)
        rover.move()
        self.assertEqual(rover.get_y(), 8)
        rover = MarsRover(4, 0, "S", 4, 8)
        rover.move()
        self.assertEqual(rover.get_y(), 0)



if __name__ == '__main__':
    unittest.main()




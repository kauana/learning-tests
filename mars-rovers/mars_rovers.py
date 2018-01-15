import sys
from mars_rover import MarsRover

def main():
    plateau_layout = input()
    plateau_width, plateau_height = plateau_layout.split(" ")

    for line in sys.stdin:
        x, y, direction = line.strip().split(" ")
        rover = MarsRover(int(x), int(y), direction, int(plateau_width), int(plateau_height))

        # read next line
        line = next(sys.stdin).strip()

        rover.explore(line)
        print(rover.get_x(), rover.get_y(), rover.get_direction())

main()

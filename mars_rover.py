class MarsRover:
    def __init__(self, x, y, direction, width, height):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction

    def change_direction(self, side):
        if side == "R":
            self.direction = {
                "N": "E",
                "E": "S",
                "S": "W",
                "W": "N",
            }.get(self.direction)
        else:
            self.direction = {
                "N": "W",
                "W": "S",
                "S": "E",
                "E": "N",
            }.get(self.direction)

    def move(self):
        if self.direction == "N" and self.y < self.height:
            self.y += 1
        elif self.direction == "S" and self.y > 0:
            self.y -= 1
        elif self.direction == "E" and self.x < self.width:
            self.x += 1
        elif self.direction == "W" and self.x > 0:
            self.x -= 1




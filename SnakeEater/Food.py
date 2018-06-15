from random import randint

class Food(object):
    def __init__(self, Grid):
        self.grid = Grid
        self.color = "#FF7500"
        self.set_pos()

    def set_pos(self):
        x = randint(0, self.grid.grid_x - 1)
        y = randint(0, self.grid.grid_y - 1)
        self.pos = (x, y)

    def display(self):
        self.grid.draw(self.pos, self.color)

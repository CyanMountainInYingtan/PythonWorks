from Food import *

class Snake(object):
    def __init__(self, Grid):
        self.grid = Grid
        self.body = [(10, 6), (10, 7), (10, 8)]
        self.direction = "Up"
        self.status = ['run', 'stop']
        self.speed = 300
        self.color = "#FFC64B"
        self.food = Food(self.grid)
        self.display_food()
        self.gameover = False
        self.score = 0

    def available_grid(self):
        return [i for i in self.grid.grid_list if i not in self.body[2:]]

    def change_direction(self, direction):
        self.direction = direction

    def display(self):
        for (x, y) in self.body:
            self.grid.draw((x, y), self.color)

    def display_food(self):
        while (self.food.pos in self.body):
            self.food.set_pos()
        self.food.display()

    def move(self):
        head = self.body[0]
        if self.direction == 'Up':
            new = (head[0], head[1] - 1)
        elif self.direction == 'Down':
            new = (head[0], head[1] + 1)
        elif self.direction == 'Left':
            new = (head[0] - 1, head[1])
        else:
            new = (head[0] + 1, head[1])
        if not self.food.pos == head:
            pop = self.body.pop()
            self.grid.draw(pop, self.grid.bg) 
        else:
            self.display_food()
            self.score += 1
        self.body.insert(0, new)
        if not new in self.available_grid():
            self.status.reverse()
            self.gameover = True
        else:
            self.grid.draw(new, color=self.color)

from tkinter import *
from random import randint

class Grid(object):
    def __init__(self, master=None, window_width=800, window_height=600, grid_width=50, offset=10):
        self.height = window_height
        self.width = window_width
        self.grid_width = grid_width
        self.offset = offset
        self.grid_x = self.width / self.grid_width
        self.grid_y = self.height / self.grid_width
        self.bg = "#D6ECF0"
        self.canvas = Canvas(master, width=self.width + 2 * self.offset, height=self.height + 2 * self.offset,
                             bg=self.bg)
        self.canvas.pack()
        self.grid_list = self.grid_list()

    def draw(self, pos, color, ):
        x = pos[0] * self.grid_width + self.offset
        y = pos[1] * self.grid_width + self.offset
        self.canvas.create_rectangle(
            x, y, x + self.grid_width, y + self.grid_width, fill=color, outline=self.bg)

    def grid_list(self):
        grid_list = []
        for y in range(0, self.grid_y.__int__()):
            for x in range(0, self.grid_x.__int__()):
                grid_list.append((x, y))

        return grid_list


import tkinter as tk
from Grid import *
from Snake import *


class Game(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid = Grid(master=master, *args, **kwargs)
        self.snake = Snake(self.grid)
        self.bind_all("<KeyRelease>", self.key_release)
        self.snake.display()

    def run(self):
        if not self.snake.status[0] == 'stop':
            self.snake.move()
        if self.snake.gameover == True:
            #message = tkMessageBox.showinfo("Game Over", "your score: %d" % self.snake.score)
            # if message == 'ok':
            tk.sys.exit()
        self.after(self.snake.speed, self.run)

    def key_release(self, event):
        key = event.keysym
        key_dict = {"Up": "Down", "Down": "Up",
                    "Left": "Right", "Right": "Left"}
        if key_dict.__contains__(key) and not key == key_dict[self.snake.direction]:
            self.snake.change_direction(key)
            self.snake.move()
        elif key == 'p':
            self.snake.status.reverse()

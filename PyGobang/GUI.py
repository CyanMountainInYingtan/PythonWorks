#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
import math
import Mark


class Site:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pixel_x = 30 + 30 * self.x
        self.pixel_y = 30 + 30 * self.y


class Chess_Board_Canvas(tk.Canvas):
    def __init__(self, master=None, height=0, width=0):
        tk.Canvas.__init__(self, master, height=height, width=width)
        self.step_record_chess_board = Mark.Step_Record_Chess_Board()
        self.init_chess_board_points()
        self.init_chess_board_canvas()

    def init_chess_board_points(self):
        self.chess_board_points = [
            [None for i in range(15)] for j in range(15)]

        for i in range(15):
            for j in range(15):
                self.chess_board_points[i][j] = Site(i, j)

    def init_chess_board_canvas(self):
        for i in range(15):
            self.create_line(self.chess_board_points[i][0].pixel_x, self.chess_board_points[i][0].pixel_y,
                             self.chess_board_points[i][14].pixel_x, self.chess_board_points[i][14].pixel_y)

        for j in range(15):
            self.create_line(self.chess_board_points[0][j].pixel_x, self.chess_board_points[0][j].pixel_y,
                             self.chess_board_points[14][j].pixel_x, self.chess_board_points[14][j].pixel_y)

        for i in range(15):
            for j in range(15):
                r = 1
                self.create_oval(self.chess_board_points[i][j].pixel_x-r, self.chess_board_points[i][j].pixel_y-r,
                                 self.chess_board_points[i][j].pixel_x+r, self.chess_board_points[i][j].pixel_y+r)

    def click1(self, event):
        for i in range(15):
            for j in range(15):
                square_distance = math.pow((event.x - self.chess_board_points[i][j].pixel_x), 2) + math.pow(
                    (event.y - self.chess_board_points[i][j].pixel_y), 2)
                if (square_distance <= 200) and (not self.step_record_chess_board.has_record(i, j)):
                    if self.step_record_chess_board.who_to_play() == 1:
                        self.create_oval(self.chess_board_points[i][j].pixel_x-10, self.chess_board_points[i][j].pixel_y-10,
                                         self.chess_board_points[i][j].pixel_x+10, self.chess_board_points[i][j].pixel_y+10, fill='white')

                    elif self.step_record_chess_board.who_to_play() == 2:
                        self.create_oval(self.chess_board_points[i][j].pixel_x-10, self.chess_board_points[i][j].pixel_y-10,
                                         self.chess_board_points[i][j].pixel_x+10, self.chess_board_points[i][j].pixel_y+10, fill='black')

                    self.step_record_chess_board.insert_record(i, j)
                    result = self.step_record_chess_board.check()

                    if result == 1:
                        self.create_text(240, 550, text='执白子者胜利')
                        self.unbind('<Button-1>')

                    elif result == 2:
                        self.create_text(240, 550, text='执黑子者胜利')
                        self.unbind('<Button-1>')


class Chess_Board_Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        self.chess_board_label_frame = tk.LabelFrame(
            self, text="鹰潭青山制作", padx=8, pady=8)
        self.chess_board_canvas = Chess_Board_Canvas(
            self.chess_board_label_frame, height=600, width=480)
        self.chess_board_canvas.bind(
            '<Button-1>', self.chess_board_canvas.click1)
        self.chess_board_label_frame.pack()
        self.chess_board_canvas.pack()

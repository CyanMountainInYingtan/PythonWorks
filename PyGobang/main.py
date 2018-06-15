#!/usr/bin/env python
#-*- coding: utf-8 -*-

import GUI
import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    gui_chess_board = GUI.Chess_Board_Frame(window)
    gui_chess_board.pack()
    window.mainloop()

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Just a simple snake clone by Tammo Behrends.

Sept. 2014 @ Vancouver, CA
'''

import sys
import tkinter as tk


_WIDTH = 800
_HEIGHT = 600


class SnakeCanvas(tk.Canvas):
    ''' The snake game it self. '''
    def __init__(self, master):
        tk.Canvas.__init__(self, width=_WIDTH, height=_HEIGHT,
            background='dark gray', highlightthickness=0)

        self.master = master 
        self.pack()


class SnakeFrame(tk.Frame):
    ''' The main window for the snake game. '''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.game = SnakeCanvas(master)

        self.pack()
        master.title('snake_tk')


def main():
    ''' The main entry point for this program. '''
    root = tk.Tk()
    app = SnakeFrame(master=root)
    app.mainloop()

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Just a simple snake clone by Tammo Behrends.

Sept. 2014 @ Vancouver, CA
'''

import sys
import tkinter as tk

from enum import Enum, unique


_WIDTH = 800
_HEIGHT = 600

@unique
class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class SnakeCanvas(tk.Canvas):
    ''' The snake game itself. '''
    def __init__(self, master):
        tk.Canvas.__init__(self, width=_WIDTH, height=_HEIGHT,
            background='dark gray', highlightthickness=0)

        self.master = master
        self.setup()
        self.pack()

    def setup(self):
        self.direction = Direction.LEFT

        self.bind_all("<Key>", self.onKeyEvent)

    def onKeyEvent(self, event):
        key = event.keysym

        if key == 'Left' and self.direction is not Direction.RIGHT:
            self.direction = Direction.LEFT
            print(key)

        if key == 'Right' and self.direction is not Direction.LEFT:
            self.direction = Direction.RIGHT
            print(key)

        if key == 'Up' and self.direction is not Direction.DOWN:
            self.direction = Direction.UP
            print(key)

        if key == 'Down' and self.direction is not Direction.UP:
            self.direction = Direction.DOWN
            print(key)


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

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
_SIZE = 10
_INTERVAL = 200


@unique
class Direction(Enum):
    ''' Direction constants. '''
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
        self.running = True

        width, height = _WIDTH // _SIZE, _HEIGHT // _SIZE
        self.snake = [[width - _SIZE, height], [width, height], [width + _SIZE, height]]

        self.bind_all("<Key>", self.onKeyEvent)
        self.after(_INTERVAL, self.onUpdate)

    def draw(self):
        self.delete("all")

        head = self.snake[0]
        self.create_rectangle(head[0], head[1], head[0] + _SIZE, head[1] + _SIZE,
                              outline="#000", fill="#a30000")

        for element in self.snake[1:]:
            self.create_rectangle(element[0], element[1], element[0] + _SIZE, element[1] + _SIZE,
                                  outline="#000", fill="#006610")

    def move(self):
        head = self.snake[0]

        if self.direction is Direction.RIGHT:
            new_x, new_y = (head[0] + _SIZE) % _WIDTH, head[1]
        if self.direction is Direction.LEFT:
            new_x, new_y = (head[0] - _SIZE) % _WIDTH, head[1]
        if self.direction is Direction.UP:
            new_x, new_y = head[0], (head[1] - _SIZE) % _HEIGHT
        if self.direction is Direction.DOWN:
            new_x, new_y = head[0], (head[1] + _SIZE) % _HEIGHT

        self.snake = [[new_x, new_y]] + self.snake[:-1]

    def onUpdate(self):
        if self.running:
            self.move()
            self.draw()

            self.after(_INTERVAL, self.onUpdate)

    def onKeyEvent(self, event):
        if event.keysym == 'Left' and self.direction is not Direction.RIGHT:
            self.direction = Direction.LEFT

        if event.keysym == 'Right' and self.direction is not Direction.LEFT:
            self.direction = Direction.RIGHT

        if event.keysym == 'Up' and self.direction is not Direction.DOWN:
            self.direction = Direction.UP

        if event.keysym == 'Down' and self.direction is not Direction.UP:
            self.direction = Direction.DOWN


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

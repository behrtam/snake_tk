#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Just a simple snake clone by Tammo Behrends.

Sept. 2014 @ Vancouver, CA
'''

import sys
import tkinter as tk

from enum import Enum, unique
from random import randint


_WIDTH = 900
_HEIGHT = 600
_SIZE = 30
_INTERVAL = 100


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
        self.bind_all("<Key>", self.on_key_event)
        self.pack()

    def setup(self):
        self.direction = Direction.LEFT
        self.running = True
        self.game_over = False

        width, height = int((_WIDTH // _SIZE) / 2 * _SIZE), int((_HEIGHT // _SIZE) / 2 * _SIZE)
        self.snake = [[width - _SIZE, height], [width, height], [width + _SIZE, height]]
        self.create_bit()

        self.after(_INTERVAL, self.on_update)

    def create_bit(self):
        while True:
            new_bit = [randint(0, (_WIDTH // _SIZE) - 1) * _SIZE,
                       randint(0, (_HEIGHT // _SIZE) - 1) * _SIZE]
            if new_bit not in self.snake:
                break
        self.bit = new_bit

    def draw(self):
        self.delete("all")

        self.create_rectangle(self.bit[0], self.bit[1],
                              self.bit[0] + _SIZE, self.bit[1] + _SIZE,
                              outline="#915a07", fill="#e88f0c")

        head = self.snake[0]
        self.create_rectangle(head[0], head[1], head[0] + _SIZE, head[1] + _SIZE,
                              outline="#000", fill="#a30000")

        for element in self.snake[1:]:
            self.create_rectangle(element[0], element[1],
                                  element[0] + _SIZE, element[1] + _SIZE,
                                  outline="#000", fill="#006610")

        if self.game_over:
            self.create_text(_WIDTH // 2, _HEIGHT // 2, text="game over!")

    def move(self):
        head = self.snake[0]

        if self.direction is Direction.RIGHT:
            new_head = [(head[0] + _SIZE) % _WIDTH, head[1]]
        if self.direction is Direction.LEFT:
            new_head = [(head[0] - _SIZE) % _WIDTH, head[1]]
        if self.direction is Direction.UP:
            new_head = [head[0], (head[1] - _SIZE) % _HEIGHT]
        if self.direction is Direction.DOWN:
            new_head = [head[0], (head[1] + _SIZE) % _HEIGHT]

        # collision detection
        if new_head in self.snake:
            self.running = False
            self.game_over = True

        # collecting the bit and grow the snake
        elif self.bit == new_head:
            self.snake = [new_head] + self.snake
            self.create_bit()

        # just moving forward
        else:
            self.snake = [new_head] + self.snake[:-1]

    def on_update(self):
        if self.running:
            self.move()
            self.draw()

            self.after(_INTERVAL, self.on_update)

    def on_key_event(self, event):
        if event.keysym == 'Left' and self.direction is not Direction.RIGHT:
            self.direction = Direction.LEFT

        if event.keysym == 'Right' and self.direction is not Direction.LEFT:
            self.direction = Direction.RIGHT

        if event.keysym == 'Up' and self.direction is not Direction.DOWN:
            self.direction = Direction.UP

        if event.keysym == 'Down' and self.direction is not Direction.UP:
            self.direction = Direction.DOWN

        if event.keysym == 'q':
            self.master.destroy()

        if event.keysym == 'p':
            self.running = not self.running
            if self.running:
                self.on_update()

        if not self.running and event.keysym == 'r':
            self.setup()


class SnakeFrame(tk.Frame):
    ''' The main window for the snake game. '''
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.game = SnakeCanvas(master)

        self.pack()
        master.title('snake_tk by tammo')


def main():
    ''' The main entry point for this program. '''

    if (_HEIGHT % _SIZE != 0) or (_WIDTH % _SIZE != 0):
        print("error: The 'HEIGHT' and the 'WIDTH' neeed to be a multiple of the 'SIZE'!",
              file=sys.stderr)
        return 1

    root = tk.Tk()
    app = SnakeFrame(master=root)
    app.mainloop()

if __name__ == '__main__':
    sys.exit(main())

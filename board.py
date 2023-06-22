from random import randint
from tkinter import *

from settings import *


class Board:
    def __init__(self, logic):
        self.logic = logic

    def create_board(self, root):
        board = [[0] * 15 for _ in range(15)]
        for x in range(15):
            for y in range(15):
                board[y][x] = Label(
                    root,
                    width=2,
                    height=1,
                    bg=GRAY,
                    font="Arial 11 bold",
                )
                board[y][x].grid(column=x, row=y + 1)
        self.set_mines(board)
        self.set_points(board)
        return board

    def create_cover(self, root, hidden):
        tiles = [[0] * 15 for _ in range(15)]
        for x in range(15):
            for y in range(15):
                tiles[y][x] = Button(
                    root,
                    width=2,
                    height=1,
                    pady=-1,
                    bg=LGRAY,
                    activebackground=GRAY,
                    command=lambda nx=x, ny=y, tile=tiles: self.logic.click(
                        nx,
                        ny,
                        tile,
                        hidden,
                        root,
                    ),
                )
                tiles[y][x].grid(column=x, row=y + 1)
                tiles[y][x].bind("<Button-3>", self.logic.flag)
        return tiles

    def set_mines(self, board):
        bombs = BOMB_COUNT
        while bombs:
            x = randint(0, 14)
            y = randint(0, 14)
            if board[y][x]["text"] != BOMB:
                board[y][x]["text"] = BOMB
                board[y][x]["background"] = RED
                board[y][x]["foreground"] = BLACK
                bombs -= 1

    def set_color(self, board):
        if board["text"] == "1":
            return BLUE
        if board["text"] == "2":
            return GREEN
        if board["text"] == "3":
            return RED
        if board["text"] == "4":
            return PURPLE
        if board["text"] == "5":
            return MAROON
        return CYAN

    def count_bombs(self, board, x, y):
        counter = 0
        for ny in range(y - 1, y + 2):
            for nx in range(x - 1, x + 2):
                if ny < 0 or nx < 0:
                    continue
                try:
                    if board[ny][nx]["text"] == BOMB:
                        counter += 1
                except IndexError:
                    pass
        return str(counter) if counter > 0 else ""

    def set_points(self, board):
        for x in range(15):
            for y in range(15):
                if board[y][x]["text"] != BOMB:
                    board[y][x]["text"] = self.count_bombs(board, x, y)
                    board[y][x]["foreground"] = self.set_color(board[y][x])

import ctypes
from tkinter import *
from settings import *


class Window:
    def __init__(self, root, board):
        self.root = root
        self.board = board
        self.width, self.height = 360, 435
        self.screensize = self.get_screensize()
        self.screensize_offset = (self.screensize[0] - self.width) // 2, (
            self.screensize[1] - self.height
        ) // 2
        root.geometry(
            f"{self.width}x{self.height}+{self.screensize_offset[0]}+{self.screensize_offset[1]}"
        )
        root.resizable(False, False)
        root.configure(bg="#606060")
        root.title("Saper")

        self.reset_btn = Button(
            self.root,
            width=10,
            height=3,
            bg=LGRAY,
            activebackground=GRAY,
            text="RESET",
            command=self.reset_board,
        )
        self.reset_btn.grid(column=0, row=0, columnspan=15, pady=10)

        self.hidden = self.board.create_board(self.root)
        self.cover = self.board.create_cover(self.root, self.hidden)

    def reset_board(self):
        self.hidden = self.board.create_board(self.root)
        self.cover = self.board.create_cover(self.root, self.hidden)

    def get_screensize(self):
        self.user32 = ctypes.windll.user32
        return self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)

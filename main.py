from tkinter import Tk

from board import Board
from logic import Logic
from window import Window


def main():
    board = Board(Logic)
    root = Tk()
    app = Window(root, board)
    root.mainloop()


if __name__ == "__main__":
    main()

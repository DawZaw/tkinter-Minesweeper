from itertools import chain

from tkinter import *
from settings import *
from popup import Popup


class Logic:
    def flag(event):
        if event.widget["background"] != RED:
            event.widget.configure(bg=RED, text=FLAG, activebackground=RED)
        else:
            event.widget.configure(bg=LGRAY, text="", activebackground=GRAY)

    def uncover(x, y, tiles, hidden):
        if hidden[y][x]["text"] == "":
            if tiles[y][x].winfo_exists() and tiles[y][x]["text"] != FLAG:
                tiles[y][x].destroy()
                if x > 0:
                    Logic.uncover(x - 1, y, tiles, hidden)
                if x < 14:
                    Logic.uncover(x + 1, y, tiles, hidden)
                if y > 0:
                    Logic.uncover(x, y - 1, tiles, hidden)
                if y < 14:
                    Logic.uncover(x, y + 1, tiles, hidden)
                if x > 0 and y > 0:
                    Logic.uncover(x - 1, y - 1, tiles, hidden)
                if x > 0 and y < 14:
                    Logic.uncover(x - 1, y + 1, tiles, hidden)
                if x < 14 and y > 0:
                    Logic.uncover(x + 1, y - 1, tiles, hidden)
                if x < 14 and y < 14:
                    Logic.uncover(x + 1, y + 1, tiles, hidden)
        if tiles[y][x].winfo_exists() and tiles[y][x]["text"] != FLAG:
            tiles[y][x].destroy()
        return

    def clear_tiles(tiles):
        for x in range(15):
            for y in range(15):
                if tiles[y][x].winfo_exists():
                    tiles[y][x].destroy()

    def click(x, y, tiles, hidden, root):
        if tiles[y][x]["background"] != RED:
            Logic.uncover(x, y, tiles, hidden)
            if hidden[y][x]["text"] == BOMB:
                Popup(root, "lost")
                Logic.clear_tiles(tiles)
        Logic.check_win(tiles, root)

    def check_win(tiles, root):
        counter = 0
        tls = chain.from_iterable(tiles)
        for tl in tls:
            if tl.winfo_exists():
                counter += 1
        if counter == BOMB_COUNT:
            Popup(root, "won")
            Logic.clear_tiles(tiles)

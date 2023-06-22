import ctypes
from tkinter import *


class Popup:
    def __init__(self, root, result):
        self.root = root
        self.screensize = self.get_screensize()
        self.width, self.height = 200, 85
        self.offset = (self.screensize[0] - self.width) // 2, (
            self.screensize[1] - self.height
        ) // 2
        self.top = Toplevel(self.root)
        self.top.geometry(
            f"{self.width}x{self.height}+{self.offset[0]}+{self.offset[1]}"
        )
        self.top.resizable(False, False)
        if result == "lost":
            self.lose_msg = Label(self.top, text="YOU LOST!", anchor="center")
        elif result == "won":
            self.lose_msg = Label(self.top, text="YOU WON!", anchor="center")
        self.lose_msg.pack(pady=25)

    def get_screensize(self):
        self.user32 = ctypes.windll.user32
        return self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)

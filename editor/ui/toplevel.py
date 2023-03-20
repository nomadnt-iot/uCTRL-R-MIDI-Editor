import tkinter as tk

class Toplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
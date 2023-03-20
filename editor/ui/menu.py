import tkinter as tk

class Menu(tk.Menu):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

    def enable(self):
        self.configure(state='enable')

        return self

    def disable(self):
        self.configure(state='disabled')

        return self
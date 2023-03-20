import tkinter as tk

class Button(tk.Button): 
    def __init__(self, master=None, text=None, **kw):
        super().__init__(master, text=text, **kw)

    def enable(self):
        self.configure(state='normal')

        return self

    def disable(self):
        self.configure(state='disabled')

        return self
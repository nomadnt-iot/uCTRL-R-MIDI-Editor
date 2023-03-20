import tkinter as tk

class Fieldset(tk.LabelFrame):
    def __init__(self, master=None, text=None, **kw):
        super().__init__(master, text=text, **kw)
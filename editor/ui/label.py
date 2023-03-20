import tkinter as tk

class Label(tk.Label):
    def __init__(self, master=None, text=None, **kw):
        super().__init__(master, text=text, **kw)

    def enable(self):
        self.configure(state='normal')

        return self

    def disable(self):
        self.configure(state='disabled')

        return self

    def set(self, value):
        self.configure(text=value)
        # self.update_idletasks()

        return self

    def clear(self):
        self.configure(text=None)
        # self.update_idletasks()
        
        return self
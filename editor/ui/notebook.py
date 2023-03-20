import tkinter as tk
from tkinter import ttk

class Notebook(ttk.Notebook):

    def enable(self):
        self.configure(state='enable')

        return self

    def disable(self):
        self.configure(state='disabled')

        return self
from tkinter import ttk

from ..ui import Frame
from .settings import Settings

class Tabs(Frame):
    def __init__(self, master=None, **kw):
        self.master = master
        super().__init__(self.master, **kw)

        self._setup()

    def _setup(self):
        self.notebook = ttk.Notebook(self)

        settings = Settings(self.notebook)
        settings.pack(fill='both', expand=True)

        self.notebook.add(settings, text='Settings')
        
        self.notebook.pack(fill='both', expand=True)
    
    def disable(self):
        for i, tab in enumerate(self.notebook.tabs()):
            self.notebook.tab(i, state='disabled')
        
    
    def enable(self):
        for i, tab in enumerate(self.notebook.tabs()):
            self.notebook.tab(i, state='normal')
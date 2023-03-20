from ui import Menu

class Menubar(Menu):
    def __init__(self, master=None, **kw):
        self.master = master

        super().__init__(self.master, **kw)

        self._setup()

    def _setup(self):
        file = Menu(self, tearoff=False)
        file.add_command(label='Exit', command=self.master.quit)
        self.add_cascade(label='File', menu=file)

        help = Menu(self, tearoff=False)
        help.add_command(label='About', command=self.master.about)
        self.add_cascade(label='Help', menu=help)
from ui import Frame, Label, Link, Picture, Toplevel

class About(Toplevel):
    def __init__(self, master=None, height=350, width=350, **kw):
        self.master = master

        super().__init__(self.master, height=height, width=width, **kw)
        
        self._setup()
    
    def _setup(self):
        self.resizable(False, False)
        self.title('About uCTRL-R Editor')
        # self.transient(self.master)

        frame = Frame(self)
        frame.pack()

        self.logo = Picture(frame, image='data/logo.jpg')
        self.logo.pack(padx=20, pady=30)

        self.title = Label(frame, 'uCTRL Editor', font=('Helvetica', 14, 'bold'))
        self.title.pack(padx=0, pady=5)

        self.version = Label(frame, 'Version: %s' % ('0.8'))
        self.version.pack(padx=0, pady=5)
        
        self.link = Link(frame, 'http://www.daelectronics.com')
        self.link.pack(padx=0, pady=30)
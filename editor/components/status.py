from ui import Label

class Status(Label):
    def __init__(self, master=None, text=None, borderwidth=1, relief='sunken', anchor='w', **kw):
        super().__init__(master=master, text=text, borderwidth=borderwidth, relief=relief, anchor=anchor, **kw)
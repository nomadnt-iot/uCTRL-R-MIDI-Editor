from .label import Label
import webbrowser

class Link(Label):
    def __init__(self, master=None, href=None, text=None, font=('Helvetica', 9 ,'underline'), foreground='blue', cursor='hand2', **kw):
        self.master = master
        self._href = href
        
        if not text:
            text = self._href

        super().__init__(master, text=text, font=font, foreground=foreground, cursor=cursor, **kw)

        self.bind('<Button-1>', self.onClick)
    
    def onClick(self, ev):
        webbrowser.open_new_tab(self._href)
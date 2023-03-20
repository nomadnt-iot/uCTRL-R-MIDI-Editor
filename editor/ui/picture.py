from .label import Label

from PIL import Image as Img, ImageTk
from pathlib import Path

class Picture(Label):
    def __init__(self, master=None, image=None, **kw):
        path = Path(__file__).resolve().parent.parent.joinpath(image)
        print(path)
        self.image = ImageTk.PhotoImage(Img.open(path))
        super().__init__(master, image=self.image, **kw)

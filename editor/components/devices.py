from ui import Frame, Select, Button, Label

class Devices(Frame):
    def __init__(self, master=None, **kw):
        self.master = master

        super().__init__(master=self.master, **kw)

        self._setup()

    def _setup(self):
        self.button = Button(self, 'Detect devices', command=self.master.scan)

        self.options = Select(self, command=self.select)
        self.options.disable()
        
        self.label = Label(self, 'Choose device')
        self.label.disable()

        self.button.pack(side='left')
        self.options.pack(side='right')
        self.label.pack(side='right', padx=5, pady=5)

    def update(self, devices):
        self.label.disable()

        options = [device['name'] for device in devices]
        self.options.fill(options)

        if len(options) > 0:    
            self.label.enable()
        
        return self

    def select(self, device):
        for item in self.master.devices:
            if item['name'] == device:
                self.master.connect(item)
                break

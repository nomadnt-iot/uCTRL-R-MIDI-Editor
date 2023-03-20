import tkinter as tk
import time

from components import About, Status, Menubar, Devices, Settings
from device.device import list_devices, Device

class Editor(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)

        # widgets dictionary
        self.components = {}

        # available devices
        self.devices = []

        # selected device
        self.device = Device()

        self._setup()
        self.scan()
    
    def _setup(self):
        """ Setup widget components """

        self.resizable(False, False)
        self.title('uCTRL-R Editor')
        self.configure(menu=Menubar(self))

        self.components['status'] = Status(self, 'Initializing components...')
        self.components['status'].pack(side='bottom', fill='x', padx=10, pady=5)

        self.components['devices'] = Devices(self)
        self.components['devices'].pack(fill='x', padx=10, pady=10)

        self.components['settings'] = Settings(self)        
        self.components['settings'].pack(fill='both', expand=True)        

    def about(self):
        """ Show about window """
        About(self)

    def _scan(self):
        """ Scanning for new devices and connect to the first found """
        self.devices = list_devices()
        if len(self.devices) > 0: self.connect(self.devices[0])

    # cambiare il nome della funzione
    def scan(self):
        self.components['status'].set('Scanning for new devices')
        
        self.devices = list_devices()
    
        self.components['devices'].update(self.devices)

        if len(self.devices) > 0:
            self.components['status'].set('Connecting to {}'.format(self.devices[0]['name']))
            self.connect(self.devices[0])
            self.components['settings'].enable()
            self.components['settings'].reload()
        else:
            self.components['settings'].disable()
            self.components['status'].set('No devices found')

        return self

    def connect(self, device):
        """ Connect to device """
        self.components['status'].set('Connected to {}'.format(device['name']))        
        self.device.connect(device['port'])
        self.device.load()
    
    def disconnect(self):
        """ Disconnect device """
        self.device.disconnect()

    def save(self):
        """ Save configuration to device """
        self.components['status'].set('Saving configuration')
        self.device.save()
        self.components['status'].set('Configuration saved')
    
    def reset(self):
        """ Reset configuration to device """
        self.components['status'].set('Resetting configuration')
        # self.components['settings'].disable()
        self.device.reset()
        # la reset dovrebbe già avere la load
        self.device.load()
        # self.components['settings'].enable()
        self.components['settings'].reload()
        self.components['status'].set('Configuration resetted')

if __name__ == '__main__':
    e = Editor()
    e.mainloop()
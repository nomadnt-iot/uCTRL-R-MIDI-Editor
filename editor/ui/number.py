import tkinter as tk

class Number(tk.Spinbox):
    def __init__(self, master=None, values=None, variable=None, command=None, width=15, **kw):
        self.master = master

        if variable == None:
            variable = tk.StringVar()

        self._variable = variable
        self._command = command

        super().__init__(self.master, values=values, textvariable=self._variable, width=width, command=self._command_cb, **kw)
        self.bind('<Key>', self._key)

    def enable(self):
        self.configure(state='normal')

        return self

    def disable(self):
        self.configure(state='disabled')

        return self

    def set(self, value):
        self._variable.set(value)
        # self.delete(0, 'end')
        # self.insert(0, value)

    def onChange(self, command):
        if command is None:
            self._command = lambda: None
        else:
            self._command = command

        return self
    
    def _command_cb(self):
        if self._command:
            self._command(self.get())
    
    def _key(self, event):
        print(event.char)
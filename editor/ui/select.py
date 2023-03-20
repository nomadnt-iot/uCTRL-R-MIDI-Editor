import tkinter as tk

class Select(tk.OptionMenu):
    def __init__(self, master=None, options=[], variable=None, command=None, **kw):
        self.master = master
        self.options = options

        if variable == None:
            variable = tk.StringVar()

        self._variable = variable
        self._command = command

        if(len(options) == 0):
            super().__init__(self.master, self._variable, None, command=self._command_cb, **kw)
        else:
            super().__init__(self.master, self._variable, *self.options, command=self._command_cb, **kw)

        self._resize()
        self._set_option_by_index(0)

    def enable(self):
        self.configure(state='normal')

        return self

    def disable(self):
        self.configure(state='disabled')

        return self

    def clear(self):
        self['menu'].delete(0, 'end')
        self._variable.set('')

        return self

    def fill(self, options):
        self.disable()

        self.options = options

        self.clear()

        for option in self.options:
            self['menu'].add_command(label=option, command=lambda value=option : self._command_cb(value))
            # self['menu'].add_command(label=option, command=tk._setit(self.variable, option, self._command_cb))
        
        if len(self.options) > 0:
            self._set_option_by_index(0)
            self.enable()

        self._resize()

        return self
    
    def get(self):
        return self._variable.get()

    def set(self, value):
        return self._variable.set(value)

    def _set_option_by_index(self, index):
        if index < len(self.options):
            self._variable.set(self.options[index])
            return True
        else:
            return False

    def _command_cb(self, value):
        if self._command:
            self._command(value)

    def _resize(self):
        width = 10
        size = self['menu'].index('end') or 0 + 1

        if size:
            for i in range(size):
                w = len(self['menu'].entrycget(i, 'label'))
                if w > width: width = w

        self.configure(width=width, anchor='w')

    def onChange(self, command):
        if command is None:
            self._command = lambda: None
        else:
            self._command = command

        return self
from ui import Frame, Fieldset, Label, Select, Number, Button
from constants import BUTTON_LABELS, BUTTON_FUNCTIONS, BUTTON_NUMBERS, BUTTON_CONTROLS, BUTTON_CHANNELS
from constants import SLIDER_LABELS, SLIDER_NUMBERS, SLIDER_CONTROLS, SLIDER_CHANNELS

class Settings(Frame):
    def __init__(self, master=None, **kw):
        self.master = master
        self.device = self.master.device

        super().__init__(self.master, **kw)        
        
        self.buttons = [{'press': {}, 'hold': {}} for _ in range(4)]
        self.sliders = [{} for _ in range(2)]
        self.actions = {}

        self._setup_press_panel()
        self._setup_hold_panel()
        self._setup_sliders_panel()
        self._setup_actions_panel()

    def _setup_press_panel(self):
        frame = Fieldset(self, 'Press and release')

        # Fieldset Press and release
        for i, label in enumerate(BUTTON_LABELS):
            Label(frame, label).grid(column=(i + 1), row=1, sticky='W', padx=4)

        for i, button in enumerate(self.buttons):
            label = Label(frame, 'Button %s' % (i + 1))
            label.grid(column=0, row=(i + 2), sticky='W', padx=4)

            button['press']['mode'] = Select(frame, BUTTON_FUNCTIONS)
            button['press']['mode'].onChange(lambda value, index=i : self._setButtonMode(index, 'press', value))
            button['press']['mode'].grid(column=1, row=(i + 2), padx=3, pady=3, sticky='EW')
        
            button['press']['program'] = Number(frame, BUTTON_NUMBERS)
            button['press']['program'].onChange(lambda value, index=i : self._setButtonProgram(index, 'press', value))
            button['press']['program'].grid(column=2, row=(i + 2), padx=3, pady=3, sticky='EW')

            button['press']['control'] = Number(frame, BUTTON_CONTROLS)
            button['press']['control'].onChange(lambda value, index=i : self._setButtonControl(index, 'press', value))
            button['press']['control'].grid(column=3, row=(i + 2), padx=3, pady=3, sticky='EW')

            button['press']['channel'] = Number(frame, BUTTON_CHANNELS)
            button['press']['channel'].onChange(lambda value, index=i : self._setButtonChannel(index, 'press', value))
            button['press']['channel'].grid(column=4, row=(i + 2), padx=3, pady=3, sticky='EW')

        frame.grid(column=0, row=0, sticky='N', padx=10, pady=10)

    def _setup_hold_panel(self):
        frame = Fieldset(self, 'Press, hold and release')

        # Fieldset Press, hold and release
        for i, label in enumerate(BUTTON_LABELS):
            Label(frame, label).grid(column=(i + 1), row=1, sticky='W', padx=4)

        for i, button in enumerate(self.buttons):
            label = Label(frame, 'Button %s' % (i + 1))
            label.grid(column=0, row=(i + 2), sticky='W', padx=4)

            button['hold']['mode'] = Select(frame, BUTTON_FUNCTIONS[:-1])
            button['hold']['mode'].onChange(lambda value, index=i : self._setButtonMode(index, 'hold', value))
            button['hold']['mode'].grid(column=1, row=(i + 2), padx=3, pady=3, sticky='EW')

            button['hold']['program'] = Number(frame, BUTTON_NUMBERS)
            button['hold']['program'].onChange(lambda value, index=i : self._setButtonProgram(index, 'hold', value))
            button['hold']['program'].grid(column=2, row=(i + 2), padx=3, pady=3, sticky='EW')

            button['hold']['control'] = Number(frame, BUTTON_CONTROLS)
            button['hold']['control'].onChange(lambda value, index=i : self._setButtonControl(index, 'hold', value))
            button['hold']['control'].grid(column=3, row=(i + 2), padx=3, pady=3, sticky='EW')

            button['hold']['channel'] = Number(frame, BUTTON_CHANNELS)
            button['hold']['channel'].onChange(lambda value, index=i : self._setButtonChannel(index, 'hold', value))
            button['hold']['channel'].grid(column=4, row=(i + 2), padx=3, pady=3, sticky='EW')

        frame.grid(column=0, row=1, sticky='S', padx=10, pady=10)
    
    def _setup_sliders_panel(self):
        frame = Fieldset(self, 'vSlider and Ext. Expr. Pedal')
        labels = ['vSlider', 'Ext. Expr. Pedal']

        # Frame 3 vSlider and Ext. Expr. Pedal
        for i, label in enumerate(SLIDER_LABELS):
            Label(frame, label).grid(column=(i + 1), row=1, sticky='W', padx=4)        

        for i, slider in enumerate(self.sliders):
            Label(frame, labels[i]).grid(column=0, row=(i + 2), sticky='W', padx=4)

            slider['mode'] = Number(frame, SLIDER_NUMBERS)
            slider['mode'].onChange(lambda value, index=i : self._setSliderMode(index, value))
            slider['mode'].grid(column=1, row=(i + 2), padx=3, pady=3, sticky='E')

            slider['control'] = Number(frame, SLIDER_CONTROLS)
            slider['control'].onChange(lambda value, index=i : self._setSliderControl(index, value))
            slider['control'].grid(column=2, row=(i + 2), padx=3, pady=3, sticky='E')

            slider['channel'] = Number(frame, SLIDER_CHANNELS)
            slider['channel'].onChange(lambda value, index=i : self._setSliderChannel(index, value))
            slider['channel'].grid(column=3, row=(i + 2), padx=3, pady=3, sticky='E')

        frame.grid(column=1, row=0, sticky='NS', padx=10, pady=10)

    def _setup_actions_panel(self):
        """ Setup actions panel """
        frame = Frame(self)

        self.actions['save'] = Button(frame, 'Save configuration', command=self.master.save)
        self.actions['save'].pack(side='left', fill='both', expand=True)
        self.actions['reload'] = Button(frame, 'Reload configuration', command=self.reload)
        self.actions['reload'].pack(side='left', fill='both', expand=True)
        self.actions['reset'] = Button(frame, 'Reset configuration', command=self.master.reset)
        self.actions['reset'].pack(side='left', fill='both', expand=True)
        frame.grid(column=1, row=1, sticky='WES', padx=10, pady=10)

    def enable(self):
        """ Enable all input widget """
        self.enableButtons()
        self.enableSliders()
        self.enableActions()
        
        return self
    
    def enableButtons(self):
        """ Enable all input buttons widget """
        for button in self.buttons:
            for event in button.values():
                [item.enable() for item in event.values()]

        self.refreshButtonsMode()

        return self

    def enableSliders(self):
        """ Enable all input sliders widget """
        for slider in self.sliders:
            [item.enable() for item in slider.values()]
        
        return self
    
    def enableActions(self):
        """ Enable all input actions widget """
        [action.enable() for action in self.actions.values()]

        return self
    
    def disable(self):
        """ Disable all input widget """
        self.disableButtons()
        self.disableSliders()
        self.disableActions()
        
        return self

    def disableButtons(self):
        """ Disable all input buttons widget """
        for button in self.buttons:
            for event in button.values():
                [item.disable() for item in event.values()]

        return self

    def disableSliders(self):
        """ Disable all input sliders widget """
        for slider in self.sliders:
            [item.disable() for item in slider.values()]
        
        return self
    
    def disableActions(self):
        """ Disable all input actions widget """
        [action.disable() for action in self.actions.values()]

        return self

    def reload(self):
        """ reload configuration """
        for i, button in enumerate(self.buttons):
            button['press']['mode'].set(BUTTON_FUNCTIONS[self.device.getButton(i, 'press', 'mode')])
            button['press']['program'].set(self.device.getButton(i, 'press', 'program'))
            button['press']['control'].set(self.device.getButton(i, 'press', 'control'))
            button['press']['channel'].set(self.device.getButton(i, 'press', 'channel'))
            
            button['hold']['mode'].set(BUTTON_FUNCTIONS[:-1][self.device.getButton(i, 'hold', 'mode')])
            button['hold']['program'].set(self.device.getButton(i, 'hold', 'program'))
            button['hold']['control'].set(self.device.getButton(i, 'hold', 'control'))
            button['hold']['channel'].set(self.device.getButton(i, 'hold', 'channel'))

        for i, slider in enumerate(self.sliders):
            slider['mode'].set(self.device.getSlider(i, 'mode'))
            slider['control'].set(self.device.getSlider(i, 'control'))
            slider['channel'].set(self.device.getSlider(i, 'channel'))

        self.refreshButtonsMode()

    def refreshButtonsMode(self):
        """ call changeButtonMode on all buttons """
        for i, button in enumerate(self.buttons):
            self._changeButtonMode(i, 'hold')
            self._changeButtonMode(i, 'press')
    
    def _changeButtonMode(self, index, event):
        """ enable or disable buttons based on some choices """
        button = self.buttons[index]
        value  = button[event]['mode'].get()        

        if value == 'Program Change':
            button[event]['control'].disable()
        elif value == 'Toggle CC':
            button[event]['control'].disable()
        else:
            button[event]['control'].enable()

        if event == 'press':
            if value == 'Tap':
                [e.disable() for e in button['hold'].values()]
            else:
                [e.enable() for e in button['hold'].values()]
                self._changeButtonMode(index, 'hold')

    def _setButtonMode(self, index, event, value):
        """ Set button mode """
        if event == 'press':
            value = BUTTON_FUNCTIONS.index(value)
        else:
            value = BUTTON_FUNCTIONS[:-1].index(value)
        
        self.device.setButton(index, event, 'mode', value)
        self._changeButtonMode(index, event)

    def _setButtonProgram(self, index, event, value):
        """ Set button program """
        self.device.setButton(index, event, 'program', value)        
    
    def _setButtonControl(self, index, event, value):
        """ Set button control """        
        self.device.setButton(index, event, 'control', value)        
    
    def _setButtonChannel(self, index, event, value):
        """ Set button channel """
        self.device.setButton(index, event, 'channel', value)        

    def _setSliderMode(self, index, value):
        """ Set slider mode """        
        self.device.setSlider(index, 'mode', value)

    def _setSliderControl(self, index, value):
        """ Set slider control """
        self.device.setSlider(index, 'control', value)        
    
    def _setSliderChannel(self, index, value):
        """ Set slider channel """
        self.device.setSlider(index, 'channel', value)
# supported boards
HW_VIDS = [5824, 9114]
HW_PIDS = [1161, 32780]

# buttons related constants
BUTTON_EVENTS = ['press', 'hold']
BUTTON_LABELS = ['Function', 'Number', 'CC Value', 'Midi Channel']
BUTTON_FUNCTIONS = ['Program Change', 'Momentary CC', 'Toggle CC', 'Tap']
BUTTON_NUMBERS  = ['%i' % i for i in range(128)]
BUTTON_CONTROLS = ['%i' % i for i in range(128)]
BUTTON_CHANNELS = ['%i' % (i + 1) for i in range(16)]

# sliders related constants
SLIDER_LABELS   = ['Continuos Control', 'CC For Effect Switch', '']
SLIDER_NUMBERS  = ['%i' % i for i in range(128)]
SLIDER_CONTROLS = ['%i' % i for i in range(128)]
SLIDER_CHANNELS = ['%i' % (i + 1) for i in range(16)]
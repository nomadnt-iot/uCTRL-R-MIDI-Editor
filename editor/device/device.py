from serial.tools import list_ports
from serial import Serial
from constants import BUTTON_EVENTS
from constants import HW_VIDS, HW_PIDS
import time
import struct

BUTTON_OPTIONS = ['mode', 'program', 'control', 'channel']
SLIDER_OPTIONS = ['mode', 'control', 'channel']

def list_devices():
    """ Return the list of avaiable device """
    devices = []
    for port in list(list_ports.comports()):
        if (port.vid in HW_VIDS) and (port.pid in HW_PIDS):
            devices.append({
                'name': '{} on {}'.format(port.product  or 'uCTRL-R-MIDI', port.device),
                'port': port.device
            })
    return devices

class Device:
    def __init__(self):
        self._serial = Serial(timeout=1)
        
        self._version = None

        self._buttons = [{
            'press': {'mode': 0, 'program': 0, 'control': 0, 'channel': 0},
            'hold':  {'mode': 0, 'program': 0, 'control': 0, 'channel': 0}
        } for _ in range(4)]

        self._sliders = [{
            'mode': 0, 'control': 0, 'channel': 0
        } for _ in range(2)]

        self._config = {}

    def connect(self, port, baudrate=9600):
        """ Connect to serial device """

        if not self.is_connected():
            self._serial.port = port
            self._baudrate = baudrate

            self._serial.open()
            #self._serial.flushInput()
            while self._serial.readline(): pass
        
        return self
    
    def disconnect(self):
        """ Disconnect from serial device """

        if self.is_connected():
            self._serial.close()

        return self

    def is_connected(self):
        """ return if device connected or not """
        return self._serial.is_open

    def save(self):
        """ save configuration to device """
        # for option, value in self._config.items():
        #     self.send('{}{}'.format(option, value))
        #     print(self.read())

        data = []
        for i in range(4):
            data.append(self._buttons[i]['press']['mode'])
            data.append(self._buttons[i]['press']['program'])
            data.append(self._buttons[i]['press']['control'])
            data.append(self._buttons[i]['press']['channel'])

            data.append(self._buttons[i]['hold']['mode'])
            data.append(self._buttons[i]['hold']['program'])
            data.append(self._buttons[i]['hold']['control'])
            data.append(self._buttons[i]['hold']['channel'])

        for i in range(2):
            data.append(self._sliders[i]['mode'])
            data.append(self._sliders[i]['control'])
            data.append(self._sliders[i]['channel'])

        # print(data)
        # print(struct.pack('4B4B4B4B4B4B4B4B3B3B', *data))
        self.send('S')
        self._serial.write(struct.pack('4B4B4B4B4B4B4B4B3B3B', *data))
        while True:
            # reading line
            line = self.read()

            print(line)

            # if 'Done' is find or no more lines on the buffer break
            if not line or line == 'Done': break

        return self

    def reset(self):
        """ Resetting device configuration """
        self.send('Z')
        # self._serial.flushInput()
        self.read()
        
        return self

    def load(self):
        """ Load configuration from device """
        self.send('Y')

        # unpacking data from device
        data = struct.unpack('<B4B4B4B4B4B4B4B4B3B3B', self._serial.read(39))

        # first element represent the firmware version
        self._version = data[0]

        index = e = o = 0
        for i, value in enumerate(data[1:33]):
            # switching option
            if i > 0 and i % 8 == 0: o += 1

            #print('button[{}][{}][{}]={}'.format(index, BUTTON_EVENTS[e], BUTTON_OPTIONS[o], value))
            self._buttons[index][BUTTON_EVENTS[e]][BUTTON_OPTIONS[o]] = value

            index += 1

            # switching event
            if index == 4: e ^= 1

            # resetting group counter
            if index == 4: index = 0

        index = e = o = 0
        for i, value in enumerate(data[33:]):
            # switching option
            if i > 0 and i % 2 == 0: o += 1

            #print('slider[{}][{}]={}'.format(index, SLIDER_OPTIONS[o], value))
            self._sliders[index][SLIDER_OPTIONS[o]] = value

            index += 1

            # resetting group counter
            if index == 2: index = 0

    
    def __load(self):
        """ Load configuration from device """
        self.send('Y')

        self._version = self.read()
        buttons = self.read()

        cursor = index = e = o = 0
        while True:
            # reading line
            line = self.read()

            # if 'Done' is find or no more lines on the buffer break
            if not line or line == 'Done': break

            # buttons configuration
            if cursor < 32:

                # switching option
                if cursor > 0 and cursor % 8 == 0: o += 1

                event = BUTTON_EVENTS[e]
                option = BUTTON_OPTIONS[o]

                # print('button[{}][{}][{}]={}'.format(index, event, option, int(line)))                
                self._buttons[index][event][option] = int(line)
                
                index += 1

                # switching event
                if index == 4: e ^= 1

                # resetting group counter
                if index == 4: index = 0

            # sliders configuration
            else:
                if cursor == 32: o = 0

                # switching option
                if cursor > 32 and cursor % 2 == 0: o += 1

                option = SLIDER_OPTIONS[o]
                
                #print('slider[{}][{}]={}'.format(index, option, int(line)))                
                self._sliders[index][option] = int(line)

                index += 1

                # resetting group counter
                if index == 2: index = 0
            
            cursor += 1

    def send(self, string):
        """ Send string to serial """
        self._serial.write(bytes(string, 'utf-8'))
    
    def read(self):
        """ Read line from serial buffer """
        return self._serial.readline().decode('utf-8').rstrip('\r\n')
        
    def dump(self):
        print(self._config)

    def getButton(self, index, event, option):
        """ getting button configuration """        
        return self._buttons[index][event][option]

    def setButton(self, index, event, option, value):
        """ setting button configuration """
        self._buttons[index][event][option] = int(value)
        self._encodeButton(index, event, option, value)
    
    def getSlider(self, index, option):
        """ getting slider configuration """
        return self._sliders[index][option]

    def setSlider(self, index, option, value):
        """ setting slider configuration """
        self._sliders[index][option] = int(value)
        self._encodeSlider(index, option, value)

    def _encodeButton(self, index, event, option, value):
        """ encoding button configuration """
        
        index = chr(index + 65)
        option = BUTTON_OPTIONS.index(option) * 2

        if event == 'hold': option += 1

        config = '{}{}{}'.format(option, index, value)

        self._config['{}{}'.format(option, index)] = value

    def _encodeSlider(self, index, option, value):
        """ encoding slider configuration """

        options = ['!', '@', '#']

        index = chr(index + 65)
        option = options[SLIDER_OPTIONS.index(option)]

        config = '{}{}{}'.format(option, index, value)

        self._config['{}{}'.format(option, index)] = value
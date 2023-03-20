# uCTRL Editor

## Windows

To start to develop  *uCTRL Editor* on windows operating system follow instructions:

- Download and install Python 3.7 https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe

- ```pip install -r requirements.txt```


### Using pyinstaller

#### Install Visual C++ 2015 Build Tools

- Download and install Visual C++ 2015 Build Tools http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe
- ```pyinstaller -F -w --add-data="../data/logo.jpg;data" --distpath="../bin" -n uCTRL-Editor editor.py```

# Serial Protocol

Function: [00]
Number:   [00000000]
Control:  [00000000]
Channel:  [0000]

[00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000]
[00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000]
[00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000]
[00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000] [00][00000000][00000000][0000]

[2][8][8][4] [2][8][8][4] [2][8][8][4] [2][8][8][4]
[2][8][8][4] [2][8][8][4] [2][8][8][4] [2][8][8][4]
[2][8][8][4] [2][8][8][4] [2][8][8][4] [2][8][8][4]
[2][8][8][4] [2][8][8][4] [2][8][8][4] [2][8][8][4]

[0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15]
[0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15]
[0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15]
[0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15] [0-3][0-127][0-127][0-15]

[0-127][0-127][0-15]
[0-127][0-127][0-15]

# new ProcessBuilder(current.currentDir + "/bin/avrdude" , "-C" , current.currentDir + "bin/avrdude.conf" , "-v" , /*"-patmega2560"*/ "-patmega32u4 " , "-cwiring" , "-P" + currentPortName , "-b115200" , "-D", "-U", "flash:w:" + filePath + ":i");

Button Press 0: [0A][2A][4A][6A]
Button Press 1: [0B][2B][4B][6B]
Button Press 2: [0C][2C][4C][6C]
Button Press 3: [0D][2D][4D][6D]

Button Hold 0:  [1A][3A][5A][7A]
Button Hold 1:  [1B][3B][5B][7B]
Button Hold 2:  [1C][3C][5C][7C]
Button Hold 3:  [1D][3D][5D][7D]

Slider 0: [!A][@A][#A]
Slider 1: [!B][@B][#B]

# buttons[0]['press']['mode']
# buttons[1]['press']['mode']
# buttons[2]['press']['mode']
# buttons[3]['press']['mode']
# buttons[0]['hold']['mode']
# buttons[1]['hold']['mode']
# buttons[2]['hold']['mode']
# buttons[3]['hold']['mode']
# buttons[0]['press']['pc']
# buttons[1]['press']['pc']
# buttons[2]['press']['pc']
# buttons[3]['press']['pc']
# buttons[0]['hold']['pc']
# buttons[1]['hold']['pc']
# buttons[2]['hold']['pc']
# buttons[3]['hold']['pc']
# buttons[0]['press']['cc']
# buttons[1]['press']['cc']
# buttons[2]['press']['cc']
# buttons[3]['press']['cc']
# buttons[0]['hold']['cc']
# buttons[1]['hold']['cc']
# buttons[2]['hold']['cc']
# buttons[3]['hold']['cc']
# buttons[0]['press']['ch']
# buttons[1]['press']['ch']
# buttons[2]['press']['ch']
# buttons[3]['press']['ch']
# buttons[0]['hold']['ch']
# buttons[1]['hold']['ch']
# buttons[2]['hold']['ch']
# buttons[3]['hold']['ch']

# sliders[0]['ctrl]
# sliders[1]['ctrl']
# sliders[0]['cc']
# sliders[1]['cc']
# sliders[0]['ch']
# sliders[1]['ch']


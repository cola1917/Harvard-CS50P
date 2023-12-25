from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fontList = figlet.getFonts()
font = fontList[0]

def error():
    print('Invalid usage')
    sys.exit(1)

if len(sys.argv) == 1:
    font = random.choice(fontList)
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fontList:
            font = sys.argv[2]
        else:
            error()
    else:
        error()
else:
    error()
s = input('Input: ')
figlet.setFont(font=font)
print('Output:' + figlet.renderText(s))

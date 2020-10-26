#! python3
# mapIt.py запускает карту в браузере, извлекает почтовый адрес из командной строки или буферма обмена.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


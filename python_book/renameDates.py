'''Переименовать файлы, имена которых включают даты, указанные в американском формате (ММ-ДД-ГГГГ), приводя
их в соответствие с европейским форматом дат (ДД-ММ-ГГГГ)'''

import shutil, os, re

datePattern = re.compile(r"""^(.*?) #group(1)
    ((0|1)?\d)-                     #group(2) group(3)
    ((0|1|2|3)?\d-                  #group(4) group(5)
    ((19|20)\d\d)                   #group(6) group(7)
    (.*?)$                          #group(8)
    """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print('Заменяем имя "%s" именем "%s"...'
          % (amerFilename, euroFilename))
# shutil.move(amerFilename, euroFilename) # раскомментировать
# после выполнения
# тестирования

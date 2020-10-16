import os, zipfile, re

pdf = re.compile(r'(\w)+(\.)(pdf|jpg)')

for foldername, subfolder, filename in os.walk('C:\\Users'):
    mo = pdf.search(str(filename))
    print(mo.groups())

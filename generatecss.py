import os
from fontTools import ttLib

cssContent = ''
for filename in os.listdir():
    if filename.lower().endswith('.ttf') or filename.lower().endswith('.otf'):
        names = (ttLib.TTFont(filename)['name'].names)
        details = {}
        for x in names:
            if x.langID == 0 or x.langID == 1033:
                try:
                    details[x.nameID] = x.toUnicode()
                except UnicodeDecodeError:
                    details[x.nameID] = x.string.decode(errors='ignore')

        cssContent += '''
@font-face {
font-family: ''' + "'" + details[1] + "'" + ''';
src: url('https://cdn.jsdelivr.net/gh/virtualvinodh/aksharamukha-fonts/''' + filename + "'" + ''')
}
'''

with open('aksharamukha-fonts.css', 'w') as f:
    f.write(cssContent)

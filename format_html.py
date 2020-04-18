EOL_TAG = '<br />\n'

FILENAME = 'about.html'
FILE_PATH = 'templates/' + FILENAME
NEW_FILE = ''

with open(FILE_PATH, encoding='utf8') as f:
    is_par = False
    for line in f.readlines():
        if '<p>' in line:
            is_par = True
        if '</p>' in line:
            is_par = False
        if is_par and line and EOL_TAG not in line:
            line = line.replace('\n', '') + EOL_TAG
        if line:
            NEW_FILE += line.replace('\n', '') + '\n'

print(NEW_FILE)
with open(FILE_PATH, 'w', encoding='utf8') as f:
    f.write(NEW_FILE)

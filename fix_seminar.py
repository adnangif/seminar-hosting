import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the exact span containing SEMINAR
text = text.replace('<span>SEMINAR<\\u002Fspan>', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

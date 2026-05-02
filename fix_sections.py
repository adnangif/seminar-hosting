import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to match <span class=\"sec\">§ ...<\u002Fspan>
pattern = r'<span class=\\"sec\\">§.*?<\\u002Fspan>'
text = re.sub(pattern, '', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

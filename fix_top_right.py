with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('SEMINAR · 2026', '2026')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

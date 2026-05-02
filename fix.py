import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. replace MSC AI, 
text = text.replace('SEMINAR · MSC AI · 2026', 'SEMINAR · 2026')

# 2. remove "servey" from top right
text = text.replace('<span>SURVEY<\\u002Fspan>', '')

# 3. remove "Based on 10 sources, 5 frameworks"
# We need to remove the whole block:
#         <div>\n          <div class=\"title-meta\" style=\"margin-bottom: 8px;\">Based on<\\u002Fdiv>\n          <div class=\"title-author\" style=\"font-style: italic;\">10 sources, 5 frameworks<\\u002Fdiv>\n        <\\u002Fdiv>
pattern_based_on = r'<div>\\n\s*<div class=\\"title-meta\\" style=\\"margin-bottom: 8px;\\">Based on<\\u002Fdiv>\\n\s*<div class=\\"title-author\\" style=\\"font-style: italic;\\">10 sources, 5 frameworks<\\u002Fdiv>\\n\s*<\\u002Fdiv>'
text = re.sub(pattern_based_on, '', text)

# 4. replace "khulna university * Msc seminar" with "MSc. 260204"
text = text.replace('Khulna University · MSc Seminar', 'MSc. 260204')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

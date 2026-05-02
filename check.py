with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("SEMINAR:", "SEMINAR · MSC AI · 2026" in text)
print("SURVEY:", text.find("SURVEY<"))
print("Based on:", text.find("10 sources, 5 frameworks"))
print("Khulna:", text.find("Khulna University · MSc Seminar"))
print("MSc. 260204:", text.find("MSc. 260204"))

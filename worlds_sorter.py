with open('dict/russian_nouns_five.txt', 'r') as f:
    lines = f.readlines()
    lines.sort()

with open('dict/russian_nouns_five.txt', 'w') as f:
    f.writelines(lines)
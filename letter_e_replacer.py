with open("dict/russian_nouns_five.txt", "r") as f:
    file_content = f.read()

file_content = file_content.replace("ё", "е")

with open("dict/russian_nouns_five.txt", "w") as f:
    f.write(file_content)
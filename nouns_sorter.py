with open("dict/russian_nouns.txt", "r") as f:
    nouns = f.readlines()

five_letter_nouns = filter(lambda x: len(x.strip()) == 5, nouns)

with open("dict/russian_nouns_five.txt", "w") as f:
    f.writelines(five_letter_nouns)
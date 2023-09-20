# ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗  ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗
# ██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
# ██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║  ╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░
# ╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║  ░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
# ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║  ██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
# ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

file_paths = [
    './dict/russian/russian_nouns_4.txt',
    './dict/russian/russian_nouns_5.txt',
    './dict/russian/russian_nouns_6.txt',
    './dict/russian/russian_nouns_7.txt',
    './dict/russian/russian_nouns_8.txt',
    './dict/russian/russian_nouns_9.txt',
    './dict/russian/russian_nouns_10.txt',
    './dict/russian/russian_nouns_11.txt'
]

for file_path in file_paths:
    with open(file_path, "r") as f:
        file_content = f.read()

    file_content = file_content.replace("ё", "е")

    with open(file_path, "w") as f:
        f.write(file_content)

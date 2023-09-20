# ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗  ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗
# ██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
# ██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║  ╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░
# ╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║  ░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
# ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║  ██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
# ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝



import configparser

# Функция для создания и настройки файла конфигурации
def create_config_file(word_length):
    config = configparser.ConfigParser()

    config['Settings'] = {
        'DictionaryPath': f'dict/russian/russian_nouns_{word_length}.txt',
        'ValidCharacters': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ',
        'WordLength': str(word_length),
        'WordsToRemove': 'clint,garbo,galen,abner'
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

while True:
    # Спрашиваем пользователя о количестве букв
    print("Сколько букв в вашем слове?")
    print("Выберите длину слова (от 4 до 11):")
    word_length = int(input())

    if word_length < 4 or word_length > 11:
        print("Недопустимая длина слова. Выберите от 4 до 11 букв.")
    else:
        with open(f'dict/russian/russian_nouns_{word_length}.txt', 'w') as f:
            # Здесь можно добавить код для наполнения файла словами нужной длины
            pass

        create_config_file(word_length)
        print(f"Настройки изменены. Теперь выбрана длина слова: {word_length}")
        break


# ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗  ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗
# ██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
# ██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║  ╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░
# ╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║  ░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
# ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║  ██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
# ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

import configparser
import sys

# Чтение файла конфигурации
config = configparser.ConfigParser()
config.read('config.ini')

# Извлечение настроек из файла конфигурации
dictpath = config.get('Settings', 'DictionaryPath')
validchars = config.get('Settings', 'ValidCharacters')
wordlength = config.getint('Settings', 'WordLength')
wordstoremove = config.get('Settings', 'WordsToRemove').split(',')

# Проверка аргументов командной строки
if len(sys.argv) > 1:  
    dictpath = sys.argv[1]

# Чтение и обработка словаря
allwords = open(dictpath, "r").read().split('\n')
validwords = set()

for w in allwords:
    if ("'" in w): continue
    if (len(w) != wordlength): continue
    for i in range(wordlength + 1):
        if (i < wordlength and w[i] not in validchars): break
        elif (i == wordlength): validwords.add(w.lower())

# Удаление определенных слов
for word in wordstoremove:
    validwords.discard(word)

# Преобразование в список
validwords = list(validwords)

def isThisSecretAvailable(testword,mask,secret):
    '''
    mask: G,Y,N -- зеленый, желтый, отсутствует
    Возвращает True, если секретное слово может быть секретным словом с этим тестовым словом и маской
    '''
    for i in range(len(mask)):
        if(mask[i]=='N' and testword[i] not in secret):continue
        if(mask[i]=='G' and testword[i]==secret[i]):continue
        if(mask[i]=='Y' and testword[i] in secret and testword[i]!=secret[i]):continue
        return False
    return True

def getMask(testword,secret):
    '''
    Возвращает маску из символов NYG для введенного тестового слова и секретного слова
    '''
    mask=""
    for i in range(len(testword)):
        if(testword[i]==secret[i]):mask+="G"
        elif(testword[i] in secret):mask+="Y"
        else:mask+="N"
    return mask

def getAvailableWordsByMask(testword,mask,wordlist):
    '''
    Возвращает список доступных слов для введенного тестового слова и маски
    '''
    validsecrets=[]
    for w in wordlist:
        if(isThisSecretAvailable(testword,mask,w)):
            validsecrets.append(w)
    return validsecrets

# Получить больше различий в начальном шаге

print("Анализ словаря ("+str(len(validwords))+" слов)...")

testwordmasks=dict() # Сделаем словарь: слово -> множество возможных масок
for i in validwords:
    testwordmasks[i]=set()
    for s in validwords:
        testwordmasks[i].add(getMask(i,s))

masksvariances=[] # Сделаем список с информацией о количестве разных масок
for i in validwords:
    masksvariances.append(len(testwordmasks[i]))

maxmasksvariances=max(masksvariances)
maxvariancewords1=[]
for i in range(len(validwords)):
    if(masksvariances[i]==maxmasksvariances):
        print(validwords[i])
        maxvariancewords1.append(validwords[i])


def getBestSteps(wordlist,allwords=None):
    '''
    Получить лучший шаг для поиска слова в списке wordlist с использованием словаря allwords
    Режим Hard включен, если allwords=None или allwords=wordlist
    '''
    if(allwords is None):
        allwords=wordlist
    testwordmasks=dict()
    for i in allwords:
        testwordmasks[i]=set()
        for s in wordlist:
            testwordmasks[i].add(getMask(i,s))
    masksvariances=[]
    for i in allwords:
        masksvariances.append(len(testwordmasks[i]))
    maxmasksvariances=max(masksvariances)
    print("Различные маски:",maxmasksvariances)
    maxvariancewords=[]
    maxvariancewords2=[]
    maxvariancewords3=[]
    for i in range(len(allwords)):
        if(masksvariances[i]==maxmasksvariances):
            print(allwords[i])
            maxvariancewords.append(allwords[i])
            if(maxmasksvariances==1):break
        elif(masksvariances[i]==maxmasksvariances-1):
        # На случай, если в maxvariancewords будет всего одно слово и его не будет в словаре игры
            maxvariancewords2.append(allwords[i])
        elif(masksvariances[i]==maxmasksvariances-2):
            maxvariancewords3.append(allwords[i])
    # Среди лучших вариантов я бы поставил на первое место те, в которых буквы не повторяются
    maxvariancewords.sort(key=lambda x:-len(set(x)))
    maxvariancewords2.sort(key=lambda x:-len(set(x)))
    maxvariancewords3.sort(key=lambda x:-len(set(x)))
    return maxvariancewords+maxvariancewords2+maxvariancewords3

def mainloop():
    print("Введите одно из следующих слов:",maxvariancewords1,"("+str(maxmasksvariances)+" разных масок)")
    newwordlist=getAvailableWordsByMask(input("Какое слово вы ввели: ").lower(),input("Какую маску вы получили: ").upper(),validwords)
    print("Найдено",len(newwordlist),"доступных слов")
    beststeps=getBestSteps(newwordlist,validwords)
    if(len(beststeps)>7):beststeps=beststeps[:7]
    print("Пожалуйста, введите одно из следующих слов:",beststeps)
    while(len(newwordlist)>1):
        newwordlist=getAvailableWordsByMask(input("Какое слово вы ввели: ").lower(),input("Какую маску вы получили: ").upper(),newwordlist)
        print("Найдено",len(newwordlist),"доступных слов")
        if(len(newwordlist)==1):break
        beststeps=getBestSteps(newwordlist,validwords)
        if(len(beststeps)>7):beststeps=beststeps[:7]
        print("Пожалуйста, введите одно из следующих слов:",beststeps)
    print("Ваше слово:",newwordlist)

if(__name__=="__main__"):
    mainloop()

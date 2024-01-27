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
dictpath = config.get('Worlde', 'DictionaryPath')
validchars = config.get('Worlde', 'ValidCharacters')
wordlength = config.getint('Worlde', 'WordLength')
wordstoremove = config.get('Worlde', 'WordsToRemove').split(',')

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
	mask: G,Y,N -- green, yellow, none
	Return True if secret can be secret word with this testword and mask
	'''
	for i in range(len(mask)):
		if(mask[i]=='N' and testword[i] not in secret):continue
		if(mask[i]=='G' and testword[i]==secret[i]):continue
		if(mask[i]=='Y' and testword[i] in secret and testword[i]!=secret[i]):continue
		return False
	return True

def getMask(testword,secret):
	'''
	Returns mask of NYG symbols for typed testword and secretword
	'''
	mask=""
	for i in range(len(testword)):
		if(testword[i]==secret[i]):mask+="G"
		elif(testword[i] in secret):mask+="Y"
		else:mask+="N"
	return mask

def getAvailableWordsByMask(testword,mask,wordlist):
	'''
	Return list of available words by typed testword and mask
	'''
	validsecrets=[]
	for w in wordlist:
		if(isThisSecretAvailable(testword,mask,w)):
			validsecrets.append(w)
	return validsecrets

# Get more difference start step

print("Analyze dictionary ("+str(len(validwords))+" words)...")

testwordmasks=dict() # Сделаем словарь: слово -> множество возможных масок
for i in validwords:
	testwordmasks[i]=set()
	for s in validwords:
		testwordmasks[i].add(getMask(i,s))

masksvariances=[] # Сделаем лист с информацией о количестве разных масок
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
	Get best step for find word in wordlist by allwords dictionary
	HardMode on if allwords=None or allwords=wordlist
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
	print("Different masks:",maxmasksvariances)
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
	print("Enter one of next words:",maxvariancewords1,"("+str(maxmasksvariances)+" different masks)")
	newwordlist=getAvailableWordsByMask(input("What word did you type: ").lower(),input("What mask did you get: ").upper(),validwords)
	print("Found",len(newwordlist),"available words")
	beststeps=getBestSteps(newwordlist,validwords)
	if(len(beststeps)>7):beststeps=beststeps[:7]
	print("Please, type one of next words:",beststeps)
	while(len(newwordlist)>1):
		newwordlist=getAvailableWordsByMask(input("What word did you type: ").lower(),input("What mask did you get: ").upper(),newwordlist)
		print("Found",len(newwordlist),"available words")
		if(len(newwordlist)==1):break
		beststeps=getBestSteps(newwordlist,validwords)
		if(len(beststeps)>7):beststeps=beststeps[:7]
		print("Please, type one of next words:",beststeps)
	print("Your word is",newwordlist)

if(__name__=="__main__"):
	mainloop()

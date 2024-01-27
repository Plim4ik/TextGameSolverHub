# ░██████╗░██╗░░░██╗░█████╗░███╗░░██╗████████╗██╗░░░██╗███╗░░░███╗  ░██████╗████████╗░█████╗░░█████╗░██╗░░██╗
# ██╔═══██╗██║░░░██║██╔══██╗████╗░██║╚══██╔══╝██║░░░██║████╗░████║  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
# ██║██╗██║██║░░░██║███████║██╔██╗██║░░░██║░░░██║░░░██║██╔████╔██║  ╚█████╗░░░░██║░░░███████║██║░░╚═╝█████═╝░
# ╚██████╔╝██║░░░██║██╔══██║██║╚████║░░░██║░░░██║░░░██║██║╚██╔╝██║  ░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
# ░╚═██╔═╝░╚██████╔╝██║░░██║██║░╚███║░░░██║░░░╚██████╔╝██║░╚═╝░██║  ██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
# ░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝


from collections import Counter
import sys
import time

# Use: python AnagramFinder.py [letters without space]
# Example: python3 AnagramFinder.py битдеа

with open('dict/russian_nouns.txt', 'r') as f:
    dictionary = f.read()

dictionary = [x.lower() for x in dictionary.split('\n')]


def return_anagrams(letters: str) -> list:
    global dictionary

    assert isinstance(letters, str), 'Scrambled letters should only be of type string.'

    letters = letters.lower()

    letters_count = Counter(letters)

    anagrams = set()
    for word in dictionary:
        # Check if all the unique letters in word are in the scrambled letters
        if not set(word) - set(letters):
            check_word = set()
            # Check if the count of each letter is less than or equal
            # to the count of that letter in scrambled letter input
            for k, v in Counter(word).items():
                if v <= letters_count[k]:
                    check_word.add(k)
            # Check if check_words is exactly equal to the unique letters
            # in the word of the dictionary
            if check_word == set(word):
                anagrams.add(word)

    # Check if the empty string is in the set before attempting to remove it
    if '' in anagrams:
        anagrams.remove('')

    return sorted(list(anagrams), key=lambda x: len(x))



if __name__ == '__main__':
    start = time.time()
    test_anagrams = return_anagrams(sys.argv[1])
    print(test_anagrams)
    stop = time.time()
    print(f"Number of anagrams: {len(test_anagrams)}")
    print(f"Time Taken: {round(stop - start, 5)} seconds")
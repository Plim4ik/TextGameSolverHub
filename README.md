# 🎮 TextGameSolverHub

## 📂 Repository Description:

TextGameSolverHub is a collection of Python scripts designed to solve various text-based games. These scripts utilize algorithms and strategies to decipher and solve word-related challenges in games like Wordle, Words of Wonders (WoW), and similar text-based puzzles.

## 🎮 Supported Games:

The repository currently provides solutions for the following games:

1. **Wordle:** A popular word puzzle game where players attempt to guess a secret word within a limited number of attempts.

2. **Words of Wonders (WoW):** A game that combines word search and crossword puzzle elements, challenging players to find hidden words based on provided clues.

Feel free to explore the scripts and enhance the repository with additional solutions for other text-based games!

## 🚀 Usage Instructions:

### AnagramFinder (WoW)

Use the following command to run AnagramFinder for Words of Wonders:

```bash
python AnagramFinder.py [letters without space]
```

Example:

```bash
python3 AnagramFinder.py битдеа
```

### WorldeSolver (Wordle)

Use the following command to run WorldeSolver for Wordle:

```bash
python WorldeSolver.py
```

Example:

```bash
# Analyze dictionary (12970 words)...
tares
Enter one of the next words: ['tares'] (212 different masks)
What word did you type: tares
What mask did you get: nyngy
# Here, 'n' represents the absence of the letter in the word (None),
# 'g' represents the correct letter in the correct position (Green),
# 'y' represents the correct letter in the wrong position (Yellow).
```

## 🌍 Available Languages (9)
| Language Name   | Native Language Name   |   Number of Words | Word File           |
|-----------------|------------------------|-------------------|---------------------|
| Swedish         | Svenska                |            403791 | dict/Swedish.txt    |
| Turkish         | Türkçe                 |             60450 | dict/Turkish.txt    |
| Russian         | Русский язык           |             51304 | dict/Russian.txt    |
| French          | Français               |            336528 | dict/French.txt     |
| English         | English                |             12973 | dict/English.txt    |
| Spanish         | Español                |            559801 | dict/Spanish.txt    |
| Italian         | Italiano               |           1707903 | dict/Italian.txt    |
| Portuguese      | Português              |           1108873 | dict/Portuguese.txt |
| Polish          | Polski                 |           4075605 | dict/Polish.txt     |

## 🛠️ Installation

1. Clone this repository to your computer using the following command:

```bash
git clone https://github.com/Plim4ik/TextGameSolverHub.git
```

2. Install all necessary dependencies:

```bash
cd TextGameSolverHub
pip install -r requirements.txt
```

## ⚙️ Configuration

### Worlde

- **DictionaryPath**: Path to the dictionary file for Wordle. Example: `dict/Russian.txt`
- **ValidCharacters**: Valid characters that can be used in words for Wordle. Example: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`
- **WordLength**: The length of words to solve in Wordle. Example: `5`
- **WordsToRemove**: Words to remove from the dictionary for Wordle. Example: `clint,abner`

### AnagramFinder

- **DictionaryPath**: Path to the dictionary file for AnagramFinder. Example: `dict/Russian.txt`
- **MinLength**: The minimum length of words to consider in AnagramFinder. Example: `3`

## ➕ Adding New Words

To add new words to the dictionary, open the dictionary file in a text editor and add each new word on a new line. Remember that all words should be written in lowercase and should not contain spaces or special characters.
word: str = input()

def palindromo(word: str):
    letters = list()
    for letter in word:
        letters.append(letter)
    new_word = list()
    for letter in range(len(letters)-1, -1, -1):
        new_word.append(letters[letter])
    if new_word == letters:
        return True
    else:
        return False

print(palindromo(word))

def Anagrama():
    list_word = list(map(str, input("Ingrese palabras: ").split()))
    anagram = []
    for i in range(len(list_word)):
        base = sorted(list_word[i])
        grupo = []
        for palabra in list_word:
            if sorted(palabra) == base:
                grupo.append(palabra)
        if len(grupo) > 1 and grupo not in anagram:
            anagram.append(grupo)
    return anagram

print(Anagrama())

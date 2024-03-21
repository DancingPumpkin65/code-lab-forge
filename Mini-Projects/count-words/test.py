def count_words(path, word):
    # Link file path - variable
    PR = open(path, "r")
    prg = PR.read()

    # Uppercase to lowercase
    prg1 = prg.lower()
    word1 = word.lower()
    s = 0

    # RegEx / Regular Expression
    import re
    words = re.findall(r'\w+', prg1) 

    # Count 
    s = words.count(word1)
    
    print(f"le nombre d'apparition du mot '{word}' est: {s} fois")

# Exemple
count_words("D:\\Documents\\DEV101\\Khalid Okaidi\\Algorithme-Python\\Series\\Série4\\daw.txt", "specifiedWord")

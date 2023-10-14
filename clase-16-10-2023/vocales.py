texto = "aeiouu"
vocales = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for letra in texto:
    if letra in vocales:
        vocales[letra] +=1
print(vocales)
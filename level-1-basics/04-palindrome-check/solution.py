texto = str(input("frase: ")).strip().lower()

invertido = ""

for char in texto:
    invertido = char + invertido

if texto == invertido:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
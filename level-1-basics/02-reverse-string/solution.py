texto = str(input("frase: "))
invertido = ""

tamanho = len(texto)

for i in range(tamanho-1, -1, -1):
    invertido += texto[i]

print(invertido)
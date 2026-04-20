texto = str(input("frase: "))

vogais = "aeiou"
count = 0
for char in texto:
    if char.lower() in vogais:
        count += 1

print("QTD de vogais:", count)
numero = str(input("numero: ")).strip()

if not numero.isdigit():
    print("Por favor, insira um número válido.")
    exit()

soma = 0

for i in numero:
    soma += int(i)

print(f"A soma dos dígitos é: {soma}")
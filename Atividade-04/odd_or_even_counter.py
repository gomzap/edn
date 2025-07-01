pares = []
impares = []

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

    if entrada.lower() == 'encerrar':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'encerrar'.")

# Resultados
print("\nAnálise dos números:")
print(f"Números pares ({len(pares)}): {pares}")
print(f"Números ímpares ({len(impares)}): {impares}")
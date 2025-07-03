def calcular_desconto():
    try:
        # Interação com o usuário
        preco_original = float(input("Digite o preço original do produto: R$ "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

        # Cálculo do valor do desconto
        valor_desconto = preco_original * (porcentagem_desconto / 100)

        # Cálculo do preço final
        preco_final = preco_original - valor_desconto

        # Formatação para 2 casas decimais
        preco_final_formatado = round(preco_final, 2)
        valor_desconto_formatado = round(valor_desconto, 2)

        print(f"\nDesconto aplicado: R$ {valor_desconto_formatado}")
        print(f"Preço final com desconto: R$ {preco_final_formatado}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Executa a função
calcular_desconto()
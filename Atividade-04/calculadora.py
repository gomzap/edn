def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao not in ('+', '-', '*', '/'):
                raise ValueError("Operação inválida.")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero.")
                resultado = num1 / num2

            print(f"Resultado: {resultado}")
            break

        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, tente novamente.\n")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Por favor, tente novamente.\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}\n")

calculadora()

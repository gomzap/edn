def converter_temperatura(valor, origem, destino):
    if origem == destino:
        return valor

    # Convertendo para Celsius
    if origem == "F":
        valor = (valor - 32) * 5/9
    elif origem == "K":
        valor = valor - 273.15

    # Convertendo de Celsius para destino
    if destino == "F":
        return (valor * 9/5) + 32
    elif destino == "K":
        return valor + 273.15
    else:
        return valor

print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

if origem not in ["C", "F", "K"] or destino not in ["C", "F", "K"]:
    print("Unidade inválida. Use C, F ou K.")
else:
    resultado = converter_temperatura(temp, origem, destino)
    print(f"{temp}°{origem} equivale a {resultado:.2f}°{destino}")
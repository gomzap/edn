import re

def verifica_palindromo():
    texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    texto_limpo = re.sub(r'[^A-Za-z0-9]', '', texto).lower()
    if texto_limpo == texto_limpo[::-1]:
        print("Sim")
    else:
        print("Não")

verifica_palindromo()

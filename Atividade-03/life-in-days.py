from datetime import datetime

def idade_em_dias(ano, mes, dia):

    hoje = datetime.now()
    nascimento = datetime(ano, mes, dia)
    diferenca = hoje - nascimento
    return diferenca.days

ano = int(input("Digite o ano de nascimento (ex: 1999): "))
mes = int(input("Digite o mês de nascimento (1 a 12): "))
dia = int(input("Digite o dia de nascimento (1 a 31): "))

dias_de_vida = idade_em_dias(ano, mes, dia)
print(f"Essa pessoa tem aproximadamente {dias_de_vida} dias de vida.")
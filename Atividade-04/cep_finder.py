import requests

def consultar_cep(cep):
    try:
        dados = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
        return None if 'erro' in dados else dados
    except:
        return None

def main():
    print("Consulta de CEP - ViaCEP\n-----------------------")
    while True:
        cep = input("\nCEP (8 dígitos) ou 'sair': ").strip()
        if cep.lower() == 'sair': break
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido! Digite 8 números.")
            continue
            
        dados = consultar_cep(cep)
        if dados:
            print(f"""
            Endereço:
            Logradouro: {dados.get('logradouro', 'Não informado')}
            Bairro: {dados.get('bairro', 'Não informado')}
            Cidade: {dados.get('localidade', 'Não informado')}
            Estado: {dados.get('uf', 'Não informado')}""")
            
        if input("\nNova consulta? (s/n): ").lower() != 's': break

if __name__ == "__main__":
    main()
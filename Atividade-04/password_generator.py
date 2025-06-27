import random
import string

def gerar_senha(n):
    chars = string.ascii_letters + string.digits + '!@#$%&*()-_=+[]{}^~;:,.<>/?'
    senha = [random.choice(string.ascii_lowercase),
             random.choice(string.ascii_uppercase),
             random.choice(string.digits),
             random.choice('!@#$%&*()-_=+[]{}^~;:,.<>/?')] + \
            [random.choice(chars) for _ in range(n-4)]
    random.shuffle(senha)
    return ''.join(senha)

def main():
    print("Gerador de Senhas Seguras\n-------------------------")
    while True:
        try:
            n = int(input("\nComprimento da senha (mínimo 8): "))
            if n < 8:
                print("Mínimo 8 caracteres!")
                continue
            print(f"\nSenha: {gerar_senha(n)}\nTamanho: {n} caracteres")
            if input("\nNova senha? (s/n): ").lower() != 's': break
        except ValueError:
            print("Digite um número válido!")

if __name__ == "__main__":
    main()
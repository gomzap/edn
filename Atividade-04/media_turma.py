notas = []
quantidade = int(input("Quantos alunos na turma? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas dos alunos:")
for i, nota in enumerate(notas, start=1):
    print(f"Aluno {i}: {nota}")

print(f"\nMédia da turma: {media:.2f}")
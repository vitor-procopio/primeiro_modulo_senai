#-------------------------------------------------------------------------------------------------------
# Inicializando variáveis
notas = []

# Loop para receber as 4 notas do aluno
for bimestre in range(1, 5):
    nota = float(input(f'Digite a nota do {bimestre}º bimestre: '))
    notas.append(nota)
    print(f'Nota {nota} armazenada com sucesso!')

# Calculando a média
media = sum(notas) / len(notas)

# Mostrando resultado
print(f'A média do aluno é {media:.2f}')
#-------------------------------------------------------------------------------------------------------
"""O for ... in range(...) é usado para repetir um bloco de código um número específico de vezes."""
# for i in range("início, fim, passo"):
#      código a repetir
# início → valor inicial (opcional, padrão é 0)

# fim → valor onde para antes de chegar (não inclui o fim)

# passo → quanto aumenta a cada repetição (opcional, padrão é 1)
#-------------------------------------------------------------------------------------------------
# Média com while
# 'nota_total' é o acumulador de notas
nota_total = 0
bimestre = 0

while bimestre < 4:
    nota = float(input('Digite a nota do aluno: '))
    nota_total += nota  # Acumulando a nota total
    bimestre += 1
    print(f'A {nota} digitada do aluno foi armazenada com sucesso!')

media = nota_total / 4  # Calculando a média após sair do loop
print(f'A média do aluno é {media}')
#-------------------------------------------------------------------------------------------------


"""notas de 4 bimestres. Vamos entender cada parte: 

1. Preparando o Terreno:

Python

nota_total = 0
bimestre = 0
nota_total = 0: Cria uma variável chamada nota_total e começa ela com o valor zero. Essa variável vai guardar a soma de todas as notas que você digitar.

bimestre = 0: Cria outra variável, bimestre, também começando do zero. Ela vai servir como um contador para saber em qual bimestre o código está no momento.

2. O Loop (A Repetição):

Python

while bimestre < 4:
while bimestre < 4:: Esta é a parte que cria um loop, ou seja, um bloco de código que vai se repetir. A instrução while (enquanto, em inglês) diz: "enquanto a variável bimestre for menor que 4, continue executando as linhas de código que estão aqui dentro". Como a gente quer 4 notas (uma para cada bimestre), o loop vai rodar 4 vezes.

3. O que acontece dentro do Loop:

Python

    nota = float(input('Digite a nota do aluno: '))
    nota_total += nota  # Acumulando a nota total
    bimestre += 1
    print(f'A {nota} digitada do aluno foi armazenada com sucesso!')
nota = float(input('Digite a nota do aluno: ')): Pede para você, usuário, digitar a nota. O input() mostra a mensagem na tela. O float() é importante porque ele converte o que você digitou (que vem como texto) para um número com casas decimais (como 8.5 ou 7.0), o que é essencial para fazer o cálculo depois.

nota_total += nota: Esta é uma forma curta de dizer nota_total = nota_total + nota. A cada vez que o loop roda, a nota que você acabou de digitar é somada à variável nota_total. Assim, no final, essa variável terá a soma de todas as notas.

bimestre += 1: Outra forma curta de dizer bimestre = bimestre + 1. A cada volta do loop, esse contador aumenta em 1. Quando ele chegar a 4, a condição do while (bimestre < 4) deixa de ser verdadeira e o loop é encerrado.

print(f'A {nota} digitada do aluno foi armazenada com sucesso!'): Mostra uma mensagem na tela para você saber que a nota foi guardada. O f' ' (chamado de f-string) permite que você coloque o valor da variável nota diretamente na frase.

4. A Saída do Loop e o Resultado Final:

Python

media = nota_total / 4  # Calculando a média após sair do loop
print(f'A média do aluno é {media}')
Quando o loop termina (após 4 repetições), o código continua a partir daqui.

media = nota_total / 4: Calcula a média, pegando a nota_total (que já tem a soma das 4 notas) e dividindo por 4.

print(f'A média do aluno é {media}'): Por fim, exibe o resultado da média na tela."""
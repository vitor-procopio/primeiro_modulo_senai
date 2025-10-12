#imprimir numeros pares até o numero digitado pelo usuario
x = 0
numero_par = int(input('Digite um número par: '))

while x < numero_par:
    x += 2
    print(x)
# O while é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.

# Sintaxe básica:

# while condição:
#     # código que será repetido


# A condição é testada antes de cada repetição.

# Se a condição for True, o código dentro do while roda.

# Quando a condição virar False, o loop para.

# Exemplo simples:

# contador = 1
# while contador <= 5:
#     print(contador)
#     contador += 1


# Saída:

# 1
# 2
# 3
# 4
# 5


# 💡 Explicação do exemplo:

# contador começa em 1.

# Enquanto contador <= 5, o loop roda.

# Cada vez que roda, soma 1 ao contador.

# Quando contador chega a 6, a condição contador <= 5 é False, e o loop termina.

# O while é útil quando não sabemos exatamente quantas vezes o código vai rodar, diferente do for, que normalmente sabemos o número de repetições.
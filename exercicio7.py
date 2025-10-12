""""For i in range" é uma construção em Python que cria um loop para executar um bloco de código um número específico de vezes. A função range() gera uma sequência de números inteiros, e para cada número dessa sequência (atribuído à variável i a cada iteração), o código dentro do loop é executado. 
Como funciona
1. for:
É a palavra-chave que inicia um loop, indicando que o código a seguir será repetido. 
2. i:
É uma variável que receberá o valor de cada número da sequência range() em cada repetição do loop. Você pode usar qualquer nome de variável aqui, como numero, indice, etc. 
3. in:
É a palavra-chave que indica que i vai receber cada um dos elementos da sequência que vier a seguir. 
4. range():
Esta função gera uma sequência de números inteiros. 
range(n): Gera números de 0 até n-1. Por exemplo, range(5) gera 0, 1, 2, 3, 4. 
range(inicio, fim): Gera números de inicio até fim-1. Por exemplo, range(1, 6) gera 1, 2, 3, 4, 5. 
range(inicio, fim, passo): Gera números de inicio até fim-1, mas incrementando em passo. Por exemplo, range(1, 10, 2) gera 1, 3, 5, 7, 9. """

#-------------------------------------------------------------------------------------------------
# Gerar números ímpares de acordo com a quantidade digitada pelo usuário

quantidade = int(input("Quantos números ímpares você deseja gerar? "))

numero = 1  # primeiro número ímpar
for i in range(quantidade):
    print(numero)
    numero += 2
 #-------------------------------------------------------------------------------------------------

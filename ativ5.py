"""Beleza 🚀

Em Python, while True: é um laço infinito.

👉 Vamos por partes:

while = "enquanto"

True = sempre verdadeiro"""
# while True:
#     print("Isso nunca vai parar!")

"""Esse código vai rodar para sempre, porque a condição (True) nunca deixa de ser verdadeira."""
"""🔹 Como sair dele?
 Normalmente a gente usa o comando #break# dentro do laço para parar em algum momento:"""
# while True:
#     resposta = input("Digite 'sair' para encerrar: ")
#     if resposta == "sair":
#         break
#     print("Você digitou:", resposta)

"""Nesse exemplo, o while True roda sem parar, até que o usuário digite "sair", quando o break é executado e o loop acaba.

⚡ Em resumo:

while True → roda pra sempre

precisa de break (ou algo que pare o programa)

muito usado em menus, jogos, servidores, e programas que ficam esperando eventos"""
#-------------------------------------------------------------------------------------------------
#media com break
soma = 0
nota = 0

while True:
    nota = float(input('Digite a nota do aluno: \n ou \nDigite a  99 para SAIR : ' ))
    if nota == 99:
        break
    soma += nota
print(f' A média do aluno é {soma / 4}')
#-------------------------------------------------------------------------------------------------
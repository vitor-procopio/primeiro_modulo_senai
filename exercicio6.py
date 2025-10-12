"""🔹 1. Declaração das variáveis
soma = 0
contador = 0


soma: vai acumular todas as notas digitadas.

contador: conta quantas notas foram digitadas (assim podemos calcular a média certinho).

🔹 2. Mensagens iniciais
print("=== Cálculo da média do aluno ===")
print("Digite as notas uma por vez.")
print("Para encerrar, digite 99.\n")


Apenas para deixar o programa mais amigável, explicando ao usuário como usar.

🔹 3. Loop infinito (while True)
while True:
    nota = float(input("Digite a nota: "))
    if nota == 99:
        break
    soma += nota
    contador += 1


while True: cria um laço que só vai parar com um break.

nota = float(input(...)): o usuário digita uma nota (convertida para número decimal).

if nota == 99: break: se a pessoa digitar 99, o programa sai do loop.

soma += nota: soma a nota digitada ao total.

contador += 1: aumenta em 1 a contagem de notas.

🔹 4. Cálculo da média
if contador > 0:
    media = soma / contador
    print(f"\nO aluno teve {contador} notas registradas.")
    print(f"A média final é: {media:.2f}")
else:
    print("\nNenhuma nota foi registrada.")


if contador > 0: só calcula a média se ao menos 1 nota tiver sido digitada.

media = soma / contador: divide a soma das notas pela quantidade de notas.

print(... {media:.2f}): mostra a média formatada com 2 casas decimais.

else: se o usuário só digitar 99 sem nenhuma nota, aparece a mensagem “Nenhuma nota foi registrada.”"""

#-------------------------------------------------------------------------------------------------
soma = 0
contador = 0

print("=== Cálculo da média do aluno ===")
print("Digite as notas uma por vez.")
print("Para encerrar, digite 99.\n")

while True:
    nota = float(input("Digite a nota: "))
    if nota == 99:
        break
    soma += nota
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"\nO aluno teve {contador} notas registradas.")
    print(f"A média final é: {media:.2f}")
else:
    print("\nNenhuma nota foi registrada.")
#-------------------------------------------------------------------------------------------------
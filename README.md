📁 Estrutura do Repositório
🟢 Nível Básico
ativ1.py - "Olá Mundo" clássico para iniciar na programação

ativ2.py - Operações matemáticas básicas com entrada do usuário

exercicio1.py - Cálculo de média escolar simples

exercicio2.py - Cálculo de IMC (Índice de Massa Corporal)

exercicio3.py - Operações matemáticas (multiplicação, divisão, subtração)

🟡 Nível Intermediário
ativ3.py - Demonstração do match-case (Python 3.10+)

exercicio4.py - Sistema de comissão para vendedores

exercicio8.py - Cálculo de média usando listas e for loop

🔵 Estruturas de Controle
ativ4.py & exercicio5.py - Implementação de loops while com condicionais

ativ5.py - Uso de while True com break para controle de fluxo

ativ6.py & exercicio7.py - Geração de números ímpares usando diferentes abordagens

ativ7.py & exercicio6.py - Cálculos de média com acumuladores e contadores

🎯 Conceitos Demonstrados
1. Entrada e Saída Básica
python
# Exemplo de input/output
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
2. Estruturas Condicionais
if/else tradicional

match-case (Python 3.10+)

3. Loops e Iterações
while com condição controlada

while True com break

for...in range() para iterações numéricas

4. Manipulação de Dados
Conversão de tipos (int(), float())

Acumuladores e contadores

Listas e operações com listas

💡 Destaques Técnicos
Match-Case (Python 3.10+)
python
match variavel:
    case "valor1":
        print("Código para valor1")
    case "valor2":
        print("Código para valor2")
    case _:
        print("Código padrão")
Loop Controlado com Break
python
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == "sair":
        break
Cálculo de Média com Validação
python
if contador > 0:
    media = soma / contador
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota registrada.")
🚀 Aplicações Práticas
Estes exercícios cobrem cenários do mundo real como:

Sistemas educacionais (cálculo de médias)

Sistemas comerciais (cálculo de comissões)

Aplicações de saúde (cálculo de IMC)

Jogos e interatividade (charadas e desafios)

📈 Progressão de Aprendizado
Os arquivos seguem uma progressão lógica de complexidade, permitindo que iniciantes desenvolvam habilidades gradualmente enquanto programadores mais experientes podem revisitar conceitos fundamentais.

🛠 Habilidades Desenvolvidas
Lógica de programação

Manipulação de dados

Controle de fluxo

Validação de entrada

Resolução de problemas

Boas práticas de codificação

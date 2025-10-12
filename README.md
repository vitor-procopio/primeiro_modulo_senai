📁 Estrutura do Repositório
🟢 Nível Básico

ativ1.py – Implementação do clássico “Olá, Mundo”, introduzindo os primeiros conceitos de programação.

ativ2.py – Execução de operações matemáticas básicas com entrada de dados via usuário.

exercicio1.py – Cálculo simples de média escolar.

exercicio2.py – Cálculo do IMC (Índice de Massa Corporal).

exercicio3.py – Operações aritméticas (multiplicação, divisão e subtração).

🟡 Nível Intermediário

ativ3.py – Demonstração prática do match-case (recurso introduzido no Python 3.10+).

exercicio4.py – Sistema de cálculo de comissão para vendedores.

exercicio8.py – Cálculo de média utilizando listas e loops for.

🔵 Estruturas de Controle

ativ4.py e exercicio5.py – Implementações com loops while e condicionais.

ativ5.py – Uso de while True com break para controle de fluxo.

ativ6.py e exercicio7.py – Geração de números ímpares utilizando diferentes abordagens.

ativ7.py e exercicio6.py – Cálculos de média com acumuladores e contadores.

🎯 Conceitos Abordados
1. Entrada e Saída de Dados
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

2. Estruturas Condicionais

if/else tradicional

match-case (Python 3.10+)

3. Estruturas de Repetição

while com condição controlada

while True com break

for...in range() para iterações numéricas

4. Manipulação de Dados

Conversão de tipos (int(), float())

Uso de acumuladores e contadores

Criação e manipulação de listas

💡 Destaques Técnicos
Uso do match-case
match variavel:
    case "valor1":
        print("Código para valor1")
    case "valor2":
        print("Código para valor2")
    case _:
        print("Código padrão")

Loop Controlado com break
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == "sair":
        break

Cálculo de Média com Validação
if contador > 0:
    media = soma / contador
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota registrada.")

🚀 Aplicações Práticas

Os exercícios representam cenários comuns do mundo real, como:

Sistemas educacionais: cálculo de médias.

Sistemas comerciais: cálculo de comissões.

Aplicações de saúde: cálculo de IMC.

Jogos e interatividade: desafios e perguntas lógicas.

📈 Progressão de Aprendizado

A organização dos arquivos segue uma progressão lógica de complexidade, permitindo que:

Iniciantes aprendam gradualmente os fundamentos da linguagem.

Programadores intermediários revisem conceitos essenciais de forma prática.

🛠 Habilidades Desenvolvidas

Lógica de programação

Manipulação e validação de dados

Controle de fluxo

Estruturação e clareza de código

Resolução de problemas

Boas práticas de desenvolvimento

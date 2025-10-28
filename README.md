🐍 Exercícios de Python — Fundamentos

Coleção de atividades práticas para aprender lógica de programação e Python passo a passo.
Ideal para iniciantes que querem entender desde o “Olá Mundo” até estruturas de repetição e conceitos modernos da linguagem.

📚 ÍNDICE DE CONTEÚDOS
🎯 Exercícios Básicos
Arquivo	Descrição	Dificuldade
ativ1.py	Olá Mundo — Primeiro programa	⭐

ativ2.py	Soma simples — Entrada e operações	⭐

exercicio1.py	Média escolar — 3 notas	⭐

exercicio2.py	Cálculo de IMC — Saúde	⭐⭐

➕ Operações Matemáticas
Arquivo	Operações	Conceitos
exercicio3.py	Multiplicação, Divisão, Subtração	float(), operadores matemáticos
exercicio4.py	Cálculo de comissão	Porcentagem, formatação com f-string
🔄 Estruturas de Repetição — WHILE
Arquivo	Descrição	Conceito
ativ6.py	Números ímpares	while com contador
ativ8.py	Números pares	while incremental
ativ7.py	Média escolar	while com acumulador
ativ5.py	Média com interrupção	while True, break
🎮 Programas Interativos
Arquivo	Tipo	Descrição
ativ4.py	🎯 Charada	"Charada da fruta"
exercicio5.py	🎯 Charada	"Buraco negro"
exercicio6.py	📊 Calculadora	Média dinâmica com interação
🔁 Estruturas de Repetição — FOR
Arquivo	Descrição	Destaque
exercicio7.py	Números ímpares	for + range()
exercicio8.py	Média com lista	for, listas, sum()
🆕 Recursos Modernos
Arquivo	Recurso	Versão
ativ3.py	match-case	Python 3.10+
🚀 Como Usar
📋 Pré-requisitos

✅ Python 3.10+ (necessário para match-case)

💻 Editor de código: VS Code, PyCharm ou IDLE

🎬 Executando os Programas
# Execute qualquer exercício
python exercicio1.py

# Ou diretamente no terminal
python3 ativ2.py

🧠 Conceitos Abordados
📊 Por Categoria
🔤 Entrada e Saída
input()     # Receber dados do usuário
print()     # Exibir resultados
f"texto"    # Formatação moderna (f-strings)

🔢 Tipos de Dados
Tipo	Descrição
int	Números inteiros
float	Números decimais
str	Texto (strings)
⚡ Estruturas de Controle
# Condicionais
if, elif, else
match case  # (Python 3.10+)

# Loops
while, while True
for i in range()

🔄 Exemplos de Loops
🔁 Loop WHILE
# While simples
contador = 0
while contador < 10:
    print(contador)
    contador += 1

# While infinito com break
while True:
    resposta = input("Digite 'sair': ")
    if resposta == "sair":
        break

🔢 Loop FOR
# Range básico
for i in range(5):          # 0, 1, 2, 3, 4
for i in range(1, 6):       # 1, 2, 3, 4, 5
for i in range(1, 10, 2):   # 1, 3, 5, 7, 9

📖 Guia de Aprendizado
🎯 Para Iniciantes

Comece com ativ1.py e ativ2.py

Pratique operações em exercicio3.py

Explore loops com ativ6.py e ativ8.py

🔄 Para Praticar Loops
Tipo de Loop	Arquivos
While básico	ativ6.py, ativ8.py
While com acumulador	ativ7.py
While infinito	ativ5.py, exercicio6.py
For loop	exercicio7.py, exercicio8.py
🆕 Recursos Avançados

match-case: ativ3.py

Listas e funções: exercicio8.py

💡 Dicas Importantes
✅ Boas Práticas

Teste cada exercício separadamente

Modifique os valores de entrada

Experimente fazer variações dos códigos

Use print() para debuggar

🐛 Solução de Problemas
Erro	Causa	Solução
❌ Erro de versão	Usando Python antigo	Atualize para Python 3.10+
⚠️ Entrada inválida	Falta de validação	Teste com diferentes valores
🔁 Loop infinito	Condição incorreta	Revise o while ou adicione break

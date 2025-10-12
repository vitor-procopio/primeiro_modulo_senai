"""📘 Utilizando switch-case (match-case) no Python
📌 O que é switch-case?
O switch-case é uma estrutura de controle comum em muitas linguagens de programação (como C, Java e JavaScript) que permite executar diferentes blocos de código com base no valor de uma variável. Ele é útil como alternativa a múltiplos blocos if-elif-else.

No Python, não existe a estrutura tradicional switch-case, mas a partir da versão Python 3.10, foi introduzido o match-case, que oferece funcionalidade similar e até mais poderosa."""
"""✅ Requisitos
Python 3.10 ou superior (o match-case não existe em versões anteriores)."""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#🧠 Como funciona o match-case?
#A estrutura básica é:
consumo = 10

match consumo:
    case valor if valor < 8:
        print("Baixo desempenho")
    case valor if valor < 12:
        print("Desempenho médio")
    case _:
        print("Bom desempenho")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
variavel = "valor1"

match variavel:
    case "valor1":
        print("Código para valor1")
    case "valor2":
        print("Código para valor2")
    case _:
        print("Código padrão")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""oq esta errado ? match variavel: case valor1: # código para valor1 case valor2: # código para valor2 case _: # código padrão (equivalente ao else) #Você também pode usar condições dentro dos case, como: match consumo: case valor if valor < 8: print("Baixo desempenho") case valor if valor < 12: print("Desempenho médio") case _: print("Bom desempenho")"""

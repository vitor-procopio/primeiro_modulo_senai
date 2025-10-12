#--------------------------------------------------------------------------------------
"""Charada da fruta usando while loop"""
#--------------------------------------------------------------------------------------
print("Charada, boa sorte neste desafio!")
buraco = input("Quanto mais você tira de mim, maior eu fico.")

while buraco != 'Buraco negro':
    buraco = input('O que eu sou? ')
    if buraco == 'Buraco negro':
        print('Você acertou!')
    else:
        print('Tente novamente, te falta QI!')
#--------------------------------------------------------------------------------------

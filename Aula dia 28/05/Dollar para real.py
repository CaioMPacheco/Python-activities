import os
def limpar_tela():
    os.system('cls')

limpar_tela()

real = float(input("Qual o valor em dollars? :"))
dollar = 5.25
conversão = real*dollar

if real < 0:
    print("Impossível fazer isso!")
else:   
    print(f"O valor em real é {conversão:.2f}R$")
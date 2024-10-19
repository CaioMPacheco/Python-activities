import os
def limpar_tela():
    os.system('cls')

limpar_tela()

valororiginal = float(input("Qual o preço original do produto? :"))
desconto = float(input("Qual o valor do desconto? (em porcentagem) :"))
porcentagem = desconto/100 * valororiginal
preço_final = valororiginal - desconto

if valororiginal < 0:
    print("Impossível fazer sua operação!")

elif desconto == 0:
    print(f"O produto é {valororiginal}R$")
elif desconto < 0:
    print("Impossível fazer sua operação!")
else:
    print(f"O produto é {preço_final}R$")

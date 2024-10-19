import os
def limpar_tela():
    os.system('cls')

limpar_tela()

#Começo
raio = float(input("Qual o valor do raio? :"))
pi = 3.141592
area = pi * raio ** 2

if raio < 0 :
    print("Não é possível calcular sua área!")

else:
    print(f"O valor da área é {area}m²")
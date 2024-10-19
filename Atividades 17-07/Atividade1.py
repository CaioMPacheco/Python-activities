import math
import os
import numpy as np
import matplotlib.pyplot as plt

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar()

a = float(input("Digite o valor de a: "))
if a == 0:
    print("Não é uma equação do segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    limpar()

    delta = b**2- 4*a*c

    print(f"Delta = {b}² - 4×{a}×{c}")
    print(f"Delta = {b*b} - {4*a*c}")
    print(f"Delta = {delta}")
    print("\n")

    input("Pressione ENTER para continuar!")
    limpar()

    if delta < 0:
        print("Delta é negativo, portanto não há raízes reais")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Delta é igual a 0, a única raiz é x = {-b} / (2×{a})")
        print(f"x = {x}")
    elif delta != 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Delta é positivo, as raízes são:")
        print(f"x1 = (-{b} + √{delta}) / (2×{a})")
        print(f"x1 = ({-b} + {math.sqrt(delta)}) / (2×{a})")
        print(f"x1 = {x1}")
        print(f"x2 = (-{b} - √{delta}) / (2×{a})")
        print(f"x2 = ({-b} - {math.sqrt(delta)}) / (2×{a})")
        print(f"x2 = {x2}")
        if a > 0:
            print("A parábola é concava para cima")
            minx = maxix = (-1 * b)/2 * a
            miny = maxiy = (-1 *delta)/4 * a
            print(f"E o ponto mínimo dela é ({minx} , {miny}) ")
            x = np.array([1, 2, 3, 15, 45])
            y = np.array([43, 59, 98,])
            plt.plot(x,y)
            plt.show()
        elif a < 0 :
            print("A parábola é concava para baixo")
            maxix = (-1 * b)/2 * a
            maxiy = (-1 *delta)/4 * a
            print(f"E o ponto máximo dela é ({maxix}, {maxiy}) ")
        else:
            print("uma função de 2º grau não pode ter A igual a zero")
    else:
        print("Operação inválida")

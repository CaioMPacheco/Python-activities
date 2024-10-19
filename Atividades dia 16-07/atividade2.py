import os

def limpar():
    os.system('cls')

limpar()

#Menu de escolha
print("--------------------------------------------------------------------------")
print("                            Consumo de energia                            ")
print("                             By:Caio Pacheco                              ")
print("--------------------------------------------------------------------------")

print(" \n")
locais_casa = ["sala", "cozinha", "banheiro", "quarto", "lavanderia"]
perguntainicial = input("Qual o tipo de circuito( Paralelo ou Série? ): ").lower()
perguntaq = input("Qual o ambiente que você que saber o consumo?")

if perguntainicial == "série" or "serie":
    lampadas = int(input("Quantas lâmpadas tem em sua casa: "))
    tempohora = float(input("Quantas horas(apenas as horas) exatas você deixa elas ligadas no dia : "))
    tempomin = float(input("E quantos minutos(apenas os minutos) você deixa elas ligadas no dia : "))
    tensão = int(input("Qual a tensão da sua casa 127v ou 220v: "))
    tempohora = tempohora + (tempomin/60)
    resistência = lampadas * 70
    corrente = tensão/resistência
    potência = tensão * corrente
    consumo = (potência * tempohora)/1000
    BandeiraVerde = 0.79969
    BandeiraAmarela = 0.81854
    BandeiraVermelha = 0.84432
    semana = consumo * 7
    mês = consumo * 30
    ano = consumo * 365

    limpar()
    print("--------------------------------------------------------------------------")
    print("                            Consumo de energia                            ")
    print("                             By:Caio Pacheco                              ")
    print("--------------------------------------------------------------------------")

    print("\n")
    print(f"Na bandeira verde você teve o consumo de {consumo * BandeiraVerde :.2f}R$ no dia .")
    print(f"Na bandeira amarela você teve o consumo de {consumo * BandeiraAmarela :.2f}R$ no dia .")
    print(f"Na bandeira vermelha você teve o consumo de {consumo * BandeiraVermelha :.2f}R$ no dia .")
    print("\n")
    print(f"Na bandeira verde você teve o consumo de {semana * BandeiraVerde :.2f}R$ na semana .")
    print(f"Na bandeira amarela você teve o consumo de {semana * BandeiraAmarela :.2f}R$ na semana .")
    print(f"Na bandeira vermelha você teve o consumo de {semana * BandeiraVermelha :.2f}R$ na semana .")
    print("\n")
    print(f"Na bandeira verde você teve o consumo de {mês * BandeiraVerde :.2f}R$ no mês .")
    print(f"Na bandeira amarela você teve o consumo de {mês * BandeiraAmarela :.2f}R$ no mês .")
    print(f"Na bandeira vermelha você teve o consumo de {mês * BandeiraVermelha :.2f}R$ no mês .")
    print("\n")
    print(f"Na bandeira branca você teve o consumo de {ano * BandeiraVerde :.2f}R$ no ano .")
    print(f"Na bandeira amarela você teve o consumo de {ano * BandeiraAmarela :.2f}R$ no ano .")
    print(f"Na bandeira vermelha você teve o consumo de {ano * BandeiraVermelha :.2f}R$ no ano .")

elif perguntainicial == "paralelo":
    lampadas = int(input("Quantas lâmpadas tem em sua casa: "))
    tempohora = float(input("Quantas horas(apenas as horas) exatas você deixa elas ligadas no dia :"))
    tempomin = float(input("E quantos minutos(apenas os minutos) você deixa elas ligadas no dia : "))
    tensão = int(input("Qual a tensão da sua casa 127v ou 220v: "))
    tempohora = tempohora + (tempomin/60)
    BandeiraVerde = 0.79969
    BandeiraAmarela = 0.81854
    BandeiraVermelha = 0.84432
    numeroini = 0
    resistências = []

    for i in range(lampadas):
        numeroini += 1
        resistência = int(input(f"{numeroini} - Qual a resistência da {numeroini}ª lampâda: "))
        resistências.append(resistência)

    resistência_eq = 1 / sum(1/ r for r in resistências)
    corrente = tensão / resistência_eq
    potência = tensão * corrente
    consumo = (potência * tempohora) / 1000
    semana = consumo * 7
    mês = consumo * 30
    ano = consumo * 365

    limpar()

    print("--------------------------------------------------------------------------")
    print("                            Consumo de energia                            ")
    print("                             By:Caio Pacheco                              ")
    print("--------------------------------------------------------------------------")

    print("\n")
    print(f"Na bandeira verde você teve o consumo de {consumo * BandeiraVerde :.2f}R$ no dia .")
    print(f"Na bandeira amarela você teve o consumo de {consumo * BandeiraAmarela :.2f}R$ no dia .")
    print(f"Na bandeira vermelha você teve o consumo de {consumo * BandeiraVermelha :.2f}R$ no dia .")
    print("\n")
    print(f"Na bandeira verde você teve o consumo de {semana * BandeiraVerde :.2f}R$ na semana .")
    print(f"Na bandeira amarela você teve o consumo de {semana * BandeiraAmarela :.2f}R$ na semana .")
    print(f"Na bandeira vermelha você teve o consum    o de {semana * BandeiraVermelha :.2f}R$ na semana .")
    print("\n")
    print(f"Na bandeira verde você teve o consumo de {mês * BandeiraVerde :.2f}R$ no mês .")
    print(f"Na bandeira amarela você teve o consumo de {mês * BandeiraAmarela :.2f}R$ no mês .")
    print(f"Na bandeira vermelha você teve o consumo de {mês * BandeiraVermelha :.2f}R$ no mês .")
    print("\n")
    print(f"Na bandeira verde você teve o consumo de {ano * BandeiraVerde :.2f}R$ no ano .")
    print(f"Na bandeira amarela você teve o consumo de {ano * BandeiraAmarela :.2f}R$ no ano .")
    print(f"Na bandeira vermelha você teve o consumo de {ano * BandeiraVermelha :.2f}R$ no ano .")
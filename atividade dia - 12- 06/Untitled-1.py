lampadas = int(input("Quantas lâmpadas tem em sua casa: "))
tempohora = float(input("Quantas horas(apenas as horas) exatas você deixa elas ligadas no dia : "))
tempomin = float(input("E quantos minutos(apenas os minutos) você deixa elas ligadas no dia : "))
tempohora = tempohora + (tempomin/60)
tensão = 127
resistência = lampadas * 70
corrente = tensão/resistência
potência = tensão * corrente
consumo = (potência * tempohora)/1000
BandeiraBranca = 3.87
BandeiraAmarela = 4.53
BandeiraVermelha = 5.60
mês = consumo * 30

print("\n")
print(f"Na bandeira branca você teve o consumo de {consumo * BandeiraBranca :.2f}R$ no dia .")
print(f"Na bandeira amarela você teve o consumo de {consumo * BandeiraAmarela :.2f}R$ no dia .")
print(f"Na bandeira vermelha você teve o consumo de {consumo * BandeiraVermelha :.2f}R$ no dia .")
print("\n")
print(f"Na bandeira branca você teve o consumo de {mês * BandeiraBranca :.2f}R$ no mês .")
print(f"Na bandeira amarela você teve o consumo de {mês * BandeiraAmarela :.2f}R$ no mês .")
print(f"Na bandeira vermelha você teve o consumo de {mês * BandeiraVermelha :.2f}R$ no mês .")

def atividade_8():
    #Variáveis
    nome = str(input("Por favor digite um apelido para você: "))
    número = len(nome) * (3 + 5) // 2
    certo = False
    Tentativa = 0

    #Código
    print("Por favor tente adivinha um número de 1 a 100")
    while not certo:
        chute = int(input("Digite o número: "))
        Tentativa += 1

        if número > 100:
            (número - número) + 49
        
        if chute == número:
            print(f"Parabéns você acertou, o número secreto era {número} e você utilizou {Tentativa} tentativas")
            print("Se quiser jogar novamente, use outro apelido!")
            certo = True
        elif chute > número:
            print("O número secreto é menor. ")
        elif chute < número:
            print("O número secreto é maior. ")
atividade_8()
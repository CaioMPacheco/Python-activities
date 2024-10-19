 # Pede ao usuário o valor do salário
salario = float(input("Digite o valor do salario: "))

 # Pede ao usuário o valor do apartamento
apartamento = float(input("Digite o valor do apartamento: "))

 # Pergunta em quantos anos o usuário pretende pagar o apartamento
anos = int(input("Em quantos anos você pretende pagar o apartamento? "))

 # Taxa de juros anual
taxa_juros = 0.12

 # Saldo devedor inicial
saldo_devedor = apartamento

 # Lista para armazenar as parcelas anuais
parcelas_anuais = []

 # Variável para verificar se pode comprar o apartamento
pode_comprar = True

 # Calcula o valor das parcelas anuais com juros
for ano in range(1, anos + 1):
    juros_anual = saldo_devedor * taxa_juros
    pagamento_anual = saldo_devedor / (anos - ano + 1)
    saldo_devedor -= pagamento_anual
    parcela_anual_com_juros = juros_anual + pagamento_anual
    parcelas_anuais.append(parcela_anual_com_juros)

    # Verifica se a parcela anual dividida por 12 é maior que 30% do salário
    if parcela_anual_com_juros / 12 > salario * 0.3:
        pode_comprar = False

 # Exibe o valor a ser pago a cada ano
for ano, parcela_anual in enumerate(parcelas_anuais, start=1):
    print(f"Ano {ano}: R$ {parcela_anual:.2f}")

 # Exibe se pode ou não comprar o apartamento
if pode_comprar:
    print("Você pode comprar o apartamento pois a parcela é menor que 30% do seu salário")
else:
    print("Você não pode comprar o apartamento pois a parcela é maior que 30% do seu salário")

def atividade_3():
    # Pede ao usuário o número inteiro
    num = int(input("Digite um número inteiro: "))

    # Pede ao usuário qual será a base de conversão
    base = int(input("Digite a base de conversão (2 para binário, 8 para octal, 16 para hexadecimal): "))

    if base == 2:
        print(f"O número {num} em binário é: {bin(num)[2:]}")
    elif base == 8:
        print(f"O número {num} em octal é: {oct(num)[2:]}")
    elif base == 16:
        print(f"O número {num} em hexadecimal é: {hex(num)[2:]}")
    else:
        print("Base de conversão inválida")

def atividade_4():
    # Peça o ano de nascimento do usuário
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    
    # Informe de acordo com a idade se ele ainda vai se alistar (< 18 anos),
    # se já pode se alistar (18 anos),
    # ou se já passou da hora de se alistar (> 18 anos),
    # e mostre quantos anos faltam ou já passaram.
    ano_atual = 2024
    idade = ano_atual - ano_nascimento
    
    if idade < 18:
        print(f"Você ainda vai se alistar. Faltam {18 - idade} anos.")
    elif idade == 18:
        print("Você já pode se alistar.")
    else:
        print(f"Você já passou da hora de se alistar. Já se passaram {idade - 18} anos.")

def atividade_5():
    # Peça ao usuário seu ano de nascimento
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = 2024
    idade = ano_atual - ano_nascimento
    
    # Verifica em qual categoria de natação o usuário se enquadra
    if idade < 9:
        print("Você se enquadra na categoria Mirim")
    elif idade < 14:
        print("Você se enquadra na categoria Infantil")
    elif idade < 19:
        print("Você se enquadra na categoria Juvenil")
    elif idade < 22:
        print("Você se enquadra na categoria Sênior")
    else:
        print("Você se enquadra na categoria Master")

def atividade_6():
    # Peça ao usuário para digitar uma frase qualquer
    frase = input("Digite uma frase qualquer: ")
    
    # Remove espaços em branco e converte para letras minúsculas
    frase = frase.replace(" ", "").lower()
    
    # Verifica se a frase é um palíndromo
    if frase == frase[::-1]:
        print("A frase é um palíndromo")
    else:
        print("A frase não é um palíndromo")
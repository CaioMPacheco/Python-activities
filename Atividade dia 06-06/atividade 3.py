#Função para contar vogal
def cont_letra(palavra):
    vogais ="aeiou"
    return len([letra for letra in palavra.lower() if letra in vogais])

#Código
palavra_vogal = input("Digite uma palavra para se contas as vogais: ")
quantidade_vogais = cont_letra(palavra_vogal)
print(f"Essa palavra tem {quantidade_vogais} vogais")

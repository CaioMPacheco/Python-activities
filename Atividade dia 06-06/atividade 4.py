#Função para contar vogal
def cont_vogal(palavra):
    vogais ="aeiou"
    return len([letra for letra in palavra.lower() if letra in vogais])

#Exemplo de uso
palavra_exemplo = "desenvolvimento"
quantidade_vogais = cont_vogal(palavra_exemplo)
print(f"A palavra '{palavra_exemplo}' tem {quantidade_vogais} vogais. ")
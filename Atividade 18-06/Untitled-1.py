def atividade_5():
    # Variáveis
    frase = input("Digite uma frase: ")
    As = ['á', 'ã', 'à', 'â']
    
    # Substituição dos caracteres acentuados
    for caracter in As:
        frase = frase.replace(caracter, 'a')
        
    # Contagem de 'a' e 'A'
    contar_a = frase.lower().count('a')
    
    # Saída
    print(f"A frase tem {contar_a} A ou a!")

atividade_5()
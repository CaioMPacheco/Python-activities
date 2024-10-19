def Atividade_1():
    print(" \n")
    pizzas = ["pepperoni", "3 queijos", "strogonoff"]

    for pizza in pizzas:
        print(pizza)

    print(" \n")

    for pizza in pizzas:
        if pizza == "pepperoni":
            print(f"A pizza de {pizza} é uma das mais famosas.")
        elif pizza == "3 queijos":
            print(f"A pizza de {pizza} é odiada por muitos e amada por outros.")
        else:
            print(f"A pizza {pizza} é bem diferente mas é uma das mais saborosas!")

    print(" \n")

    print(f"A pizza de {pizzas[0]} é uma das mais famosas.")
    print(f"A pizza de {pizzas[1]} é odiada por muitos e amada por outros.")
    print(f"Mas a pizza {pizzas[-1]} é bem diferente e é uma das mais saborosas!")
    print("Eu amo todos os tipos de pizza, normalmente sempre peço 2 por mês e sempre peço ou como na Francesinha!!!")

def Atividade_2():
    animais = ['Cachorro', 'Gato', 'Urso']

    for animal in animais:
        print(animal)

    print(" ")
    
    for animal in animais:
        if animal == "Cachorro":
            print(f"O {animal} é um animal muito amigavel.")
        elif animal == "Gato":
            print(f"O {animal} é um animal bastante travesso.")
        else:
            print(f"O {animal} é um animal muito forte.")
    animais = str(animais).lower()
    animais = animais.replace("[", " ")
    animais = animais.replace("]", " ")
    animais = animais.replace("'", "")

    print(f"Os animais {animais} são todos mamíferos")

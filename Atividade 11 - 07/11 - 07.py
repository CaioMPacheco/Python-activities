import os, datetime, sys
from datetime import datetime
from random import *

def limpar_tela():
    os.system('cls')
def Atividade1():
    números = [0, 2, 4, 6, 8, 10]
    print(números) 
    númeroreverso = reversed(números)
    print(list(númeroreverso))

def Atividade2():
    horas = int(input("Quantas horas você trabalhou no mês: "))
    if horas > 160:
        print(f"Seu salário será de R${(160 * 29.11) + ((horas - 160)*5):.2f}")
    elif horas <= 160:
        print(f"Você não receberá hora extra, logo seu salário será de R${160*29.11:.2f}.")

def Atividade3():
    númerosperfeitos = [6, 28, 496, 8128, 33550336]
    perguntanúmero = int(input("Digite um número para saber se ele é perfeito: "))
    if perguntanúmero in númerosperfeitos:
        print("O número é perfeito")
    else:
        print("O número não é perfeito")

def Atividade4():
    print(f"A versão do python é {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def Atividade5():
    # Obtém a data e hora atuais
    agora = datetime.datetime.now()

    # Formata a saída para exibição
    data_formatada = agora.strftime("%Y-%m-%d")
    hora_formatada = agora.strftime("%H:%M:%S")

    # Exibe a data e hora atuais
    print("Data atual:", data_formatada)
    print("Hora atual:", hora_formatada)

def Atividade6():
    def numero_para_romano(numero):
    # Definição dos símbolos e seus valores
        simbolos = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
            40: "XL", 50: "L", 90: "XC", 100: "C",
            400: "CD", 500: "D", 900: "CM", 1000: "M"
        }
        
        # Lista reversa dos valores para iteração
        valores = sorted(simbolos.keys(), reverse=True)
        
        resultado = ""
        
        # Iteração para encontrar o algarismo romano equivalente
        for valor in valores:
            while numero >= valor:
                resultado += simbolos[valor]
                numero -= valor
        
        return resultado

    # Função principal para interação com o usuário
    def main():
        try:
            # Recebe o número do usuário
            numero = int(input("Digite um número inteiro (1 a 3999): "))
            
            # Verifica se o número está dentro do intervalo válido
            if 1 <= numero <= 3999:
                # Converte o número para algarismo romano
                romano = numero_para_romano(numero)
                print(f"O número {numero} em algarismos romanos é: {romano}")
            else:
                print("Número fora do intervalo válido (1 a 3999).")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

    if __name__ == "__main__":
        main()

def Atividade7():
    var = "Global"

    def varlocal():
        var = "Local"
        print(var)
    print(var)
    varlocal()

def Atividade8():
    def senhas():
        quantidades = int("Você quer uma senha com tantos números? ")
        senha = random(0, quantidades)
        randint(0, senha)
        print(randint)

    senhas()

def Atividade9():
    class Medico:
     def __init__(self, nome, especialidade, atende_convenio):
        self.nome = nome
        self.especialidade = especialidade
        self.atende_convenio = atende_convenio

    # Lista de médicos pré-cadastrados
    medicos = [
        Medico("Dr. Carlos", "Clínico Geral", False),
        Medico("Dr. Ana", "Pediatra", True),
        Medico("Dr. Luiz", "Cardiologista", False),
        Medico("Dra. Maria", "Dermatologista", True),
        Medico("Dr. Felipe", "Ortopedista", True),
        Medico("Dra. Laura", "Oftalmologista", False),
        Medico("Dr. João", "Ginecologista", True),
        Medico("Dra. Sofia", "Neurologista", False),
        Medico("Dr. Pedro", "Urologista", False),
        Medico("Dra. Juliana", "Oncologista", True)
    ]

# Dicionário para armazenar as consultas marcadas
    consultas_marcadas = {}

# Função para listar os médicos
    def listar_medicos():
        print("Lista de Médicos:")
        for i, medico in enumerate(medicos):
            print(f"{i+1}. {medico.nome} - {medico.especialidade}")

# Função para agendar uma consulta
    def agendar_consulta(medico_index, data_consulta, paciente):
        medico = medicos[medico_index - 1]
        if medico_index not in consultas_marcadas:
            consultas_marcadas[medico_index] = []
        consultas_marcadas[medico_index].append((data_consulta, paciente))
        print(f"Consulta agendada com sucesso para o Dr. {medico.nome} em {data_consulta}.")

# Função para calcular os valores ganhos pelos médicos até o final de 2024
    def calcular_valores_ganhos():
        valores_ganhos = {}
        for medico_index, consultas in consultas_marcadas.items():
            medico = medicos[medico_index - 1]
            valor_consulta = 300 if not medico.atende_convenio else 180
            total_ganho = len(consultas) * valor_consulta
            valores_ganhos[medico.nome] = total_ganho
        return valores_ganhos

# Exemplo de utilização do programa

# Listar os médicos disponíveis
    listar_medicos()
    print()

# Agendar consultas de exemplo
    agendar_consulta(2, "2024-07-20", "Maria Silva")
    agendar_consulta(4, "2024-07-25", "João Santos")
    agendar_consulta(6, "2024-08-02", "Carla Lima")
    agendar_consulta(8, "2024-08-10", "José Silva")
    agendar_consulta(10, "2024-08-15", "Amanda Souza")

# Calcular e imprimir os valores ganhos pelos médicos
    valores_ganhos = calcular_valores_ganhos()
    print("\nValores ganhos pelos médicos até o final de 2024:")
    for medico,valor in valores_ganhos.items():
        print(f"{medico}: R$ {valor:.2f}")

Atividade9()
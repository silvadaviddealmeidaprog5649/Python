from math import sqrt

def Soma(stringNum):
    # Criando uma lista para armazenar todos os números
    allNumbers = []
    
    # Adicionar números da string na lista
    for i in stringNum.split():
        try:
            allNumbers.append(float(i))  # Adiciona o valor à lista
        except ValueError:
            print(f"Valor inválido: {i}. Ignorando...")  # Mensagem de erro para valores inválidos
            continue  # Continua para o próximo número se for inválido
    
    # Realizar a operação matemática entre todos os números na lista
    result = allNumbers[0]  # Inicializa com o primeiro número
    for num in allNumbers[1:]:  # Começa a subtrair os números a partir do segundo
        result += num  # Subtrai os números sucessivos

    return result


def Subtrair(stringNum):
    # Criando uma lista para armazenar todos os números
    allNumbers = []
    
    # Adicionar números da string na lista
    for i in stringNum.split():
        try:
            allNumbers.append(float(i))  # Adiciona o valor à lista
        except ValueError:
            print(f"Valor inválido: {i}. Ignorando...")  # Mensagem de erro para valores inválidos
            continue  # Continua para o próximo número se for inválido
    
    # Realizar a operação matemática entre todos os números na lista
    result = allNumbers[0]  # Inicializa com o primeiro número
    for num in allNumbers[1:]:  # Começa a subtrair os números a partir do segundo
        result -= num  # Subtrai os números sucessivos

    return result


def Multiplicar(stringNum):
    # Criando uma lista para armazenar todos os números
    allNumbers = []
    
    # Adicionar números da string na lista
    for i in stringNum.split():
        try:
            allNumbers.append(float(i))  # Adiciona o valor à lista
        except ValueError:
            print(f"Valor inválido: {i}. Ignorando...")  # Mensagem de erro para valores inválidos
            continue  # Continua para o próximo número se for inválido
    
    # Realizar a operação matemática entre todos os números na lista
    result = allNumbers[0]  # Inicializa com o primeiro número
    for num in allNumbers[1:]:  # Começa a subtrair os números a partir do segundo
        result *= num  # Subtrai os números sucessivos

    return result

def Dividir(stringNum):
    # Criando uma lista para armazenar todos os números
    allNumbers = []
    
    # Adicionar números da string na lista
    for i in stringNum.split():
        try:
            allNumbers.append(float(i))  # Adiciona o valor à lista
        except ValueError:
            print(f"Valor inválido: {i}. Ignorando...")  # Mensagem de erro para valores inválidos
            continue  # Continua para o próximo número se for inválido
    
    # Realizar a operação matemática entre todos os números na lista
    result = allNumbers[0]  # Inicializa com o primeiro número
    for num in allNumbers[1:]:  # Começa a subtrair os números a partir do segundo
        try:
            result /= num  # Subtrai os números sucessivos
        except ZeroDivisionError:
            print("Não é possível dividir um número por zero.")
            return 0
    return result

def Potenciacao(stringNum, secondNum):
    return pow(stringNum, secondNum)

def Radiciacao(stringNum): 
    return sqrt(stringNum)
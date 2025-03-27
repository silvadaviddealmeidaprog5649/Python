from math import sqrt

def PrimeiroGrau(numA, numB):
    if numA == 0:
        print("O valor de 'a' não pode ser zero, pois não é uma função do primeiro grau.")
    else:
        raiz = -(numB) / numA
    return raiz

def SegundoGrau(numA, numB, numC):
    if numA == 0:
        print("O valor de 'a' não pode ser zero, pois não é uma função do segundo grau.")
    else:
        delta = pow(numB, 2)-4*numA*numC
        if delta < 0:
            print("Não existe raízes reais possíveis.")
            return 0, 0
        else:    
            x1 = (-(numB)-sqrt(delta))/(2*numA)
            x2 = (-(numB)+sqrt(delta))/(2*numA)
    return x1,x2
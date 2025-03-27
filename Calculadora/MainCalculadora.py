import Calculos
import Funcao

print("\nBem Vindo à Calculadora!")
acao = True
while acao:
    # Exibe as opções do menu a cada iteração do loop
    print(""" 
         1 - Soma
         2 - Subtração
         3 - Multiplicação
         4 - Divisão
         5 - Potenciação
         6 - Radiciação
         7 - Equação do Primeiro Grau
         8 - Equação do Segundo Grau
         0 - Sair\n""")
    
    try:
        escolha = int(input("Digite a operação desejada: \n"))
    except ValueError:
        print("Valor Inválido! Tente novamente!")
        continue  

    match escolha:
        case 0:  
            print("A calculadora foi finalizada! Muito obrigado!")
            break

        case 1:
            numValue = input("Digite todos os números que deseja somar separados por um espaço: \n")

            print("____________________________________")
            print("O resultado é " + str(Calculos.Soma(numValue)))
            print("____________________________________")

        case 2:
            numValue = input("Digite todos os números que deseja diminuir separados por um espaço: (OBS.: Os números após o primeiro terão os sinais invertidos, ou seja, na teoria, eles serão automaticamente multiplicados por -1.)\n")
            print("____________________________________")
            print("O resultado é: " + str(Calculos.Subtrair(numValue)))
            print("____________________________________")

        case 3:
            numValue = input("Digite todos os números que deseja multiplicar em sequência, separados por um espaço: \n")
            print("____________________________________")
            print("O resultado é: " + str(Calculos.Multiplicar(numValue)))
            print("____________________________________")

        case 4:
            numValue = input("Digite todos os números que deseja dividir em sequência, separados por um espaço: \n")
            print("____________________________________")
            print("O resultado é: " + str(Calculos.Dividir(numValue)))
            print("____________________________________")

        case 5:
            while True:
                try:
                    numValue1 = float(input("Digite o número que deseja ser a base da potência: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")

            while True:
                try:
                    numValue2 = float(input("Digite o número que deseja ser o expoente da potência: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")
            print("____________________________________")
            print("O resultado é: " + str(Calculos.Potenciacao(numValue1, numValue2)))
            print("____________________________________")

        case 6:
            while True:
                try:
                    numValue = float(input("Digite o número que deseja ser a base da raiz quadrada: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")
            print("____________________________________")

            print("O resultado é: " + str(Calculos.Radiciacao(numValue)))
            print("____________________________________")

        case 7:
            print("Considere o modelo de equação do primeiro grau: Ax+B=0")
            while True:
                try:
                    A_Value = float(input("Digite o valor de A da equação do primeiro grau: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")

            while True:
                try:
                    B_Value = float(input("Digite o valor de B da equação do primeiro grau: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")
            print("____________________________________")
            print("A raíz da equação é " + str(Funcao.PrimeiroGrau(A_Value, B_Value)))
            print("____________________________________")

        case 8:
            print("Considere o modelo de equação do segundo grau: Ax²+Bx+C=0")
            while True:
                try:
                    A_Value = float(input("Digite o valor de A da equação do segundo grau: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")

            while True:
                try:
                    B_Value = float(input("Digite o valor de B da equação do segundo grau: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")

            while True:
                try:
                    C_Value = float(input("Digite o valor de C da equação do segundo grau: \n"))
                    break
                except ValueError:
                    print("Valor inválido! Tente novamente!")

            x1, x2 = Funcao.SegundoGrau(A_Value, B_Value, C_Value)
            print("____________________________________")
            print(f"Os resultados das raízes da equação do segundo grau são {x1:.2f} e {x2:.2f}")
            print("____________________________________")

        case _:
            print("Opção não disponível! Tente novamente!")

    retorno = input("Deseja continuar utilizando a calculadora? (S/N) ").upper()
    
    while(retorno != "S" and retorno != "N"):
        retorno = input("Opção inválida! Digite novamente! ")
       
    if retorno == "N":
        acao = False
        print("Obrigado! Espero ter ajudado! Volte sempre que precisar!")
    else:
        pass

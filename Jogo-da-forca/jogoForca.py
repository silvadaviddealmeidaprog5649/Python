import random

progresso = True

while progresso:
    print("_________________________________________")
    print("\nBem vindo ao Jogo da Forca!\n")
    palavras = ['GELADEIRA', 'BICICLETA', 'TIJOLO', 'ALICATE', 'COMPUTADOR', 'CADERNO', 'ROUPA', 'BOLO', 'PEIXE', 'MERCADO', 'LIVRO', 'PIMENTA', 'TECLADO', 'CAMISA', 'SAPATO']
    palavra = random.choice(palavras)
    palavra_oculta = ["_" for i in range(len(palavra))]
    tentativa = 7
    acertos = []
    erros = []

    while tentativa > 0:
        match tentativa:
            case 1:
                print("      ________")
                print("     |        |")
                print("    O         |")
                print("  / | \       |")
                print("    |         |")
                print("   /          |")     

            case 2:
                print("      ________")
                print("     |        |")
                print("    O         |")
                print("  / | \       |")
                print("    |         |")
                print("              |")

            case 3:
                print("      ________")
                print("     |        |")
                print("    O         |")
                print("  / | \       |")
                print("              |")
                print("              |")     

            case 4:
                print("      ________")
                print("     |        |")
                print("    O         |")
                print("  / |         |")
                print("              |")
                print("              |")     

            case 5:
                print("      ________")
                print("     |        |")
                print("    O         |")
                print("    |         |")
                print("              |")
                print("              |")     

            case 6:
                print("      ________ ")
                print("     |        |")
                print("    O         |")
                print("              |")
                print("              |")
                print("              |")     

            case 7:
                print("      ________ ")
                print("     |        |")
                print("              |")
                print("              |")
                print("              |")
                print("              |")

            case _:
                print('Valor inválido!')

        print('Palavra oculta: ', ''.join(palavra_oculta))
        print('Acertos: ', acertos)
        print('Erros: ', erros)

        letra = input("Digite uma letra: ").upper()

        if letra in acertos or letra in erros:
            print("Você já tentou essa letra. Tente outra.")

        if letra in palavra and tentativa > 0 and letra not in acertos:
            acertos.append(letra)
            ocorrencia = [i for i, char in enumerate(palavra) if char == letra]
            for i in ocorrencia:
                palavra_oculta[i] = letra  
        elif letra not in palavra and tentativa > 0 and letra not in erros:
            erros.append(letra)
            tentativa -= 1

        if tentativa == 0:  
            print("      ________ ")
            print("     |        |")
            print("    O         |")
            print("  / | \       |")
            print("    |         |")
            print("   / \        |")

        if '_' not in palavra_oculta and tentativa > 0:
            print("Parabéns! Você ganhou! A palavra é %s." %(palavra))
            tentativa = 0
            
        elif '_' in palavra_oculta and tentativa > 0:
            print('Continue tentando!\n')

        elif '_' in palavra_oculta and tentativa == 0:
            print('Que pena! Você perdeu! A palavra era: %s' %(palavra))
            tentativa = 0

        while tentativa == 0:
            pergunta = str(input("Deseja continuar no jogo? Digite S para sim ou N para não. ").upper())
            match pergunta:
                case "S":
                    tentativa = 7
                    palavra = random.choice(palavras)
                    palavra_oculta = ["_" for i in range(len(palavra))]
                    tentativa = 7
                    acertos = []
                    erros = []
                case "N":
                    print("Obrigado por jogar!")
                    progresso = False
                    break
                case _:
                    print("Valor inválido!")

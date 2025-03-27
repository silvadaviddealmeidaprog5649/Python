from tkinter import *

def imprimirDados():
    try:
        # Obter os valores de peso e altura dos campos de entrada
        peso = float(caixa1.get())
        altura = float(caixa2.get())

        # Verificar se os valores são válidos e dentro de um intervalo razoável
        if peso <= 0 or peso > 500:
            vartx.set("Erro! Peso inválido!")
            varty.set("Digite um peso entre 1 e 500 kg.")
            return
        
        if altura <= 0 or altura > 2.5:
            vartx.set("Erro! Altura inválida!")
            varty.set("Digite uma altura entre 0.5 e 2.5 metros.")
            return

        # Calcular IMC
        imc = peso / (altura * altura)
        vartx.set(f"O seu IMC é: {imc:.2f}")
        
        # Classificar o IMC
        if imc < 16:
            varty.set("Magreza grave")
        elif imc < 17:
            varty.set("Magreza Moderada")
        elif imc < 18.5:
            varty.set("Magreza Leve")
        elif imc < 25:
            varty.set("Peso ideal")
        elif imc < 30:
            varty.set("Sobrepeso")
        elif imc < 35:
            varty.set("Obesidade grau I")
        elif imc < 40:
            varty.set("Obesidade grau II ou severa")
        else:
            varty.set("Obesidade grau III ou mórbida")
    
    except ValueError:
        vartx.set("Valor inválido! Tente novamente.")
        varty.set("")
        
# Criar a janela principal
janela = Tk()
vartx = StringVar()
varty = StringVar()

janela.title("Calculadora IMC")
janela.geometry("400x250")
janela.configure(background="#dde")

# Impedir que a janela seja redimensionada
janela.resizable(False, False)

# Centralizar a janela na tela
janela.eval('tk::PlaceWindow %s center' % janela.winfo_toplevel())

# Mensagem de boas-vindas
lbMsg = Label(janela, text="Bem-vindo à Calculadora IMC", background="#dde", foreground="#009")
lbMsg.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Instruções para o usuário
lbMsg2 = Label(janela, text="Digite os valores correspondentes:")
lbMsg2.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Labels para Peso e Altura
MainMsg1 = Label(janela, text="Peso (KG)", background="#dde", foreground="#009")
MainMsg1.grid(row=2, column=0, pady=5, padx=10, sticky="e")

MainMsg2 = Label(janela, text="Altura (m)", background="#dde", foreground="#009")
MainMsg2.grid(row=3, column=0, pady=5, padx=10, sticky="e")

# Entradas para Peso e Altura
caixa1 = Entry(janela, width=10)
caixa1.grid(row=2, column=1, pady=5, sticky="nsew")

caixa2 = Entry(janela, width=10)
caixa2.grid(row=3, column=1, pady=5, sticky="nsew")

# Botão para calcular o IMC
botao = Button(janela, text="Calcular", command=imprimirDados)
botao.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

# Labels para mostrar o IMC calculado e a classificação
MainMsg3 = Label(janela, textvariable=vartx, background="#dde", foreground="black")
MainMsg3.grid(row=5, column=0, columnspan=2, sticky="nsew")

MainMsg4 = Label(janela, textvariable=varty, background="#dde", foreground="black")
MainMsg4.grid(row=6, column=0, columnspan=2, sticky="nsew")

# Ajustar o comportamento das colunas e linhas
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.grid_rowconfigure(6, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# Iniciar a interface gráfica
janela.mainloop()

# Importar do Tkinter
from tkinter import *
# Expressão global
expressao=""
# Definir o que é a calculadora
class Calculadora:
    def __init__(self, mestre):
        mestre.geometry("240x178") # Tamanho do container principal
        operacao=StringVar() # Entrada das strings
        self.botoes=Frame(mestre) # Container dos botões, pertencente ao principal
        self.botoes.grid(row=1, column=0) # Grid do container dos botões, com linha e coluna
        self.botoes.configure(background="black") # Cor do background do container dos botões
        # Entrada dos resultados, com comprimento, largura, cor de fundo e dos caracteres, lado do cursor, tipo de borda
        # e fonte definidos
        self.resultado=Entry(mestre, textvariable=operacao, width=30, bd=15, bg="orange", fg="black", justify="right",
                             relief=FLAT, font=("Arial", "10", "bold"))
        self.resultado.grid(row=0, column=0)
        # Botões da calculadora, pertencentes ao container botoes, com o texto, comprimento, cor de fundo e dos caracteres
        # e o comando de cada um, além do grid com linha e coluna. O comando lambda chama a função "apertar(num)"
        self.botao1=Button(self.botoes, text="1", width=5, fg="White", bg="Black", command=lambda:apertar(1))
        self.botao1.grid(row=0, column=0)
        self.botao2=Button(self.botoes, text="2", width=5, fg="White", bg="Black", command=lambda:apertar(2))
        self.botao2.grid(row=0, column=1)
        self.botao3=Button(self.botoes, text="3", width=5, fg="White", bg="Black", command=lambda:apertar(3))
        self.botao3.grid(row=0, column=2)
        self.botao4=Button(self.botoes, text="4", width=5, fg="White", bg="Black", command=lambda:apertar(4))
        self.botao4.grid(row=1, column=0)
        self.botao5=Button(self.botoes, text="5", width=5, fg="White", bg="Black", command=lambda:apertar(5))
        self.botao5.grid(row=1, column=1)
        self.botao6=Button(self.botoes, text="6", width=5, fg="White", bg="Black", command=lambda:apertar(6))
        self.botao6.grid(row=1, column=2)
        self.botao7=Button(self.botoes, text="7", width=5, fg="White", bg="Black", command=lambda:apertar(7))
        self.botao7.grid(row=2, column=0)
        self.botao8=Button(self.botoes, text="8", width=5, fg="White", bg="Black", command=lambda:apertar(8))
        self.botao8.grid(row=2, column=1)
        self.botao9=Button(self.botoes, text="9", width=5, fg="White", bg="Black", command=lambda:apertar(9))
        self.botao9.grid(row=2, column=2)
        self.botao0=Button(self.botoes, text="0", width=5, fg="White", bg="Black", command=lambda:apertar(0))
        self.botao0.grid(row=3, column=1)
        self.virg=Button(self.botoes, text=",", width=5, fg="White", bg="Black", command=lambda:apertar("."))
        self.virg.grid(row=3, column=2)
        # O botão "sair" tem como comando "self.botoes.quit", para fechar a app
        self.sair = Button(self.botoes, text="Sair", width=8, fg="White", bg="Black")
        self.sair["command"]=self.botoes.quit
        self.sair.grid(row=0, column=3, columnspan=2)
        self.soma=Button(self.botoes, text="+", width=5, fg="White", bg="Black", command=lambda:apertar("+"))
        self.soma.grid(row=1, column=3)
        self.subt=Button(self.botoes, text="-", width=5, fg="White", bg="Black", command=lambda:apertar("-"))
        self.subt.grid(row=1, column=4)
        self.mult=Button(self.botoes, text="x", width=5, fg="White", bg="Black", command=lambda:apertar("*"))
        self.mult.grid(row=2, column=3)
        self.div=Button(self.botoes, text="÷", width=5, fg="White", bg="Black", command=lambda:apertar("/"))
        self.div.grid(row=2, column=4)
        # O botão "igual" chama a função "apertarigual()"
        self.igual=Button(self.botoes, text="=", width=5, fg="White", bg="Black", command=lambda:apertarigual())
        self.igual.grid(row=3, column=3)
        # O botão "apagar" chama a função "limpar()"
        self.apagar=Button(self.botoes, text="C", width=5, fg="White", bg="Black", command=lambda:limpar())
        self.apagar.grid(row=3, column=4)
        self.um_por_x=Button(self.botoes, text="1/x", width=5, fg="White", bg="Black", command=lambda:apertar("1/"))
        self.um_por_x.grid(row=3, column=0)
        self.x_ao_quadrado=Button(self.botoes, text="x²", width=5, fg="White", bg="Black", command=lambda:apertar("**2"))
        self.x_ao_quadrado.grid(row=4, column=0)
        self.x_elevado_y=Button(self.botoes, text="x^y", width=5, fg="White", bg="Black", command=lambda:apertar("**"))
        self.x_elevado_y.grid(row=4, column=1)
        self.raiz=Button(self.botoes, text="√x", width=5, fg="White", bg="Black", command=lambda:apertar("**0.5"))
        self.raiz.grid(row=4, column=2)

        # Definir a função "apertar(num)", para que o botão apertado entre com a string correspondente dele na entrada
        def apertar(num):
            global expressao # Chama a variável global
            expressao=expressao+str(num) # Concatena as entradas
            operacao.set(expressao) # Mostra o valor da string

        # Define a função "apertarigual()", para que, quando pressionado o botão "=", a app mostre o valor da operação
        def apertarigual():
            try:
                global expressao # Chama a variável global
                total=str(eval(expressao)) # Efetua a operação
                operacao.set(total) # Mostra o valor da operação
                expressao="" # Volta ao valor inicial da variável
            except: # Laço em caso de operação inválida, como x/0
                operacao.set("Operação Inválida")
                expressao="" # Volta ao valor inicial da variável

        # Define a função "limpar()", para que, quando pressionado o botão "C", a app limpe a caixa de entrada
        def limpar():
            global expressao # Chama a variável global
            expressao="" # Valor inicial da variável
            operacao.set("") # Limpa a variável

root=Tk() # Através da variável root, foi instanciada a classe Tk(), que permite que os widgets entrem na app
root.configure(background="black") # Muda a cor do background da app
root.title("Calculadora") # Muda o título da janela da app
root.geometry("240x178") # Configura o tamanho da janela da app
Calculadora(root) # A variável root chama a classe Calculadora
root.mainloop() # Método para exibir a tela da app
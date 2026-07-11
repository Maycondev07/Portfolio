import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("calculadora")
janela.geometry("400x500")
janela.configure(bg="#121212")

pagina_inicial = tk.Frame(janela)
pagina_imc = tk.Frame(janela)
pagina_tmb = tk.Frame(janela)
pagina_get = tk.Frame(janela)
pagina_inicial.pack()

tk.Label(pagina_inicial, text="Calculadora nutricional").pack()

tk.Label(pagina_inicial,text="temos varias opções, o que gostaria de calcular?").pack()

def IMC():
    pagina_inicial.pack_forget()
    pagina_imc.pack()  
   
def TMB():
    pagina_inicial.pack_forget()
    pagina_tmb.pack()
    
def GET():
    pagina_inicial.pack_forget()
    pagina_get.pack()
    
def voltar():
    pagina_imc.pack_forget()
    pagina_tmb.pack_forget()
    pagina_get.pack_forget()
    pagina_inicial.pack()

tk.Button(pagina_inicial, text="IMC", command=IMC).pack()
tk.Button(pagina_inicial, text="TMB", command=TMB).pack()
tk.Button(pagina_inicial, text="GET", command=GET).pack()

tk.Label(pagina_imc, text="Para calcularmos o seu IMC precisamos de algumas informações, que são peso e altura").pack()


def imc():
    peso_imc = float(peso_usuario.get())
    altura_imc = float(altura_usuario.get())
    altura_imc /= 100
    resultado = round(peso_imc/(altura_imc*altura_imc),2)
    if resultado <= 18.4:
        aviso['text']= f"Seu IMC é {resultado}, está abaixo do comum"
        aviso['fg']="green"
    elif resultado <= 24.4:
        aviso['text']= f"Seu IMC é {resultado}, está completamente normal"
        aviso['fg']="yellow"
    else:
        aviso['text']= f"Seu IMC é {resultado}, está levemente acima do peso"
        aviso['fg']="red"
    

tk.Label(pagina_imc, text="Peso").pack()
peso_usuario = tk.Entry(pagina_imc)
peso_usuario.pack()

tk.Label(pagina_imc, text="Altura").pack()
altura_usuario = tk.Entry(pagina_imc)
altura_usuario.pack()

tk.Button(pagina_imc, text="enviar", command=imc).pack()

aviso = tk.Label(pagina_imc, text=" ")
aviso.pack()

tk.Button(pagina_imc, text="Voltar", command=voltar).pack()

tk.Label(pagina_tmb, text="Para calcularmos o seu TMB precisamos de algumas informações, como peso, altura, idade e sexo").pack()


def tmb():
    peso_tmb = float(peso_usuario.get())
    altura_tmb = float(altura_usuario.get())
    sexo_tmb = selecao.get()
    idade_tmb = int(idade_usuario.get())
    if sexo_tmb == "Homem":
        resultado_tmb = (6.25*altura_tmb)+(10*peso_tmb)-(5*idade_tmb)+5
        aviso2['text']=f"Sua taxa metabolica basal é de {resultado_tmb} kcal/dia"
    else:
        resultado_tmb = (6.25*altura_tmb)+(10*peso_tmb)-(5*idade_tmb)-161
        aviso2['text']=f"Sua taxa metabolica basal é de {resultado_tmb} kcal/dia"
    
    
tk.Label(pagina_tmb, text="Peso").pack()
peso_usuario = tk.Entry(pagina_tmb)
peso_usuario.pack()

tk.Label(pagina_tmb, text="Altura").pack()
altura_usuario = tk.Entry(pagina_tmb)
altura_usuario.pack()

tk.Label(pagina_tmb, text="Idade").pack()
idade_usuario = tk.Entry(pagina_tmb)
idade_usuario.pack()

tk.Label(pagina_tmb, text="Sexo").pack()
selecao = ttk.Combobox(pagina_tmb, values=["Mulher", "Homem"])
selecao.pack()

tk.Button(pagina_tmb, text="enviar", command=tmb).pack()

aviso2 = tk.Label(pagina_tmb, text=" ")
aviso2.pack()

tk.Button(pagina_tmb, text="Voltar", command=voltar).pack()

tk.Label(pagina_get, text="Para calcularmos o seu GET precisamos de algumas informações, como peso, altura, idade e sexo").pack()


def get():
    peso_get = float(peso_usuario.get())
    altura_get = float(altura_usuario.get())
    sexo_get = selecao.get()
    atividade_get = selecao2.get()
    if atividade_get == "Leve":
        atividade_get = 1
    elif atividade_get == "Moderada":
        atividade_get = 2
    elif atividade_get == "Alta":
        atividade_get = 3
    idade_get = int(idade_usuario.get())
    if sexo_get == "Homem":
        resultado_get = (6.25*altura_get)+(10*peso_get)-(5*idade_get)+5
    else:
        resultado_get = (6.25*altura_get)+(10*peso_get)-(5*idade_get)-161
    if atividade_get == 1:
        resultado_get *= 1.3
    elif atividade_get == 2:
        resultado_get *= 1.5
    elif atividade_get == 3:
        resultado_get *= 1.7
        
    aviso3['text']=f"Seu gasto energetico total é de {resultado_get} kcal/dia"
    
tk.Label(pagina_get, text="Peso").pack()
peso_usuario = tk.Entry(pagina_get)
peso_usuario.pack()

tk.Label(pagina_get, text="Altura").pack()
altura_usuario = tk.Entry(pagina_get)
altura_usuario.pack()

tk.Label(pagina_get, text="Idade").pack()
idade_usuario = tk.Entry(pagina_get)
idade_usuario.pack()

tk.Label(pagina_get, text="Sexo").pack()
selecao = ttk.Combobox(pagina_get, values=["Mulher", "Homem"])
selecao.pack()

tk.Label(pagina_get, text="Nivel de atividade fisíca").pack()
selecao2 = ttk.Combobox(pagina_get, values=["Leve", "Moderada", "Alta"])
selecao2.pack()

tk.Button(pagina_get, text="enviar", command=get).pack()

aviso3 = tk.Label(pagina_get, text=" ")
aviso3.pack()

tk.Button(pagina_get, text="Voltar", command=voltar).pack()

janela.mainloop()
tk.Button(pagina_tmb, text="enviar", command=tmb).pack()

aviso2 = tk.Label(pagina_tmb, text="")
aviso2.pack()

tk.Button(pagina_tmb, text="Voltar", command=voltar).pack()

tk.Label(pagina_get, text="Para calcularmos o seu GET precisamos de algumas informações, como peso, altura, idade e sexo").pack()


def get():
    peso = float(peso_usuario.get())
    altura = float(altura_usuario.get())
    sexo = selecao.get()
    atividade = selecao2.get()
    if atividade == "Leve":
        atividade = 1
    elif atividade == "Moderada":
        atividade = 2
    elif atividade == "Alta":
        atividade = 3
    idade = int(idade_usuario.get())
    if sexo == "Homem":
        resultado = (6.25*altura)+(10*peso)-(5*idade)+5
    else:
        resultado = (6.25*altura)+(10*peso)-(5*idade)+161
    if atividade == 1:
        resultado *= 1.3
    elif atividade == 2:
        resultado *= 1.5
    elif atividade == 3:
        resultado *= 1.7
        
    aviso3['text']=f"Seu gasto energetico total é de {resultado} kcal/dia"
    
tk.Label(pagina_get, text="Peso").pack()
peso_usuario = tk.Entry(pagina_get)
peso_usuario.pack()

tk.Label(pagina_get, text="Altura").pack()
altura_usuario = tk.Entry(pagina_get)
altura_usuario.pack()

tk.Label(pagina_get, text="Idade").pack()
idade_usuario = tk.Entry(pagina_get)
idade_usuario.pack()

tk.Label(pagina_get, text="Sexo").pack()
selecao = ttk.Combobox(pagina_get, values=["Mulher", "Homem"])
selecao.pack()

tk.Label(pagina_get, text="Nivel de atividade fisíca").pack()
selecao2 = ttk.Combobox(pagina_get, values=["Leve", "Moderada", "Alta"])
selecao2.pack()

tk.Button(pagina_get, text="enviar", command=get).pack()

aviso3 = tk.Label(pagina_get, text="")
aviso3.pack()

tk.Button(pagina_get, text="Voltar", command=voltar).pack()

janela.mainloop()

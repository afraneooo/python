from tkinter import *

# funções
def novo():
  codigo.set("")
  desc.set("")

def salvar():
  pass

def cancelar():
  pass

# conf da tela
win = Tk()
win.title("Cadastro de Produtos")
win.geometry("415x345+450+100")
win.configure()

# comp da tela
codigo = IntVar(win)
codigo.set("")
lblcod = Label(win,text="Código do produto:").place(x=15,y=15) 
txtcod = Entry(win,width=18,textvariable=codigo)
txtcod.place(x=15,y=40)
txtcod.configure(justify="right")

desc = StringVar(win)
desc.set("")
lbldesc = Label(win,text="Descrição:").place(x=15,y=60)
txtdesc = Entry(win,width=40,textvariable=desc)
txtdesc.place(x=15,y=85)
txtdesc.configure(justify="right")

marcas = ["A","B","C"]
marca = StringVar(win)
marca.set("Selecione")
lblmarca = Label(win,text="Marca:").place(x=15,y=105)
boxmarca = OptionMenu(win,marca,*marcas)
boxmarca.place(x=15,y=130)

departamentos = ["101","102","103"]
depart = StringVar(win)
depart.set("Selecione")
lbldepart = Label(win,text="Departamento:").place(x=15,y=170)
boxdepart = OptionMenu(win,depart,*departamentos)
boxdepart.place(x=15,y=195)

qtd = IntVar(win)
qtd = ""
lblqtd = Label(win,text="Quantidade estocada:").place(x=15,y=235) 
txtqtd = Entry(win,width=25,textvariable=qtd)
txtqtd.place(x=15,y=260)
txtqtd.configure(justify="right")

preco = DoubleVar(win)
preco = ""
lblpreco = Label(win,text="Preço: (R$)").place(x=15,y=280) 
txtpreco = Entry(win,width=25,textvariable=preco)
txtpreco.place(x=15,y=305)
txtpreco.configure(justify="right")

btnnovo = Button(win,text="Novo",command=novo,width=15)
btnnovo.place(x=280,y=60)

btnsalvar = Button(win,text="Salvar",command=salvar,width=15)
btnsalvar.place(x=280,y=100)

btncanc = Button(win,text="Cancelar",command=cancelar,width=15)
btncanc.place(x=280,y=140)

btnfechar = Button(win,text="Fechar",command=win.destroy,width=15)
btnfechar.place(x=280,y=180)

win.mainloop()
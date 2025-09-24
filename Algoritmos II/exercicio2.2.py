from tkinter import *

def calcular():
  if eta.get()!="" and gas.get()!="":
      etanol = float(eta.get())
      gasolina = float(gas.get())*0.7
      if gasolina > etanol:
        resultado.set("Etanol")
      elif gasolina == etanol:
        resultado.set("Gasolina ou Etanol")
      else:
        resultado.set("Gasolina")

def limpar():
  gas.set(0.0)
  eta.set(0.0)
  resultado.set("")

win = Tk()
win.title("Combustiveís")
win.geometry("250x120+500+250")
win.configure()

gas = DoubleVar()
lblgas = Label(win,text="Preço da Gasolina:").place(x=15,y=15)
txtgas = Entry(win,width=16,textvariable=gas)
txtgas.place(x=130,y=15)

eta = DoubleVar()
lbleta = Label(win,text="Preço da Etanol:").place(x=15,y=35)
txteta = Entry(win,width=16,textvariable=eta)
txteta.place(x=130,y=35)

resultado = StringVar(win)
resultado.set("")
lblabast = Label(win,text=f"Abasteça com:").place(x=15,y=55)
lblresultado = Label(win,textvariable=resultado)
lblresultado.place(x=110,y=55)

btnconverter = Button(win,text="Calcular",command=calcular,width=8)
btnconverter.place(x=15,y=80)

btnlimpar = Button(win,text="Limpar",command=limpar,width=8)
btnlimpar.place(x=90,y=80)

btnsair = Button(win,text="Sair",command=win.destroy,width=8)
btnsair.place(x=170,y=80)

win.mainloop()
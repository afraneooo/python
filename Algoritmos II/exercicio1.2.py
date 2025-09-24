from tkinter import *

# funções do programa

def converter():
  kelvin.set(celsius.get() + 273.15)
  fahrenheit.set(celsius.get()*1.8 + 32)
    
def limpar():
  celsius.set(0.0)
  fahrenheit.set(0.0)
  kelvin.set(0.0)

# conf da tela

win = Tk()
win.title("Conversor de temperaturas")
win.geometry("500x200+400+250")
win.configure()

# componentes da tela

celsius = DoubleVar(win)
lblcelsius = Label(win, text="Temperatura em Celsius:").place(x=15,y=15)
txtcelsius = Entry(win,width=76,textvariable=celsius)
txtcelsius.place(x=18,y=40)

fahrenheit = DoubleVar(win)
lblfahrenheit = Label(win,text="Temperatura em Fahrenheit:").place(x=15,y=60)
txtfahrenheit = Entry(win,width=76,textvariable=fahrenheit,state="disabled")
txtfahrenheit.place(x=18,y=85)

kelvin = DoubleVar(win)
lblkelvin = Label(win,text="Temperatura em Kelvin:").place(x=15,y=105)
txtkelvin = Entry(win,width=76,textvariable=kelvin,state="disabled")
txtkelvin.place(x=18,y=130)

btnconverter = Button(win,text="Converter",command=converter,width=10)
btnconverter.place(x=18,y=160)

btnlimpar = Button(win,text="Limpar",command=limpar,width=10)
btnlimpar.place(x=200,y=160)

btnsair = Button(win,text="Sair",command=win.destroy,width=10)
btnsair.place(x=400,y=160)

win.mainloop()
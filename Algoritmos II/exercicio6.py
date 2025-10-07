from tkinter import *
from tkinter import ttk
from utils import localizar_endereço, municipios_por_estado, listar_estados

# montagem da tela

win = Tk()
largura_tela = win.winfo_screenwidth()
altura_tela = win.winfo_screenheight()
largura_win = 670
altura_win = 400

pos_x = (largura_tela - largura_win)/2
pos_y = (altura_tela - altura_win)/2

win.title("Cadastro de Clientes")
win.geometry("%dx%d+%d+%d"%(largura_win,altura_win,pos_x,pos_y)) # Sempre centralizado
win.configure(bg="#281766")

# funcoes

def popular_cidades():
  global cidades
  cidades = municipios_por_estado(estado.get())

def buscar_endereco():
  dados_end = localizar_endereço(cep.get())
  if dados_end:
    endereco.set(dados_end["logradouro"])
    bairro.set(dados_end["bairro"])
    cidade.set(dados_end["localidade"])
    estado.set(dados_end["uf"])

def pesquisar():
  pass

def habilitar():
  txtemail.configure(state="normal")
  txtnome.configure(state="normal")
  txtbairro.configure(state="normal")
  txtcelular.configure(state="normal")
  txtcep.configure(state="normal")
  txtendereco.configure(state="normal")
  txtnumero.configure(state="normal")
  txttelefone.configure(state="normal")
  bttnest_cv.configure(state="normal")
  bttnest_cv2.configure(state="normal")
  bttnocupacao.configure(state="normal")
  bttnocupacao2.configure(state="normal")
  cbogenero.configure(state="normal")
  cboestado.configure(state="normal")
  cbocidade.configure(state="normal")
  bttnpesq.configure(state="normal")
  bttnbuscar.configure(state="normal")
  btncancelar.configure(state="normal")
  btnexcluir.configure(state="normal")
  btnsalvar.configure(state="normal")

  btnnovo.configure(state="disabled")
  


def desabilitar():
  txtemail.configure(state="disabled")
  txtnome.configure(state="disabled")
  txtbairro.configure(state="disabled")
  txtcelular.configure(state="disabled")
  txtcep.configure(state="disabled")
  txtendereco.configure(state="disabled")
  txtnumero.configure(state="disabled")
  txttelefone.configure(state="disabled")
  bttnest_cv.configure(state="disabled")
  bttnest_cv2.configure(state="disabled")
  bttnocupacao.configure(state="disabled")
  bttnocupacao2.configure(state="disabled")
  cbogenero.configure(state="disabled")
  cboestado.configure(state="disabled")
  cbocidade.configure(state="disabled")
  bttnpesq.configure(state="disabled")
  bttnbuscar.configure(state="disabled")
  btncancelar.configure(state="disabled")
  btnexcluir.configure(state="disabled")
  btnsalvar.configure(state="disabled")

  btnnovo.configure(state="normal")

def limpar():
  email.set("")
  nome.set("")
  est_cv.set(0)
  estuda.set(False)
  trabalha.set(False)
  genero.set("")
  cep.set("")
  endereco.set("")
  numero.set("")
  bairro.set("")
  cidade.set("")
  estado.set("")
  telefone.set("")
  celular.set("")

def inserir():
  habilitar()
  limpar()

def salvar():
  # validar os campos
  # gravar no bd
  limpar()

def cancelar():
  limpar()

def excluir():
  limpar()

# componentes da tela

email = StringVar(win)
lblemail = Label(win,text="Email:",bg="#281766",fg="#ffffff").place(x=15,y=15)
txtemail = Entry(win,textvariable=email,width=35)
txtemail.place(x=100,y=15)

bttnpesq = Button(win,text="...",command=pesquisar,width=2)
bttnpesq.place(x=320,y=13)

telefone = StringVar(win)
lbltelefone = Label(win,text="Telefone:",bg="#281766",fg="#ffffff").place(x=350,y=15)
txttelefone = Entry(win,textvariable=telefone,width=40)
txttelefone.place(x=410,y=15)

nome = StringVar(win)
lblnome = Label(win,text="Nome:",bg="#281766",fg="#ffffff").place(x=15,y=45)
txtnome = Entry(win,textvariable=nome,width=40)
txtnome.place(x=100,y=45)

celular = StringVar(win)
lblcelular = Label(win,text="Celular:",bg="#281766",fg="#ffffff").place(x=350,y=45)
txtcelular = Entry(win,textvariable=celular,width=40)
txtcelular.place(x=410,y=45)

est_cv = BooleanVar(win)
lblest_cv = Label(win,text="Estado Civil:",bg="#281766",fg="#ffffff").place(x=15,y=77)
bttnest_cv = Radiobutton(win,text="Casado",variable=est_cv,value=1)
bttnest_cv.place(x=100,y=75)
bttnest_cv2 = Radiobutton(win,text="Solteiro",variable=est_cv,value=2)
bttnest_cv2.place(x=180,y=75)

estuda = BooleanVar(win)
trabalha = BooleanVar(win)
lblocupacao = Label(win,text="Ocupação:",bg="#281766",fg="#ffffff").place(x=250,y=77)
bttnocupacao = Checkbutton(win,text="Estuda",variable=estuda)
bttnocupacao.place(x=320,y=75)
bttnocupacao2 = Checkbutton(win,text="Trabalha",variable=trabalha)
bttnocupacao2.place(x=380,y=75)

genero = StringVar(win)
generos = ["Masculino","Feminino","Não binário","Prefiro não dizer"]
lblgenero = Label(win,text="Gênero:",bg="#281766",fg="#ffffff").place(x=470,y=75)
cbogenero = ttk.Combobox(win,textvariable=genero,values=generos,width=18)
cbogenero.place(x=525,y=74)

cep = StringVar(win)
lblcep = Label(win,text="Cep:",bg="#281766",fg="#ffffff").place(x=15,y=108)
txtcep = Entry(win,textvariable=cep,width=15)
txtcep.place(x=100,y=108)

estado = StringVar(win)
estados = listar_estados()
lblestado = Label(win,text="Estado:",bg="#281766",fg="#ffffff").place(x=290,y=105)
cboestado = ttk.Combobox(win,textvariable=estado,values=estados,width=4)
cboestado.place(x=340,y=106)

cidade = StringVar(win)
cidades = []
lblcidade = Label(win,text="Cidade:",bg="#281766",fg="#ffffff").place(x=390,y=105)
cbocidade = ttk.Combobox(win,textvariable=cidade,values=cidades,width=32)
cbocidade.place(x=440,y=106)

bttnbuscar = Button(win,text="Buscar",command=buscar_endereco,width=10)
bttnbuscar.place(x=200,y=104)

endereco = StringVar(win)
lblendereco = Label(win,text="Endereço:",bg="#281766",fg="#ffffff").place(x=15,y=140)
txtendereco = Entry(win,textvariable=endereco,width=30)
txtendereco.place(x=100,y=140)

bairro = StringVar(win)
lblbairro = Label(win,text="Bairro:",bg="#281766",fg="#ffffff").place(x=290,y=140)
txtbairro = Entry(win,textvariable=bairro,width=30)
txtbairro.place(x=340,y=140)

numero = StringVar(win)
lblnumero = Label(win,text="Número:",bg="#281766",fg="#ffffff").place(x=530,y=140)
txtnumero = Entry(win,textvariable=numero,width=10)
txtnumero.place(x=590,y=140)

btnnovo = Button(win, text="Novo", command=inserir, width=10)
btnnovo.place(x=40, y=180)
btnsalvar = Button(win, text="Salvar", command=salvar, width=10)
btnsalvar.place(x=160, y=180)
btncancelar = Button(win, text="Cancelar", command=cancelar, width=10)
btncancelar.place(x=290, y=180)
btnexcluir = Button(win, text="Excluir", command=excluir, width=10)
btnexcluir.place(x=420, y=180)
btnsair = Button(win, text="Sair", command=win.destroy, width=10)
btnsair.place(x=550, y=180)

desabilitar()

win.mainloop()



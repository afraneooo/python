'''
Cadastro: Clientes
'''
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from utils import localizar_endereco, municipios_por_estado

global novo
novo = True

# funções
def buscar_endereco():
  dados_end = localizar_endereco(cep.get())
  if dados_end:
    endereco.set(dados_end['logradouro'])
    bairro.set(dados_end['bairro'])
    cidade.set(dados_end['localidade'])
    estado.set(dados_end['uf'])
    print(dados_end['localidade'])

def habilitar():
  txtemail.configure(state='normal')
  txtnome.configure(state='normal')
  optcasado.configure(state='normal')
  optsolteiro.configure(state='normal')
  chkestuda.configure(state='normal')
  chktrabalha.configure(state='normal')
  cbogenero.configure(state='normal')
  txtcep.configure(state='normal')
  txtendereco.configure(state='normal')
  txtnumero.configure(state='normal')
  txtbairro.configure(state='normal')
  cboestado.configure(state='normal')
  cbocidade.configure(state='normal')
  txttelefone.configure(state='normal')
  btnbuscar.configure(state='normal')
  btnpesquisar.configure(state='disabled')
  btnnovo.configure(state='disabled')
  btnsalvar.configure(state='normal')
  btncancelar.configure(state='normal')

def desabilitar():
  txtemail.configure(state='disabled')
  txtnome.configure(state='disabled')
  optcasado.configure(state='disabled')
  optsolteiro.configure(state='disabled')
  chkestuda.configure(state='disabled')
  chktrabalha.configure(state='disabled')
  cbogenero.configure(state='disabled')
  txtcep.configure(state='disabled')
  txtendereco.configure(state='disabled')
  txtnumero.configure(state='disabled')
  txtbairro.configure(state='disabled')
  cboestado.configure(state='disabled')
  cbocidade.configure(state='disabled')
  txttelefone.configure(state='disabled')
  btnbuscar.configure(state='disabled')
  btnpesquisar.configure(state='normal')
  btnnovo.configure(state='normal')
  btnsalvar.configure(state='disabled')
  btncancelar.configure(state='disabled')
  btnexcluir.configure(state='disabled')

def limpar():
  email.set("")
  nome.set("")
  estado_civil.set("solteiro")
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

def atualizar_cidades(event):
  estado_selecionado = cboestado.get()
  lista_cidades = municipios_por_estado(estado_selecionado)
  cbocidade["values"]=lista_cidades

def inserir():
  habilitar()

def salvar():
  if txtemail.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo email é obrigatório")
    txtemail.focus_set()
  elif txtnome.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo nome é obrigatório")
    txtnome.focus_set()
  elif cbogenero.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo gênero é obrigatório")
    cbogenero.focus_set()
  elif txtcep.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo CEP é obrigatório")
    txtcep.focus_set()
  elif txtendereco.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo endereço é obrigatório")
    txtendereco.focus_set()
  elif txtnumero.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo número é obrigatório")
    txtnumero.focus_set()
  elif txtbairro.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo bairro é obrigatório")
    txtbairro.focus_set()
  elif cboestado.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo estado é obrigatório")
    cboestado.focus_set()
  elif cbocidade.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo cidade é obrigatório")
    cbocidade.focus_set()
  elif txttelefone.get()=="":
    messagebox.showwarning(title="Validação", message="O Campo telefone é obrigatório")
    txttelefone.focus_set()
  else:
    # entra aqui os comandos insert ou update no banco de dados
    global novo
    if novo:
      # comando INSERT
      messagebox.showinfo(title="Sucesso", message="Registro incluido com sucesso!")
    else:
      # comando UPDATE
      messagebox.showinfo(title="Sucesso", message="Dados atualizados com sucesso!")
      novo = True
    limpar()
    desabilitar()

def cancelar():
  limpar()
  desabilitar()

def excluir():
  resposta = messagebox.askokcancel("Exclusão", "Tem certeza que deseja excluir?")
  if resposta:
    # aqui entra o comando DELETE
    messagebox.showinfo(title="Sucesso", message="Registro excluido com sucesso!")
    limpar()
    desabilitar()

def pesquisar():
  resposta = simpledialog.askstring("Pesquisa", "Digite o email do cliente:")
  # buscar o email digitado na tabela do banco de dados com o SELECT
  global novo
  novo = False
  habilitar()
  btnexcluir.configure(state='normal')

# montagem da tela
janela = Tk()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
largura_janela = 750
altura_janela = 400
pos_x = (largura_tela - largura_janela) / 2
pos_y = (altura_tela - altura_janela) / 2
janela.title("Cadastro de Clientes")
janela.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, pos_x, pos_y))
janela.configure(bg="#2E3604")

# componentes da tela
email = StringVar(janela)
lblemail = Label(janela, text="Email*:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=30, y=30)
txtemail = Entry(janela, width=35, textvariable=email, font=("Arial", 12))
txtemail.place(x=30, y=55)
btnpesquisar = Button(janela, text="Pesquisar", command=pesquisar, width=10)
btnpesquisar.place(x=365, y=55)

nome = StringVar(janela)
lblnome = Label(janela, text="Nome*:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=30, y=85)
txtnome = Entry(janela, width=35, textvariable=nome, font=("Arial", 12))
txtnome.place(x=30, y=110)

estado_civil = StringVar(value="solteiro")
lblestado_civil = Label(janela, text="Estado civil:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=30, y=140)
optsolteiro = Radiobutton(janela, text="Solteiro", variable=estado_civil, value="solteiro", font=("Arial", 12))
optsolteiro.place(x=30, y=165)
optcasado = Radiobutton(janela, text="Casado", variable=estado_civil, value="casado", font=("Arial", 12))
optcasado.place(x=130, y=165)

estuda = BooleanVar(janela)
trabalha = BooleanVar(janela)
lblocupacao = Label(janela, text="Ocupação:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=250, y=140)
chkestuda = Checkbutton(janela, text="Estuda", variable=estuda, font=("Arial", 12))
chkestuda.place(x=250, y=165)
chktrabalha = Checkbutton(janela, text="Trabalha", variable=trabalha, font=("Arial", 12))
chktrabalha.place(x=350, y=165)

genero = StringVar(janela)
lblgenero = Label(janela, text="Gênero:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=500, y=140)
lista_generos = ["Masculino", "Feminino", "Outro", "Prefiro não dizer"]
cbogenero = ttk.Combobox(janela, values=lista_generos, textvariable=genero, background="#2E3604", foreground="#FDFDFD", font=("Arial", 12))
cbogenero.place(x=500, y=165)

cep = StringVar(janela)
lblcep = Label(janela, text="CEP:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=30, y=195)
txtcep = Entry(janela, width=12, textvariable=cep, font=("Arial", 12))
txtcep.place(x=30, y=220)

btnbuscar = Button(janela, text="Buscar", command=buscar_endereco, width=10)
btnbuscar.place(x=150, y=220)

endereco = StringVar(janela)
lblendereco = Label(janela, text="Endereço:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=250, y=195)
txtendereco = Entry(janela, width=35, textvariable=endereco, font=("Arial", 12))
txtendereco.place(x=250, y=220)

numero = StringVar(janela)
lblnumero = Label(janela, text="Número:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=590, y=195)
txtnumero = Entry(janela, width=12, textvariable=numero, font=("Arial", 12))
txtnumero.place(x=590, y=220)

bairro = StringVar(janela)
lblbairro = Label(janela, text="Bairro:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=30, y=250)
txtbairro = Entry(janela, width=18, textvariable=bairro, font=("Arial", 12))
txtbairro.place(x=30, y=275)

estado = StringVar(janela)
lblestado = Label(janela, text="Estado:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=220, y=250)
lista_estados = ["ES", "MG", "SP", "RJ"]
cboestado = ttk.Combobox(janela, textvariable=estado, values=lista_estados, font=("Arial", 12), width=6)
cboestado.place(x=220, y=275)
cboestado.bind("<<ComboboxSelected>>", atualizar_cidades)

cidade = StringVar(janela)
lista_cidades = municipios_por_estado(estado.get())
lblcidade = Label(janela, text="Cidade:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=320, y=250)
cbocidade = ttk.Combobox(janela, textvariable=cidade, values=lista_cidades, font=("Arial", 12), width=15)
cbocidade.place(x=320, y=275)

telefone = StringVar(janela)
lbltelefone = Label(janela, text="Telefone:", bg="#2E3604", fg="#FDFDFD", font=("Arial", 12)).place(x=500, y=250)
txttelefone = Entry(janela, width=22, textvariable=telefone, font=("Arial", 12))
txttelefone.place(x=500, y=275)

btnnovo = Button(janela, text="Novo", command=inserir, width=10)
btnnovo.place(x=30, y=340)
btnsalvar = Button(janela, text="Salvar", command=salvar, width=10)
btnsalvar.place(x=130, y=340)
btncancelar = Button(janela, text="Cancelar", command=cancelar, width=10)
btncancelar.place(x=230, y=340)
btnexcluir = Button(janela, text="Excluir", command=excluir, width=10)
btnexcluir.place(x=330, y=340)
btnsair = Button(janela, text="Sair", command=janela.destroy, width=10)
btnsair.place(x=430, y=340)

desabilitar()

janela.mainloop()
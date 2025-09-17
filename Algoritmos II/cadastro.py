import FreeSimpleGUI as gui

gui.theme("Default")
gui.set_options(font=("Verdana",10,"bold"))

civil = ["Solteiro","Casado","Divorciado","Viúvo"]

layout = [  [gui.Text("",s=(75))],
            [gui.Text("",s=(2)),gui.Text("Nome:",s=(6)),gui.InputText(k="nome",s=(56))],
            [gui.Text("",s=(2)),gui.Text("CPF:",s=(6)),gui.InputText(k="cpf",s=(24)),gui.Text("RG:",s=(5)),gui.InputText(k="rg",s=(24))],
            [gui.Text("",s=(2)),gui.Text("Sexo:",s=(6)),gui.Radio("Feminino",group_id="sexo",k="fem"),gui.Radio("Masculino",group_id="sexo",k="masc"),
             gui.Text("",s=(2)),gui.Text("Telefone:"),gui.InputText(k="tel",s=(18))],
            [gui.Text("",s=(2)),gui.Text("Modelo de trabalho:"),gui.Checkbox("CLT",k="clt"),gui.Checkbox("PJ",key="pj"),gui.Checkbox("Estágio",k="est"),
             gui.Text("Estado Civil:"),gui.Combo(civil,default_value=None,k="civil")],
            [gui.Text("",s=(2)),gui.Button("Novo"),gui.Text("",s=(4)),gui.Button("Salvar"),gui.Text("",s=(4)),gui.Button("Cancelar"),gui.Text("",s=(4)),gui.Button("Excluir"),gui.Text("",s=(4)),gui.Button("Sair")]]

win = gui.Window("Cadastro",layout)

while True:
  event, values = win.read()
  if event==gui.WIN_CLOSED or event=="Sair":
    break
  elif event=="Salvar":
    print("Nome:")
    print(values["nome"])
    print("")
    print("CPF:")
    print(values["cpf"])
    print("")
    print("Telefone:")
    print(values["tel"])
    print("")
    print("RG:")
    print(values["rg"])
    print("")
    print("Sexo:")
    if values["fem"]:
      print("Feminino")
    else:
      print("Masculino")
    print("")
    print("Modelo(s) de trabalho desejado:")
    if (values["clt"]):
      print("CLT")
    if (values["pj"]):
      print("PJ")
    if (values["est"]):
      print("Estágio")
    print("")
    print("Estado Civil:")
    print(values["civil"])
    win["nome"].update("")
    win["cpf"].update("")
    win["tel"].update("")
    win["rg"].update("")
    win["fem"].update(False)
    win["masc"].update(False)
    win["clt"].update(False)
    win["pj"].update(False)
    win["est"].update(False)
    win["civil"].update("")

win.close()


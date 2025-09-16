import FreeSimpleGUI as gui

gui.theme("DarkBlue")

vagas = ["Auxiliar Administrativo","Técnico de Informática","Recepcionista","Assistente de RH"]

layout = [  [gui.Text("")],
            [gui.Text("CPF:")],
            [gui.InputText(key="cpf",size=(20,10))],[gui.Text("")],
            [gui.Text("Nome:",size=(25)),gui.Text("Email:")],
            [gui.InputText(key="nome",size=(29)),gui.InputText(key="email",size=(20,10))],[gui.Text("")],
            [gui.Text("Disponibilidade:")],
            [gui.Checkbox("Manhã",k="manha"),gui.Checkbox("Tarde",k="tarde"),gui.Checkbox("Noite",k="noite")],
            [gui.Text("")],[gui.Text("Vaga Desejada:")],
            [gui.Combo(vagas,default_value=None,k="vaga")],
            [gui.Text("")],[gui.Button("Candidatar-se",k="cand"),gui.Text("",s=(10)),gui.Button("Desistir",s=(8)),gui.Text("",s=(10)),gui.Button("Sair",s=(8))]]

win = gui.Window("Cadastro de candidatos",layout)

while True:
  event, values = win.read()
  if event==gui.WIN_CLOSED or event=="Sair":
    break
  elif event=="cand":
    vaga = values["vaga"]
    lay2 = [  [gui.Text(f"Vaga Escolhida: {vaga}")]]
    win2 = gui.Window("Sucesso!",lay2)
    while True:
      event,values = win2.read()
      if event==gui.WIN_CLOSED:
        break
  elif event=="Desistir":
    win["cpf"].update("")
    win["nome"].update("")
    win["email"].update("")
    win["manha"].update(False)
    win["tarde"].update(False)
    win["noite"].update(False)
    win["vaga"].update("")

win.close()
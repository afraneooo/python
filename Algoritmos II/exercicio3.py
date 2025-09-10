import FreeSimpleGUI as gui

gui.theme("DarkBlue18")

layout = [  [gui.Text("Informe o gênero:")],
            [gui.Text("Selecione:"),gui.Radio("Feminino",group_id="sexo",key="fem"),gui.Radio("Masculino",group_id="sexo",key="masc")],
            [gui.Text("Altura:"),gui.InputText(key="alt",size=(27,10))],
            [gui.Text("Peso ideal:"),gui.Text("",key="res")],
            [gui.Button("Calcular"),gui.Button("Limpar"),gui.Button("Fechar")]]

win = gui.Window("Peso Ideal",layout)

while True:
  event, values = win.read()
  if event==gui.WIN_CLOSED or event=="Fechar":
    break
  elif event == "Calcular":
    if values["alt"]!="":
      if values["masc"]:
        win["res"].update(f"{(float(values["alt"])*72.7)-58:.2f} Kg")
      elif values["fem"]:
        win["res"].update(f"{(float(values["alt"])*62.1)-44.7:.2f} Kg")
      else:
        win["res"].update("Selecione um sexo")
  elif event=="Limpar":
    win["res"].update("")
    win["fem"].update(value=False)
    win["masc"].update(value=False)
    win["alt"].update("")

win.close()
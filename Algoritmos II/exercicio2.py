import FreeSimpleGUI as gui

gui.theme("DarkBlue")

layout = [  [gui.Text("Preço da gasolina:",tooltip="Digite aqui"),gui.InputText(key="gas",size=(10,10))],
            [gui.Text("Preço do etanol:   ",tooltip="Digite aqui"),gui.InputText(key="eta",size=(10,10))],
            [gui.Text("Abasteça com:     "),gui.InputText(key="res",disabled=True,size=(20,20),text_color="black")],
            [gui.Button("Avaliar"),gui.Button("Limpar"),gui.Button("Fechar")]]
win = gui.Window("Combustíveis",layout)

while True:
  event, values = win.read()
  if event==gui.WIN_CLOSED or event=="Fechar":
    break
  elif event=="Avaliar":
    if values["eta"]!="" and values["gas"]!="":
      etanol = float(values["eta"])
      gasolina = float(values["gas"])*0.7
      if gasolina > etanol:
        win["res"].update("Etanol")
      elif gasolina == etanol:
        win["res"].update("Gasolina ou Etanol")
      else:
        win["res"].update("Gasolina")
  elif event=="Limpar":
    win["res"].update("")
    win["eta"].update("")
    win["gas"].update("")
    win["gas"].SetFocus()

win.close()

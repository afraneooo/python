import FreeSimpleGUI as gui

gui.theme("Dark")

layout = [ [gui.Text("Conversor de temperaturas!")],
           [gui.Text("Cº:"),gui.InputText(key="cel"),gui.Text("Fº:"),gui.InputText(key="fa"),gui.Text("Kelvin:"),gui.InputText(key="kel")],
           [gui.Button("Converter"),gui.Button("Limpar"),gui.Button("Sair")]]

janela = gui.Window("Conversor de temperaturas",layout)

while True:
  event, values = janela.read()
  if event == gui.WIN_CLOSED or event == "Sair":
    break
  elif event == "Converter":
    if (values["cel"])!="":
      kelvin = float(values["cel"])+273.15
      fah = float(values["cel"])+32
      janela["kel"].update(kelvin)
      janela["fa"].update(fah)
    elif (values["kel"])!="":
      celsius = float(values["kel"])-273.15
      fah = float(values["kel"])+32-273.15
      janela["cel"].update(celsius)
      janela["fa"].update(fah)
    elif (values["fa"])!="":
      celsius = float(values["fa"])-32
      kelvin = float(values["fa"])-32+273.15
      janela["cel"].update(celsius)
      janela["kel"].update(kelvin)
  elif event == "Limpar":
    janela["cel"].update("")
    janela["kel"].update("")
    janela["fa"].update("")
    
janela.close()

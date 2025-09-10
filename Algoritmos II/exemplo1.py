import FreeSimpleGUI as sg

#É pra selecionar um tema para a janela
sg.theme("Dark")

layout = [  [sg.Text("Número 1:"),sg.InputText(key="n1")],
            [sg.Text("Número 2"),sg.InputText(key="n2")],
            [sg.Text("Resultado"),sg.InputText(key="resultado",disabled=True)],
            [sg.Button("Calcular"),sg.Button("Limpar"),sg.Button("Cancelar")]]

#Criar janela
janela = sg.Window("Janela teste",layout)
#Laço indefinido para a janela ficar aberta
while True:
  event, values = janela.read()
  if event == sg.WIN_CLOSED or event == "Cancelar": #Se o usuário fechar a janela
    break
  elif event == "Calcular":
    res = float(values["n1"])+float(values["n2"])
    janela["resultado"].update(res)
  elif event == "Limpar":
    janela["n1"].update()
    janela["n2"].update()
    janela["resultado"].update()

janela.close()
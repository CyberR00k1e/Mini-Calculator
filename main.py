import PySimpleGUI as sg
import function


window = sg.Window("POC Tracking App", layout=[""])
button=sg.Button("Add")
text=sg.InputText()
window.read()
window.close()


import PySimpleGUI as sg
import function


button=sg.Button("Add")
label=sg.InputText("Please provide 2 numbers below with space between them", key="number")
input=sg.InputText(key="inputs")
label2=sg.Text("Output", key="output")
window = sg.Window("Calculator", layout=[[button],[label],[input],[label2]])


while True:
    event, value = window.read()
    r = function.test(int(value["inputs"][0]), int(value["inputs"][2]))
    match event:
            case Add:
                window["output"].update(value=r)


window.close()


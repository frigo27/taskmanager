from tkinter import Button, Frame
import PySimpleGUI as sg

def criar_item_tarefa():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container' )],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]    
    
    return sg.Window('Todo List', layout=layout, finalize=True)

janela = criar_item_tarefa()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_item_tarefa()

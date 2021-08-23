from PySimpleGUI import PySimpleGUI as sg
import time
tema = sg.theme('Reddit')

def sucesso():
    tema = sg.theme('Reddit')
    layout = [
        [sg.Text('Success!',font='Roboto',size=(20,30))]
    ]
    janela1 = sg.Window('Successful',layout,size=(100,50))
    while True:
        event,values = janela1.Read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break



    janela1.Close()


layout = [
    [sg.Text('Username',font='Roboto',size=(15,0))],
    [sg.Input(font='Roboto',size=(100,70),key='name')],
    [sg.Text('Password',font='Roboto',size=(15,0))],
    [sg.Input(font='Roboto',size=(100,70),password_char='*',key='passw')],
    [sg.Button('Confirm',font='Roboto',auto_size_button=(20,20),key='btn')]
]
janela = sg.Window('Login',layout,size=(300,270))
while True:
    event,values = janela.Read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'btn':
        if values['passw'] == 'password' and values['name'] == 'username':
            sucesso()
janela.Close()
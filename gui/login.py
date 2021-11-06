import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('User', size = (10, 0)), sg.Input(size = (15, 0), key = 'user')],
    [sg.Text('Password', size = (10, 0)), sg.Input(size = (15, 0), key = 'password', password_char='*')],
    [sg.Checkbox('Save Login?')],
    [sg.Button('Enter')]
]
# Window
window = sg.Window('Login', layout)

#Read the events
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Enter':
        if values['user'] == 'Paulo' and values['password'] == 'Pr3246278':
            print('Bem vindo, Paulo!')

import PySimpleGUI as sg

class ClothPython:
    def __init__(self):
        #Layout
        sg.theme('Reddit')
        layout = [
            [sg.Text('User', size = (10, 0)), sg.Input(size = (15, 0), key = 'user')],
            [sg.Text('Email', size = (10, 0)), sg.Input(size = (15, 0), key = 'email')],
            [sg.Text('which email providers are accepted?')],
            [sg.Checkbox('Gmail', key = 'gmail'), sg.Checkbox('Outlook', key = 'outlook'), sg.Checkbox('Yahoo', key = 'yahoo')],
            [sg.Button('Send data')],
            [sg.Output(size = (30, 20))]
        ]
        #Window
        self.window = sg.Window("User data").layout(layout)

    def Start(self):
        while True:
            #Extract data frm the screen
            self.button, self.values = self.window.Read()
            user = self.values['user']
            email = self.values['email']
            accept_gmail = self.values['gmail']
            accept_outlook = self.values['outlook']
            accept_yahoo = self.values['yahoo']

            print(f'User: {user}')
            print(f'Email: {email}')
            print(f'Accept Gmail: {accept_gmail}')
            print(f'Accept Outlook: {accept_outlook}')
            print(f'Accept Yahoo: {accept_yahoo}')

cloth = ClothPython()
cloth.Start()

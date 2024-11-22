import PySimpleGUI as sg
import matplotlib.pyplot as plt

class Gui:
    
    def __init__(self):
        self.__setup__()
        
    def __setup__(self):
        layout = [[sg.Text("File path"), sg.FileBrowse()],
                [sg.Text("this section will be used for plotting")],
                [sg.Button("plot")],
                [sg.Button("exit")]]
        
        window = sg.Window("Plot app", layout=layout)

        def run(self):
            while True:
                event, value = window.read()

                print(event, value)
                
                if event == sg.WIN_CLOSED or event == 'exit':
                    break
            
            window.close()
    
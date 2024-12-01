import PySimpleGUI as sg
import matplotlib.pyplot as plt

class Gui:
    
    def __init__(self):
        self.path = None
        self.__setup()
        
    def __setup(self):
        layout = [[sg.Text("path"), sg.Input(enable_events=True, key='-FILE-'),sg.FileBrowse(file_types=(("CSV", "*.csv"),
                                                                                                        ("txt", "*.txt")))],
                [sg.Text("this section will be used for plotting")],
                [sg.Button("plot")],
                [sg.Button("exit")]]
        
        self.window = sg.Window("Plot app", layout=layout)

    def run(self):
        while True:
            event, value = self.window.read()

            print(f"event {event} \nvalue {value}")
            
            if event == sg.WIN_CLOSED or event == 'exit':
                break
            
            if event == '-FILE-':
                self.path = value.get("-FILE-")
                
        
        self.window.close()

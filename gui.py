import PySimpleGUI as sg
from plot import Ploter

class Gui:
    
    def __init__(self):
        self.plotter = Ploter()
        self.__setup()
        
    def __setup(self):
        layout = [[sg.Text("path"), sg.Input(enable_events=True, key='-FILE-'),sg.FileBrowse(file_types=(("CSV", "*.csv"),
                                                                                                        ("txt", "*.txt")))],
                [sg.Text("this section will be used for plotting")],
                [sg.Button("Load", key='-LOAD-'), sg.Button("plot", disabled=True, key="-PLOT-")],
                [sg.Button("exit")]]
        
        self.window = sg.Window("Plot app", layout=layout)

    def run(self):
        while True:
            event, value = self.window.read()

            print(f"event {event} \nvalue {value}")
            
            if event == sg.WIN_CLOSED or event == 'exit':
                break
            
            if event == '-LOAD-':
                try:
                    self.plotter.load_data(value.get("-FILE-"))
                except FileNotFoundError:
                    sg.popup_error("File not found")
                    continue
                else:
                    self.window["-PLOT-"].update(disabled=False)
                
            if event == "-PLOT-":
                self.plotter.plot()
        
        self.window.close()

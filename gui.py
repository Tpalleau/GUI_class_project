import PySimpleGUI as sg
import matplotlib.pyplot as plt

def setup():
    layout = [[sg.Text("File path"), sg.FileBrowse()],
              [sg.Text("this section will be used for plotting")],
              [sg.Button("plot")],
              [sg.Button("exit")]]
    
    window = sg.Window("Plot app", layout=layout)

    while True:
        event, value = window.read()

        print(event, value)
        
        if event == sg.WIN_CLOSED or event == 'exit':
            break
    
    window.close()

if __name__ == "__main__":
    setup()
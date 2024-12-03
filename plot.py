import matplotlib.pyplot as plt
import pandas as pd
from logging import log

class Ploter:
    
    def __init__(self):
        self.data: pd.DataFrame
    
    def is_data_loaded(self):
        return bool(self.data)
    
    def load_data(self, path):
        self.data = pd.read_csv(path)
    
    def plot(self, colx=0, coly=1):
        print(self.data)
        plot = self.data.plot()
        plt.show(block=False)

        
    
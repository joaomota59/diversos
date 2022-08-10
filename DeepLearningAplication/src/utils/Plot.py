import progressbar
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import numpy as np

bar_widgets = [
    'Training ', 
    progressbar.Percentage(), 
    ' ', 
    progressbar.Bar(marker = "-", left = "[", right = "]"),
    ' ', progressbar.ETA()
]

class Plot():
    def __init__(self):
        self.cmap = plt.get_cmap('viridis')
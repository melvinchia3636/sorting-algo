#import lib
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import matplotlib

#selection sort
class selection_sort:

    #initialize
    def __init__(self):
        self.titlefont = {'fontsize':30, 'fontfamily':'Bahnschrift'}
        self.subtitlefont = {'fontsize':20, 'fontfamily':'Bahnschrift'}

    #plot style
    def plot(self, arr):
        plt.ion()
        self.arr = arr
        self.i=0
        self.n = len(self.arr)
        self.fig = plt.figure()
        self.line, = plt.plot(self.arr)
        for i in range(self.n):
            self.temp2 = self.arr[i:]
            self.minval =  min(self.temp2)
            self.arr.remove(self.minval)
            self.arr.insert(self.i, self.minval)
            self.line.set_ydata(self.arr)
            self.i+=1
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    #bar style 
    def bar(self, arr):
        plt.ion()
        self.arr = arr
        self.i=0
        self.n = len(self.arr)
        self.fig = plt.figure()
        self.rects = plt.bar([i for i in range(250)], self.arr, width=1.0)
        for i in range(self.n):
            self.temp2 = self.arr[i:]
            self.minval =  min(self.temp2)
            self.arr.remove(self.minval)
            self.arr.insert(self.i, self.minval)
            [rect.set_height(h) for rect, h in zip(self.rects, self.arr)]
            self.i+=1
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()


selection = selection_sort()
selection.plot(random.sample(range(1, 251), 250))
selection.bar(random.sample(range(1, 251), 250))

'''
    for i in arr:
        if i in [i for i in range(250)][::5]:
            rects[arr.index(i)].set_color('#5fa55a')
        elif i in [i for i in range(250)][1::5]:
            rects[arr.index(i)].set_color('#01b4bc')
        elif i in [i for i in range(250)][2::5]:
            rects[arr.index(i)].set_color('#f6d51f')
        elif i in [i for i in range(250)][3::5]:
            rects[arr.index(i)].set_color('#fa8925')
        elif i in [i for i in range(250)][4::5]:
            rects[arr.index(i)].set_color('#fa5457')
'''

#import lib
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import matplotlib
            
#insertion sort
class insertion_sort:

    #initialize
    def __init__(self):
        self.titlefont = {'fontsize':30, 'fontfamily':'Bahnschrift'}
        self.subtitlefont = {'fontsize':20, 'fontfamily':'Bahnschrift'}

    #plot style
    def plot(self, arr):
        plt.ion()
        self.arr = arr
        self.fig = plt.figure()
        self.line, = plt.plot(self.arr)
        for i in range(1, len(self.arr)):
            for j in range(0, i):
                if self.arr[j]<self.arr[i]:
                    pass
                else:
                    self.temp = self.arr[i]
                    self.arr.remove(self.temp)
                    self.arr.insert(j, self.temp)
            self.line.set_ydata(self.arr)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    #bar style 
    def bar(self, arr):
        plt.ion()
        self.arr = arr
        self.fig = plt.figure()
        self.rects = plt.bar([i for i in range(len(arr))], self.arr, width=1.0)
        for i in range(1, len(self.arr)):
            for j in range(0, i):
                if self.arr[j]<self.arr[i]:
                    pass
                else:
                    self.temp = self.arr[i]
                    self.arr.remove(self.temp)
                    self.arr.insert(j, self.temp)
            [rect.set_height(h) for rect, h in zip(self.rects, self.arr)]
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()


insertion = insertion_sort()
insertion.plot(random.sample(range(1, 101), 100))
insertion.bar(random.sample(range(1, 101), 100))


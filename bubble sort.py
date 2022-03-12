#import lib
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import matplotlib
            
#bubble sort
class bubble_sort:

    #initialize
    def __init__(self):
        self.titlefont = {'fontsize':30, 'fontfamily':'Bahnschrift'}
        self.subtitlefont = {'fontsize':20, 'fontfamily':'Bahnschrift'}

    #plot style
    def plot(self, arr):
        plt.ion()
        self.arr = arr
        self.run = True
        self.fig = plt.figure()
        self.line, = plt.plot(self.arr)
        while self.run:
            self.i=0
            self.run = False
            for i in range(len(self.arr)-1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    self.run=True
            self.line.set_ydata(self.arr)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    #bar style 
    def bar(self, arr):
        plt.ion()
        self.arr = arr
        self.run = True
        self.fig = plt.figure()
        self.rects = plt.bar([i for i in range(len(arr))], self.arr, width=1.0)
        while self.run:
            self.i=0
            self.run = False
            for i in range(len(self.arr)-1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    self.run=True
            [rect.set_height(h) for rect, h in zip(self.rects, self.arr)]
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()


bubble = bubble_sort()
bubble.plot(random.sample(range(1, 1001), 1000))
bubble.bar(random.sample(range(1, 1001), 1000))

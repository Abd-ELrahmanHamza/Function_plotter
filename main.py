# import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
fontFamily = "Times"
oldCanvas = -1

def title(root):
    '''
    :param root: The root object
    :return: Void
    :about: A function that creates the title section
    '''
    # Create the Title frame
    titleFrame = tk.Frame(root)
    titleFrame.pack(side=tk.TOP, pady=30)

    # Create the Label for title
    title = tk.Label(titleFrame, text="Function Plotter", font=(fontFamily, 25, "bold"), fg="green")
    title.pack(fill=tk.X)


def about(root):
    '''
    :param root: The root object
    :return: Void
    :about: A function that creates the about section
    '''

    # Create the About frame
    aboutFrame = tk.Frame(root)
    aboutFrame.pack(side=tk.BOTTOM, pady=20)

    # About title label
    titleAbout = tk.Label(aboutFrame, text="About the input data", font=(fontFamily, 20, "bold"), fg="green")
    titleAbout.pack(fill=tk.X, pady=10)

    # About text label
    txt1 = "* The function should contain: numbers or X (variable) or + or - or / or * or ^\n\n"
    txt2 = "* Min and Max values of X must be numbers."
    infoAbout = tk.Label(aboutFrame, text=txt1 + txt2, font=(fontFamily, 15), fg="maroon")
    infoAbout.pack(side=tk.LEFT)


def hozizontalSeparator(root):
    '''
    :param root: The root object
    :return: Void
    :about: Creates horizontal separator
    '''
    ttk.Separator(root, orient='horizontal').pack(fill=tk.X)


def verticalSeparator(root):
    '''
    :param root: The root object
    :return: Void
    :about: Creates vertical separator
    '''
    ttk.Separator(root, orient='vertical').pack(side=tk.LEFT, fill=tk.Y)


def stringToFunction(str):
    allowedChars = ['X', 'x', '*', '/', '-', '+', '^']
    replacements = {
        '^': '**',
        'x': 'sp.symbols(\'x\')',
        'X': 'sp.symbols(\'x\')'
    }
    for char in str:
        if ((not char.isnumeric()) and (char not in allowedChars)):
            messagebox.showwarning("showwarning",
                                   "Function is Should contain only \'X\' or \'x\' or \'+\' or \'-\' or \'*\' or \'/\' or \'^\'")
            return
    for old, new in replacements.items():
        str = str.replace(old, new)
    return eval(str)


def plot(function, maxXval, minXval, frame):
    # Handle empty string
    if (len(function) == 0):
        messagebox.showwarning("showwarning", "Function is missing")
        return -1

    # Handle invalid min and max values (float)
    try:
        maxXval = float(maxXval)
    except:
        messagebox.showwarning("showwarning", "Max X is missing")
        return -1
    try:
        minXval = float(minXval)
    except:
        messagebox.showwarning("showwarning", "Min X is missing")
        return -1

    # Handle invalid min and max values (Range)
    if minXval>= maxXval:
        messagebox.showwarning("showwarning", "Min X Must be less than Max X")
        return

    print(function, maxXval, minXval)
    # print(stringToFunction(function))
    # hp = sp.plot(stringToFunction(function), minX=minXval, maxX=maxXval)

    # Convert string function to function
    equation = stringToFunction(function)

    # Substitute by min x and max x to get the corresponding y
    maxYval = equation.subs(sp.symbols('x'),maxXval)
    minYval = equation.subs(sp.symbols('x'),minXval)

    # If corresponding y values are equal set min Y value to -10
    if(maxYval==minYval):
        minYval = -10
    hp = sp.plot_implicit(sp.Eq(equation, sp.symbols('y')), (sp.symbols('x'), minXval, maxXval),(sp.symbols('y'), minYval, maxYval))
    # hp = sp.plot_implicit(sp.Eq(equation, sp.symbols('y')), (sp.symbols('x'), minXval, maxXval))

    # Place the figure in the window
    fig = hp._backend.fig
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side = tk.BOTTOM)
    canvas.draw()

    return canvas


def inputData(frame, plotFrame):

    # Common data between all entries
    frampady = 25
    padding = 20
    entryW = 30
    lblW = 12
    lblFontSize = 16

    # Create title for the input data section
    titleFrame = tk.Frame(frame)
    titleFrame.pack(pady=10)

    # Create title title for the input data section
    titleGraph = tk.Label(titleFrame, text="Input data", font=(fontFamily, 20, "bold"), fg="green")
    titleGraph.pack(fill=tk.X, pady=10)

    # divide it into four frames for function, min, max & submit

    # 1- function
    # Function frame
    lblFrame = tk.Frame(frame)
    lblFrame.pack(pady=frampady)
    # Function label
    funlbl = tk.Label(lblFrame, text="Function : ", font=(fontFamily, lblFontSize), fg="black", anchor='w', width=lblW)
    funlbl.pack(side=tk.LEFT, padx=padding)
    # Function entry
    funEnry = tk.Entry(lblFrame, width=entryW, font=(fontFamily, lblFontSize))
    funEnry.pack(side=tk.RIGHT, padx=padding)

    # 2- Max
    # Max frame
    maxFrame = tk.Frame(frame)
    maxFrame.pack(pady=frampady)
    # Max label
    maxXlbl = tk.Label(maxFrame, text="Max value of X : ", font=(fontFamily, lblFontSize), fg="black", anchor='w',
                       width=lblW)
    maxXlbl.pack(side=tk.LEFT, padx=padding)
    # Max entry
    maxXEnry = tk.Entry(maxFrame, width=entryW, font=(fontFamily, lblFontSize))
    maxXEnry.pack(side=tk.RIGHT, padx=padding)

    # 3- Min
    # Min frame
    minFrame = tk.Frame(frame)
    minFrame.pack(pady=frampady)
    # Min label
    minXlbl = tk.Label(minFrame, text="Min value of X : ", font=(fontFamily, lblFontSize), fg="black", anchor='w',
                       width=lblW)
    minXlbl.pack(side=tk.LEFT, padx=padding)
    # Min entry
    minXEnry = tk.Entry(minFrame, width=entryW, font=(fontFamily, lblFontSize))
    minXEnry.pack(side=tk.RIGHT, padx=padding)

    def helloCallBack():
        global oldCanvas
        if(oldCanvas != -1):
            oldCanvas.get_tk_widget().destroy()
        oldCanvas = plot(funEnry.get(), maxXEnry.get(), minXEnry.get(), plotFrame)

    # 4- Submit
    # Submit frame
    submitFrame = tk.Frame(frame)
    submitFrame.pack(pady=frampady)
    # Submit button
    btn = tk.Button(submitFrame, text="Plot", command=helloCallBack, width=10, height=20,
                    font=(fontFamily, lblFontSize + 2), background="green", fg="white")
    btn.pack()


def plotGraph(frame):
    # Create the title for the graph section
    titleFrame = tk.Frame(frame)
    titleFrame.pack(pady=20)

    # Create the title label for the graph section
    titleGraph = tk.Label(titleFrame, text="Graph", font=(fontFamily, 20, "bold"), fg="green")
    titleGraph.pack(fill=tk.X, pady=10)


def body(root):
    '''
    :param root: The root object
    :return: void
    :about: Create body section
    '''

    # Create  body frame
    bodyFrame = tk.Frame(root)
    bodyFrame.pack()

    # separate the body frames into two frames => inputData & graph

    # create inputData frame
    inputDataFrame = tk.Frame(bodyFrame, width=400, height=400)
    inputDataFrame.pack(side=tk.LEFT, fill=tk.X)
    inputDataFrame.pack_propagate(0)

    # create vertical separator
    verticalSeparator(bodyFrame)

    # create graph frame
    graphFrame = tk.Frame(bodyFrame, width=400, height=400)
    graphFrame.pack(side=tk.RIGHT)
    graphFrame.pack_propagate(0)

    # Fill input data section
    inputData(inputDataFrame, graphFrame)

    # Fill graph section
    plotGraph(graphFrame)


if __name__ == '__main__':
    root = tk.Tk(className="Function Plotter")
    root.geometry("800x700")
    title(root)
    hozizontalSeparator(root)

    body(root)

    hozizontalSeparator(root)
    about(root)
    root.mainloop()

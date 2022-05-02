# import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import sympy as sp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

fontFamily = "Times"
oldCanvas = -1

# TODO: Title of the window
def title(root):
    titleFrame = tk.Frame(root)
    titleFrame.pack(side=tk.TOP, pady=30)

    title = tk.Label(titleFrame, text="Function Plotter", font=(fontFamily, 25, "bold"), fg="green")
    title.pack(fill=tk.X)


# TODO: About section contains the information of valid input data
def about(root):
    # frame of about section

    aboutFrame = tk.Frame(root)
    aboutFrame.pack(side=tk.BOTTOM, pady=20)

    titleAbout = tk.Label(aboutFrame, text="About the input data", font=(fontFamily, 20, "bold"), fg="green")
    titleAbout.pack(fill=tk.X, pady=10)
    txt1 = "* The function should contain: numbers, X (variable), + - / * ^.\n\n"
    txt2 = "* Min and Max values of X must be numbers."
    infoAbout = tk.Label(aboutFrame, text=txt1 + txt2, font=(fontFamily, 15), fg="black")
    infoAbout.pack(side=tk.LEFT)


def hozizontalSeparator(root):
    ttk.Separator(root, orient='horizontal').pack(fill=tk.X)


def verticalSeparator(root):
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
    if (len(function) == 0):
        messagebox.showwarning("showwarning", "Function is missing")
        return

    try:
        maxXval = int(maxXval)
    except:
        messagebox.showwarning("showwarning", "Max X is missing")
        return
    try:
        minXval = int(minXval)
    except:
        messagebox.showwarning("showwarning", "Min X is missing")
        return
    print(function, maxXval, minXval)
    # print(stringToFunction(function))
    # hp = sp.plot(stringToFunction(function), minX=minXval, maxX=maxXval)
    hp = sp.plot_implicit(sp.Eq(stringToFunction(function), sp.symbols('y')), (sp.symbols('x'), minXval, maxXval))
    fig = hp._backend.fig
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side = tk.BOTTOM)
    canvas.draw()
    return canvas


def inputData(frame, plotFrame):
    frampady = 25
    padding = 20
    entryW = 30
    lblW = 12
    lblFontSize = 16
    titleFrame = tk.Frame(frame)
    titleFrame.pack(pady=10)

    titleGraph = tk.Label(titleFrame, text="Input data", font=(fontFamily, 20, "bold"), fg="green")
    titleGraph.pack(fill=tk.X, pady=10)

    lblFrame = tk.Frame(frame)
    lblFrame.pack(pady=frampady)
    funlbl = tk.Label(lblFrame, text="Function : ", font=(fontFamily, lblFontSize), fg="black", anchor='w', width=lblW)
    funlbl.pack(side=tk.LEFT, padx=padding)
    funEnry = tk.Entry(lblFrame, width=entryW, font=(fontFamily, lblFontSize))
    funEnry.pack(side=tk.RIGHT, padx=padding)

    maxFrame = tk.Frame(frame)
    maxFrame.pack(pady=frampady)
    maxXlbl = tk.Label(maxFrame, text="Max value of X : ", font=(fontFamily, lblFontSize), fg="black", anchor='w',
                       width=lblW)
    maxXlbl.pack(side=tk.LEFT, padx=padding)
    maxXEnry = tk.Entry(maxFrame, width=entryW, font=(fontFamily, lblFontSize))
    maxXEnry.pack(side=tk.RIGHT, padx=padding)

    minFrame = tk.Frame(frame)
    minFrame.pack(pady=frampady)
    minXlbl = tk.Label(minFrame, text="Min value of X : ", font=(fontFamily, lblFontSize), fg="black", anchor='w',
                       width=lblW)
    minXlbl.pack(side=tk.LEFT, padx=padding)
    minXEnry = tk.Entry(minFrame, width=entryW, font=(fontFamily, lblFontSize))
    minXEnry.pack(side=tk.RIGHT, padx=padding)

    def helloCallBack():
        global oldCanvas
        if(oldCanvas != -1):
            oldCanvas.get_tk_widget().destroy()
        oldCanvas = plot(funEnry.get(), maxXEnry.get(), minXEnry.get(), plotFrame)

    submitFrame = tk.Frame(frame)
    submitFrame.pack(pady=frampady)
    btn = tk.Button(submitFrame, text="Plot", command=helloCallBack, width=10, height=20,
                    font=(fontFamily, lblFontSize + 2), background="green", fg="white")
    btn.pack()


def plotGraph(frame):
    titleFrame = tk.Frame(frame)
    titleFrame.pack(pady=20)

    titleGraph = tk.Label(titleFrame, text="Graph", font=(fontFamily, 20, "bold"), fg="green")
    titleGraph.pack(fill=tk.X, pady=10)


def body(root):
    bodyFrame = tk.Frame(root)
    bodyFrame.pack()
    # separate the body frames into two frames
    inputDataFrame = tk.Frame(bodyFrame, width=400, height=400)
    inputDataFrame.pack(side=tk.LEFT, fill=tk.X)
    inputDataFrame.pack_propagate(0)
    verticalSeparator(bodyFrame)
    graphFrame = tk.Frame(bodyFrame, width=400, height=400)
    graphFrame.pack(side=tk.RIGHT)
    graphFrame.pack_propagate(0)

    inputData(inputDataFrame, graphFrame)
    plotGraph(graphFrame)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x, y = sp.symbols("x y")
    # hp = sp.plot_implicit(sp.Eq(x ** 2 + y ** 2, 4), (x, -3, 3), (y, -3, 3))
    # fig = hp._backend.fig
    root = tk.Tk(className="Function Plotter")
    root.geometry("800x700")
    title(root)
    hozizontalSeparator(root)

    body(root)

    hozizontalSeparator(root)
    about(root)
    # canvas = FigureCanvasTkAgg(fig, master=root)
    # canvas.get_tk_widget().pack()
    # canvas.draw()
    root.mainloop()

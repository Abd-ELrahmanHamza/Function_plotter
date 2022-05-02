# import tkinter
import tkinter as tk
from tkinter import ttk

fontFamily = "Times"


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


def inputData(frame):
    frampady = 25
    padding = 20
    entryW = 30
    entryH = 20
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

    submitFrame = tk.Frame(frame)
    submitFrame.pack(pady=frampady)
    btn = tk.Button(submitFrame, text="Plot", command=helloCallBack,width = 10,height = 20,font=(fontFamily, lblFontSize+2),background = "green",fg="white")
    btn.pack()

def helloCallBack():
    print("Hello world")
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

    inputData(inputDataFrame)
    plotGraph(graphFrame)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk(className="Function Plotter")
    root.geometry("800x700")
    title(root)
    hozizontalSeparator(root)

    body(root)

    hozizontalSeparator(root)
    about(root)
    root.mainloop()

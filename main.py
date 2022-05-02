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
    ttk.Separator(root, orient='horizontal').pack(fill='x')


def body(root):
    bodyFrame = tk.Frame(root, background="red")
    bodyFrame.pack()


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

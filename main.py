# import tkinter
import tkinter as tk


def title(root):
    titleFrame = tk.Frame(root)
    titleFrame.pack(side = tk.TOP)

    title = tk.Label(titleFrame,text="Function Plotter",font=("Helvetica", 25,"bold italic"),fg="green")
    title.pack(fill = tk.X)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    root = tk.Tk(className="Function Plotter")
    root.geometry("800x700")
    title(root)
    root.mainloop()



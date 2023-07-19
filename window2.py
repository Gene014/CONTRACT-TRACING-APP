import tkinter as tk
import tkinter.font as tkFont
from tkinter import StringVar

# Input the generated front from the design application you created thru paper

class App:
    def __init__(self, root):
        # setting title
        root.title("Contact Tracing App")
        width = 842
        height = 700
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # Title Block
        TitleBlock = tk.Label(root)
        ft = tkFont.Font(family='Times', size=22)
        TitleBlock["font"] = ft
        TitleBlock["fg"] = "#333333"
        TitleBlock["justify"] = "center"
        TitleBlock["text"] = "Contact Tracing Form"
        TitleBlock.place(x=280, y=10, width=265, height=30)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
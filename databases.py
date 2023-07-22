import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import window2

class datas():
    def __init__(self, root2):
        # setting title
        root2.title("Database")
        width = 842
        height = 750
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)
        # Title Block
        TitleBlock = tk.Label(root2)
        ft = tkFont.Font(family='Times', size=22)
        TitleBlock["font"] = ft
        TitleBlock["fg"] = "#333333"
        TitleBlock["justify"] = "center"
        TitleBlock["text"] = "Database"
        TitleBlock.place(x=350, y=10)


        def iExit():
            root2.destroy()
            root = Tk()
            app = window2.App(root)
            root.focus_force()
            root.mainloop()

        exit_button = tk.Button(root2, command=lambda: iExit())
        ft = tkFont .Font(family='Times', size=10)
        exit_button["font"] = ft
        exit_button["fg"] = "#000000"
        exit_button["justify"] = "center"
        exit_button["text"] = "Home"
        exit_button.place(x=30, y=20, width=70, height=25)

        Searchbar = tk.Label(root2)
        ft = tkFont.Font(family='Times', size=12)
        Searchbar["font"] = ft
        Searchbar["fg"] = "#333333"
        Searchbar["justify"] = "center"
        Searchbar["text"] = "Search:"
        Searchbar.place(x=212, y=62)

        self.search_var = tk.StringVar(value="")

        search_entry = tk.Entry(root2)
        search_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        search_entry["font"] = ft
        search_entry["fg"] = "#101010"
        search_entry["justify"] = "left"
        search_entry["text"] = "Search"
        search_entry["textvariable"] = self.search_var
        search_entry.place(x=270, y=60, width=279, height=30)



if __name__ == "__main__":
    root2 = tk.Tk()
    app1 = datas(root2)
    root2.mainloop()

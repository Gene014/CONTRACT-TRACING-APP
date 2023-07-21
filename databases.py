import tkinter as tk
import tkinter.font as tkFont


class datas:
    def __init__(self, root):
        
        # setting title
        root.title("Database")
        width = 842
        height = 750
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
        TitleBlock["text"] = "List of Informations"
        TitleBlock.place(x=280, y=10)

if __name__ == "__main__":
    root = tk.Tk()
    app1 = datas(root)
    root.mainloop()
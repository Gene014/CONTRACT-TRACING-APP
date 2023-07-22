import tkinter as tk
from tkinter import *
from tkinter import ttk
from datastorage import DataStorage
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

        NameSearch = tk.Label(root2)
        ft = tkFont.Font(family='Times', size=12)
        NameSearch["font"] = ft
        NameSearch["fg"] = "#333333"
        NameSearch["justify"] = "center"
        NameSearch["text"] = "Search:"
        NameSearch.place(x=212, y=62)

        self.search_var = tk.StringVar(value="")

        searchbar = tk.Entry(root2)
        searchbar["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        searchbar["font"] = ft
        searchbar["fg"] = "#101010"
        searchbar["justify"] = "left"
        searchbar["text"] = "Search"
        searchbar["textvariable"] = self.search_var
        searchbar.place(x=270, y=60, width=279, height=30)

        treeview_frame = Frame(root2)
        treeview_frame.place(x=0, y=100, width=842, height=645)

        treeview = ttk.Treeview(treeview_frame)
        treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_y = Scrollbar(
            treeview, orient=tk.VERTICAL, command=treeview.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        treeview.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = Scrollbar(
            treeview, orient=tk.HORIZONTAL, command=treeview.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        treeview.configure(xscrollcommand=scrollbar_x.set)

        def setup_treeview():
            treeview["columns"] = (
                "Respondent Name",
                "Student Number",
                "First Question",
                "Second Question",
                "Third Question",
                "Fourth Question",
                "Fifth Question",
                "Email Address",
                "Contact Number",
                "Contact Person Name",
                "Contact Person Number",
                "Contact Person Email Add",
                "Relationship",
                "Submit Time"
            )

            treeview.heading("#0", text="ID")
            treeview.column("#0", width=50, stretch=0)

            for column in treeview["columns"]:
                treeview.heading(column, text=column)
                treeview.column(column, width=200, stretch=0)

        setup_treeview()

        # Transposing Datas from CSV to Database Tab
        def load_data():
            data = DataStorage.load_data('database.csv')

            for index, record in enumerate(data, start=1):
                treeview.insert("", "end", text=str(index), values=record)
        
        load_data ()
        
        def search_data(*args):

            search_text = self.search_var.get().lower()
            # Clear previous search results
            treeview.delete(*treeview.get_children())

            # Transposing Datas from CSV to Database Tab
            data = DataStorage.load_data('database.csv')

            # Search and insert matching data into the Treeview
            for index, record in enumerate(data, start=1):
                if search_text in str(record).lower():
                    treeview.insert(
                        "", "end", text=str(index), values=record)

        self.search_var.trace("w", search_data)

if __name__ == "__main__":
    root2 = tk.Tk()
    app1 = datas(root2)
    root2.mainloop()

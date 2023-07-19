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

        # NAME TEXT FIELD
        def on_entry_focus_in1(event):
            if user_name.get() == placeholder_text1:
                user_name.delete(0, tk.END)
                user_name.configure(show="")
                user_name.configure(fg="#333333")

        def on_entry_focus_out1(event):
            if user_name.get() == "":
                user_name.insert(0, placeholder_text1)
                user_name.configure(fg="gray")

        user_name = tk.Entry(root)
        user_name["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        user_name["font"] = ft
        user_name["fg"] = "gray"
        user_name["justify"] = "left"
        user_name["text"] = "Name"
        user_name.place(x=30, y=60, width=220, height=30)

        placeholder_text1 = "Enter Full name"
        user_name.insert(0, placeholder_text1)
        user_name.bind("<FocusIn>", on_entry_focus_in1)
        user_name.bind("<FocusOut>", on_entry_focus_out1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
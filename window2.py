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

        # STUDENT NUMBER TEXT FIELD

        def on_entry_focus_in2(event):
            if stdnum.get() == placeholder_text2:
                stdnum.delete(0, tk.END)
                stdnum.configure(show="")
                stdnum.configure(fg="#333333")

        def on_entry_focus_out2(event):
            if stdnum.get() == "":
                stdnum.insert(0, placeholder_text2)
                stdnum.configure(fg="gray")

        stdnum = tk.Entry(root)
        stdnum["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        stdnum["font"] = ft
        stdnum["fg"] = "gray"
        stdnum["justify"] = "left"
        stdnum["text"] = "Student Number"
        stdnum.place(x=30, y=100, width=219, height=30)

        placeholder_text2 = "Enter Student number"
        stdnum.insert(0, placeholder_text2)
        stdnum.bind("<FocusIn>", on_entry_focus_in2)
        stdnum.bind("<FocusOut>", on_entry_focus_out2)

        # QUESTION 1
        quest1 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest1["font"] = ft
        quest1["fg"] = "#333333"
        quest1["justify"] = "left"
        quest1["text"] = "1. Have you been vaccinated for COVID-19? *"
        quest1.place(x=20, y=140, width=265, height=30)
        quest1["justify"] = "left"

        self.question1 = StringVar(value="x")

        op1q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q1["font"] = ft
        op1q1["fg"] = "#333333"
        op1q1["justify"] = "left"
        op1q1["text"] = "Not Yet"
        op1q1["variable"] = self.question1
        op1q1["value"] = "Not Yet"
        op1q1.place(x=60, y=180, height=25)

        op2q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q1["font"] = ft
        op2q1["fg"] = "#333333"
        op2q1["justify"] = "left"
        op2q1["text"] = "1st Dose"
        op2q1["variable"] = self.question1
        op2q1["value"] = "1st Dose"
        op2q1.place(x=60, y=200, height=25)

        op3q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q1["font"] = ft
        op3q1["fg"] = "#333333"
        op3q1["justify"] = "left"
        op3q1["text"] = "2nd Dose (Fully Vaccinated)"
        op3q1["variable"] = self.question1
        op3q1["value"] = "2nd Dose (Fully Vaccinated)"
        op3q1.place(x=60, y=220, height=25)

        op4q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op4q1["font"] = ft
        op4q1["fg"] = "#333333"
        op4q1["justify"] = "left"
        op4q1["text"] = "1st Booster Shot"
        op4q1["variable"] = self.question1
        op4q1["value"] = "1st Booster Shot"
        op4q1.place(x=60, y=240, height=25)

        op5q1 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op5q1["font"] = ft
        op5q1["fg"] = "#333333"
        op5q1["justify"] = "left"
        op5q1["text"] = "2nd Booster Shot"
        op5q1["variable"] = self.question1
        op5q1["value"] = "2nd Booster Shot"
        op5q1.place(x=60, y=260, height=25)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
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

        # QUESTION 2
        quest2 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest2["font"] = ft
        quest2["fg"] = "#333333"
        quest2["justify"] = "left"
        quest2["text"] = "2. Are you experiencing any symptoms in the past 7 days such as:*"
        quest2.place(x=30, y=290, width=361, height=59)

        self.question2 = StringVar(value="0")

        op1q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q2["font"] = ft
        op1q2["fg"] = "#333333"
        op1q2["justify"] = "left"
        op1q2["text"] = "Fever"
        op1q2.place(x=60, y=340)
        op1q2["variable"] = self.question2
        op1q2["value"] = "Fever"

        op2q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q2["font"] = ft
        op2q2["fg"] = "#333333"
        op2q2["justify"] = "left"
        op2q2["text"] = "Cough"
        op2q2.place(x=60, y=360)
        op2q2["variable"] = self.question2
        op2q2["value"] = "Cough"

        op3q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q2["font"] = ft
        op3q2["fg"] = "#333333"
        op3q2["justify"] = "left"
        op3q2["text"] = "Colds"
        op3q2.place(x=60, y=380)
        op3q2["variable"] = self.question2
        op3q2["value"] = "Colds"

        op4q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op4q2["font"] = ft
        op4q2["fg"] = "#333333"
        op4q2["justify"] = "left"
        op4q2["text"] = "Muscle/body pains"
        op4q2.place(x=60, y=400)
        op4q2["variable"] = self.question2
        op4q2["value"] = "Muscle/body pains"

        op5q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op5q2["font"] = ft
        op5q2["fg"] = "#333333"
        op5q2["justify"] = "left"
        op5q2["text"] = "Sore throat"
        op5q2.place(x=60, y=420)
        op5q2["variable"] = self.question2
        op5q2["value"] = "Sore throat"

        op6q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op6q2["font"] = ft
        op6q2["fg"] = "#333333"
        op6q2["justify"] = "left"
        op6q2["text"] = "Diarrhea"
        op6q2.place(x=60, y=440)
        op6q2["variable"] = self.question2
        op6q2["value"] = "Diarrhea"

        op7q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op7q2["font"] = ft
        op7q2["fg"] = "#333333"
        op7q2["justify"] = "left"
        op7q2["text"] = "Headache"
        op7q2.place(x=200, y=340)
        op7q2["variable"] = self.question2
        op7q2["value"] = "Headache"

        op8q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op8q2["font"] = ft
        op8q2["fg"] = "#333333"
        op8q2["justify"] = "left"
        op8q2["text"] = "Shortness of breath"
        op8q2.place(x=200, y=360)
        op8q2["variable"] = self.question2
        op8q2["value"] = "Shortness of breath"

        op9q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op9q2["font"] = ft
        op9q2["fg"] = "#333333"
        op9q2["justify"] = "left"
        op9q2["text"] = "Difficulty of breathing"
        op9q2.place(x=200, y=380)
        op9q2["variable"] = self.question2
        op9q2["value"] = "Difficulty of breathing"

        op10q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op10q2["font"] = ft
        op10q2["fg"] = "#333333"
        op10q2["justify"] = "left"
        op10q2["text"] = "Loss of taste"
        op10q2.place(x=200, y=400)
        op10q2["variable"] = self.question2
        op10q2["value"] = "Loss of taste"

        op11q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op11q2["font"] = ft
        op11q2["fg"] = "#333333"
        op11q2["justify"] = "left"
        op11q2["text"] = "Loss of smell"
        op11q2.place(x=200, y=420)
        op11q2["variable"] = self.question2
        op11q2["value"] = "Loss of smell"

        op12q2 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op12q2["font"] = ft
        op12q2["fg"] = "#333333"
        op12q2["justify"] = "left"
        op12q2["text"] = "None of the above"
        op12q2.place(x=200, y=440)
        op12q2["variable"] = self.question2
        op12q2["value"] = "None of the above"
        
        # QUESTION 3
        quest3 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        quest3["font"] = ft
        quest3["fg"] = "#333333"
        quest3["justify"] = "left"
        quest3["text"] = "3. Have you had exposure to a probable or confirmed case in the last 14 days?*"
        quest3["wraplength"] = 350
        quest3.place(x=30, y=490)

        self.question3 = StringVar(value="0")

        op1q3 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op1q3["font"] = ft
        op1q3["fg"] = "#333333"
        op1q3["justify"] = "left"
        op1q3["text"] = "Yes"
        op1q3["value"] = "Yes"
        op1q3["variable"] = self.question3
        op1q3.place(x=60, y=530)

        op2q3 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op2q3["font"] = ft
        op2q3["fg"] = "#333333"
        op2q3["justify"] = "left"
        op2q3["text"] = "No"
        op2q3["value"] = "No"
        op2q3["variable"] = self.question3
        op2q3.place(x=60, y=550)

        op3q3 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        op3q3["font"] = ft
        op3q3["fg"] = "#333333"
        op3q3["justify"] = "left"
        op3q3["text"] = "Uncertain"
        op3q3["value"] = "Uncertain"
        op3q3["variable"] = self.question3
        op3q3.place(x=60, y=570)
       
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
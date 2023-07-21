# Input the generated front from the design application you created thru paper
# Generate the first and second window

from tkinter import *
import window2

def btn_clickedYes():
    window.destroy()
    root = Tk()
    app = window2.App(root)
    root.mainloop()

def btn_clickedNo():
    window.destroy()

window = Tk()

width = 800
height = 500
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
window.geometry(alignstr)
window.resizable(width=False, height=False)
window.configure(bg="#ffffff")
window.title('Data Act')
canvas = Canvas(
    window,
    bg="#ffffff",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    400.0, 250.0,
    image=background_img)

canvas.create_text(
    415.0, 60,
    text="Contact Tracing Form",
    fill="#fff",
    font=('"Inter" 32 bold'))

canvas.create_text(
    414.5, 225,
    text="In compliance with the Data Privacy Act of 2012 and its Implementing Rules and Regulations, we execute reasonable and appropriate security measures for the protection of personal data\nthat we collect. \n\nPress Yes if you want to continue, otherwise, press No if you want to terminate the application.",
    fill="#fff",
    width=480,
    justify="center",
    font=('"Inter" 16 bold'))


img1 = PhotoImage(file=f"img1.png")
b0 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clickedYes,
    relief="flat")
b0.place(x=240, y=360)

img0 = PhotoImage(file=f"img0.png")
b1 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clickedNo,    
    relief="flat")
b1.place(x=439, y=360,)

window.resizable(False, False)
window.mainloop()
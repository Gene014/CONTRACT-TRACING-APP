# Input the generated front from the design application you created thru paper
# Generate the first and second window

from tkinter import *
import window2

def btn_clickedNo():
    window.destroy()
    root = Tk()
    app = window2.App(root)
    root.mainloop()


def btn_clickedYes():
    window.destroy()

window = Tk()

window.geometry("800x500")
window.configure(bg="#ffffff")
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
    414.5, 241.5,
    text="In compliance with the Data Privacy Act of 2012\nand its Implementing Rules and Regulations, we\nexecute reasonable and appropriate securit\nmeasures for the protection of personal data\nthat we collect. \n\nPress Yes if you want to continue, otherwise,\npress No if you want to terminate the application.",
    fill="#fff",
    justify="center",
    font=('"Arial Narrow" 16 bold'))

canvas.create_text(
    415.0, 105.5,
    text="Contact Tracing Form",
    fill="#fff",
    font=("Inter-Bold", int(24.0)))

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clickedYes,
    relief="flat")
b0.place(
    x=439, y=345,
    width=131,
    height=65)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clickedNo,    
    relief="flat")
b1.place(
    x=240, y=345,
    width=131,
    height=65)

window.resizable(False, False)
window.mainloop()
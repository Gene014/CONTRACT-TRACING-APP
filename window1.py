# Input the generated front from the design application you created thru paper
# Generate the first and second window

from tkinter import *
import window2

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

window.resizable(False, False)
window.mainloop()
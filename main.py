import tkinter as tka

rooty = tka.Tk()
rooty.geometry("1000x600")
rooty.configure(bg="red")
rooty.title("ЕДВ")
rooty.overrideredirect(False)

x_sq1 = 199
y_sq1 = 60
x_cv1 = 400
y_cv1 = 200

sq1 = tka.Frame(rooty, width=100, height=100, bg="black")
sq1.place(x=x_sq1, y=y_sq1)

canvas = tka.Canvas(rooty, width=200, height=150, bg="red", highlightthickness=0)
canvas.pack()
#canvas.place(x=x_cv1, y=y_cv1)
crl = canvas.create_oval(50,50,150,150, fill="yellow")

def on_keyX(event):
    global x_sq1
    if event.keysym.lower() == "x":
        x += 1
        sq1.place(x=x_sq1, y=y_sq1)

def on_keyY(event):
    global y_sq1
    if event.keysym.lower() == "y":
        y_sq1 += 1
        sq1.place(x=x_sq1, y=y_sq1)

rooty.bind("<Key>", on_keyX)
rooty.bind("<Key>", on_keyY, add="+")
rooty.mainloop()
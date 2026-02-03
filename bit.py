
import tkinter as tk
from PIL import Image, ImageTk
STEP=10
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

img = Image.open("bit.png").convert("RGBA")

data = img.getdata()
new_data = []

for pixel in data:
    # se for preto puro, fica transparente
    if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(pixel)

img.putdata(new_data)

pic = ImageTk.PhotoImage(img)

rect = canvas.create_image(50, 50, image=pic)

def move(event):
    if event.keysym == "Up":
        canvas.move(rect, 0, -STEP)
    elif event.keysym == "Down":
        canvas.move(rect, 0, STEP)
    elif event.keysym == "Left":
        canvas.move(rect, -STEP, 0)
    elif event.keysym == "Right":
        canvas.move(rect, STEP, 0)

# Capturar teclas
root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

root.mainloop()

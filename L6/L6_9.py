# 第8章.pptx, P79 - 85, program that uses a Canvas control to create text

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas(winForm, bg = "white", width = 300, height = 100)
text = canvas.create_text((10, 10), text = "Hello Python!", fill = "red", anchor = "nw")
canvas.select_from(text, 0)
canvas.select_to(text, 4)
canvas.create_text((300, 50), text = "Arvin Zhao", fill = "blue", anchor = "se")
canvas.pack()

winForm.mainloop()
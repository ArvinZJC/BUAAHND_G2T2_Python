#2018.05.20, 第8章.pptx, P100 & 101, program using a Canvas control and scale()

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 150, height = 300 )
rectangle = canvas.create_rectangle( 10, 10, 110, 110, outline = "red", stipple = "gray12", fill = "green" )
canvas.scale( rectangle, 0, 0, 1, 2 )
canvas.pack()

winForm.mainloop()
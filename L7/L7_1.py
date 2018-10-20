#2018.05.26, 第8章.pptx, P104 & 105, program using a Canvas control and find_withtag()

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 200, height = 200 )
canvas.create_rectangle( 10, 10, 110, 110, tags = "r3" )
canvas.pack()
 
for item in canvas.find_withtag( "r3" ):
    canvas.itemconfig( item, outline = "blue" )

winForm.mainloop()
#2018.05.20, 第8章.pptx, P79-85, program using a Canvas control to create text

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 300, height = 100 )
TXT = canvas.create_text( ( 10, 10 ), text = "Hello Python!", fill = "red", anchor = "nw" )  #TXT is the abbreviation of text
canvas.select_from( TXT, 0 )
canvas.select_to( TXT, 4 )
canvas.create_text( ( 300, 50 ), text = "Arvin Zhao", fill = "blue", anchor = "se" )
canvas.pack()

winForm.mainloop()
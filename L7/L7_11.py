# 第8章.pptx, P163 & 164, program that uses a Text control

from tkinter import Tk, Text

winForm = Tk()

text = Text(winForm)
text.insert(1.6, "inserted")
text.insert(1.2, "0123456789")
text.pack()

winForm.mainloop()
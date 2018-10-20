#2018.05.26, 第8章.pptx, P128 & 129, program using a simple Listbox control

from tkinter import Tk, Listbox

winForm = Tk()

listbox = Listbox( winForm )

for item in [ "A", "B", "C" ]:
    listbox.insert( "end", item )

listbox.pack()

winForm.mainloop()
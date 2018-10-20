#2018.05.26, 第8章.pptx, P131, program using a Listbox control with multiple selections enabled

from tkinter import Tk, Listbox

winForm = Tk()

listbox = Listbox( winForm, selectmode = "multiple" )

for item in [ "A", "B", "C" ]:
    listbox.insert( "end", item )

listbox.pack()

winForm.mainloop()
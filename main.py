from tkinter import *

root = Tk()

# Number display
display = Entry(root)

display.grid(row=0,columnspan=3)

# numeric buttons
numbers = 1
for x in range(3):
    for y in range(3):
        btn = Button(root,text=numbers,width=2,height=2)
        btn.grid(row=x+2,column=y)
        numbers += 1

# number 0
btn = Button(root,text="0",width=2,height=2)
btn.grid(row=5,column=1)
root.mainloop()
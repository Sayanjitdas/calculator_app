from tkinter import *
import ast

root = Tk()

DISPLAY_INDEX = 0

def get_numbers(num):
    global DISPLAY_INDEX
    display.insert(DISPLAY_INDEX,num)
    DISPLAY_INDEX += 1


def get_operator(ops):
    global DISPLAY_INDEX
    display.insert(DISPLAY_INDEX,ops)
    DISPLAY_INDEX += len(ops)


def all_clear():
    global DISPLAY_INDEX
    display.delete(0,END)
    DISPLAY_INDEX = 0    


def calculate():
    global DISPLAY_INDEX
    try:
        entire_string = display.get()
        node = ast.parse(entire_string,mode="eval")
        result = eval(compile(node,'<string>',"eval"))
        all_clear()
        display.insert(0,result)
        DISPLAY_INDEX += len(str(result))
    except Exception as _:
        all_clear()
        display.insert(0,"Error")


def undo():
    global DISPLAY_INDEX
    entire_string = display.get()
    if len(entire_string):
        new_str = entire_string[:-1]
        all_clear()
        display.insert(0,new_str)
        DISPLAY_INDEX += len(new_str)

############################ UI widgets #######################################

# Number display
display = Entry(root)

display.grid(row=0,columnspan=6)

# numeric buttons
numbers = 1
for x in range(3):
    for y in range(3):
        btn = Button(root,text=numbers,width=2,height=2,command=lambda num=numbers:get_numbers(num))
        btn.grid(row=x+2,column=y)
        numbers += 1

# number 0
btn = Button(root,text="0",width=2,height=2,command=lambda:get_numbers(0))
btn.grid(row=5,column=1)


# operations
operations = ["+","-","*","/","*3.14","%","(","**",")","**2"]
ops_count = 0
for x in range(4):
    for y in range(3):
        if ops_count < len(operations):
            btn = Button(root,text=operations[ops_count],width=2,height=2,command=lambda ops=operations[ops_count]:get_operator(ops))
            ops_count += 1
            btn.grid(row=x+2,column=y+3)
            

# all clear
btn = Button(root,text="AC",width=2,height=2,command=all_clear)
btn.grid(row=5,column=0)

# equals to
btn = Button(root,text="=",width=2,height=2,command=calculate)
btn.grid(row=5,column=2)

# undo btn
btn = Button(root,text="<-",width=2,height=2,command=undo)
btn.grid(row=5,column=4)

root.mainloop()
from tkinter import *
import random 

master = Tk()
mylist = []

def close_window():
    for i in range(0,6):
        x = random.randint(0,9)
        mylist.append(x)

        print(mylist)
        
    exit()

myList = Button(master, text = 'Generate', command = close_window, bg = 'Beige', font = 'Roboto', activebackground = 'maroon', bd = '5', padx = '4', pady = '4')
myList. pack()
mainloop()
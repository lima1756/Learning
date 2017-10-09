import tkinter as tk
from tkinter import ttk;


win = tk.Tk();
win.title("My GUI");
#This blocks the resize window function
    #win.resizable(0,0);  


#Configuring and creating a label instance
aLabel = ttk.Label(win, text="My cute Label *w*")
aLabel.grid(column=0, row=0);

#click event
def clickMe():
    global action
    global aLabel
    action.configure(text="You have pressed the button o.o")
    aLabel.configure(foreground="red")
    aLabel.configure(text="Now I'm red ._.")

action = ttk.Button(win, text="I'm a button :3", command=clickMe)
action.grid(column=0, row=1)

win.mainloop();



from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.create_text(0,0, text="Hola")
canvas.pack()
time = 0
def tick():
    canvas.delete(ALL)
    # I have to declare time as a global because I'm not using
    # a class (otherwise, I could do something like self.time -= 1)
    global time
    time += 1
    # You can place the time wherever in the canvas
    # (I chose 10,10 for the example)
    canvas.create_text(10, 10, text=time)
    if time == 0:
        do_something()
    else:
        canvas.after(1000, tick)
canvas.after(1, tick)
root.mainloop()

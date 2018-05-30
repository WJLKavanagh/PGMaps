from Tkinter import *
master = Tk()

canvas_width = 1200
canvas_height = 900
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

# Draw Isometric grid
 # Draw NW-SE lines
for i in range(20):
    w.create_line(0, i*50, canvas_width, i*50 + 100, fill="grey")


y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")


mainloop()

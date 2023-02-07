from drawingpanel import *
window = drawingpanel(500, 400)
g = window.get_graphics()
for i in range(1, 11):
x = 100 + 20 * i
y = 5 + 20 * i
g.create_oval(x, y, x + 50, y + 50, fill="red")
window.mainloop()

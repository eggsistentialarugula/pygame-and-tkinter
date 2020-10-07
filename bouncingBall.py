from tkinter import *
import time

gui = Tk()
gui.geometry("600x600")
gui.title("Bouncing Ball")

c = Canvas(gui, width = 600, height = 600)
c.pack()

oval = c.create_oval(5,5,60,60,fill = 'blue')
xd = 5
yd = 10

while True:

	c.move(oval,xd,yd)
	p=c.coords(oval)
	if p[3] >= 600 or p[1] <= 0:
		yd = -yd
	if p[2] >= 600 or p[0] <= 0:
		xd = -xd

	gui.update()
	time.sleep(0.025)

gui.mainloop()
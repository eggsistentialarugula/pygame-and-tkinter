import tkinter as tkr
import time


tk = tkr.Tk()
canvas = tkr.Canvas(tk, width = 300, height = 400)
canvas.grid()

ball = canvas.create_oval(5,5,60,60,fill = "light blue")
#"""Pos[left, Top, right, bottom]

x = 1
y = 4

while True:
	canvas.move(ball,x,y)
	pos = canvas.coords(ball)
	if pos[3] >= 400 or pos[1] <= 0:
		y = -y
	if pos[2] >= 300 or pos[0] <= 0:
		x = -x
	tk.update()
	time.sleep(0.025)
	pass

tk.mainloop()
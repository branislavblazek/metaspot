import tkinter as t
import consts as c
from screen.intro import Intro

canvas = t.Canvas(width=c.WIDTH, height=c.HEIGHT, bg='black')
canvas.pack()

Intro(canvas)

canvas.mainloop()

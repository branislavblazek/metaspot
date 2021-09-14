import tkinter as t
from screen.intro import Intro

canvas = t.Canvas(width=900, height=600, bg='black')
canvas.pack()

canvas.after(200)
Intro(canvas)
canvas.update()

input()
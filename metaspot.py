import tkinter as t
import consts as c
import data as d
from screen.intro import Intro
from screen.menu import Menu

canvas = t.Canvas(width=c.WIDTH, height=c.HEIGHT, bg='black')
canvas.pack()

class Metaspot:
	def __init__(self, canvas):
		self.canvas = canvas
		self.isIntro = True
		self.isMenu = False
		self.name = ''
		self.score = 0
		self.render()

	def handle_action(self, attr):
		if attr == c.EXIT_INTRO:
			self.isIntro = False
			self.isMenu = True
			self.render()
		if attr == c.EXIT_MENU:
			self.isIntro = True
			self.isMenu = False
			self.render()

	def handle_new_name(self, new_name):
		self.name = new_name
		self.render()

	def render(self):
		self.canvas.delete('all')

		self.canvas.create_text(c.HALF_WIDTH,100, text="://metaspot",font=c.HEADING_FONT, fill='green')
		self.canvas.create_text(10,575, text="version_0.4", font=c.SMALL_FONT, fill="green", anchor="nw")
		self.canvas.create_text(c.WIDTH-250,575, text="made by: branislav", font=c.SMALL_FONT, fill="green", anchor="nw")

		if self.isIntro: Intro(canvas, self.name, self.score, self.handle_action, self.handle_new_name)
		if self.isMenu: Menu(canvas, d.MENU_GAMES, self.handle_action)

		canvas.mainloop()

Metaspot(canvas)
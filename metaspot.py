import tkinter as t
import consts as c
from utils import pick_from_list_dict
from data_handler import GetName, GetScore, SetName, GetGames
from screen.intro import Intro
from screen.menu import Menu
from screen.games.hangman import Hangman

canvas = t.Canvas(width=c.WIDTH, height=c.HEIGHT, bg='black')
canvas.pack()

class Metaspot:
	def __init__(self, canvas):
		self.canvas = canvas
		self.isIntro = True
		self.isMenu = False
		self.name = str(GetName())
		self.score = GetScore()
		self.games = GetGames().get_data()
		self.selected_game = None
		self.selected_level = None
		self.render()

	def handle_action(self, attr, args=None):
		if attr == c.EXIT_INTRO:
			self.isIntro = False
			self.isMenu = True
			self.render()
		elif attr == c.EXIT_MENU:
			self.isIntro = True
			self.isMenu = False
			self.render()
		elif attr in [c.START_HANGMAN, c.START_CRACK_THE_CODE]:
			self.isIntro = False
			self.isMenu = False
			self.selected_game = pick_from_list_dict(self.games, 'value', attr)
			self.selected_level = pick_from_list_dict(self.selected_game['levels'], 'value', args)
			self.render()

	def handle_new_name(self, new_name):
		self.name = new_name
		SetName(self.name)
		self.render()

	def handle_after_hangman(self, action):
		if action == c.EXIT_GAME:
			self.selected_game = None
			self.selected_level = None
			self.isIntro = True
		else:
			print(self.selected_game, self.selected_level)
			pass
		self.render()

	def render(self):
		self.canvas.delete('all')

		if not self.selected_game or not self.selected_level:
			self.canvas.create_text(c.HALF_WIDTH,100, text="://metaspot",font=c.HEADING_FONT, fill='green')
			self.canvas.create_text(10,570, text="version: 0.8", font=c.SMALL_FONT, fill="green", anchor="nw")
			self.canvas.create_text(c.WIDTH-300,570, text="made by: branislav", font=c.SMALL_FONT, fill="green", anchor="nw")

			if self.isIntro: Intro(canvas, self.name, self.score, self.handle_action, self.handle_new_name)
			if self.isMenu: Menu(canvas, self.games, self.handle_action)

		else:
			if self.selected_game['value'] == c.START_HANGMAN: Hangman(canvas, self.selected_level, self.handle_after_hangman)

		canvas.mainloop()

Metaspot(canvas)
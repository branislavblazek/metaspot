import consts as c
import data_general as d
from .prompt import Prompt

TEXT = 'GAME WIN!'
TEXT_LEN = len(TEXT)

class GameWinner:
	def __init__(self, canvas, on_action, is_dev=False):
		self.canvas = canvas
		self.done_animation = False
		self.prompt_index = 0
		self.on_action = on_action
		self.is_dev = is_dev
		self.render()

	def handle_enter(self, active_index):
		self.on_action(active_index)
		self.render(33)

	def handle_input(self, active_index):
		self.prompt_index = active_index
		self.render(33)

	def render(self, index=0):
		if index > 32: 
			self.canvas.delete('game_winner_prompt')

		if index == 0:
			for index_letter in range(len(TEXT)):
				tag = 'game_winner_even' if index_letter % 2 == 0 else 'game_winner_odd'
				y = 610 if index_letter % 2 == 0 else -10
				self.canvas.create_text(180 + 110 * index_letter, y, text=TEXT[index_letter], font=c.EXTRA_FONT, fill='green', tag=tag)

		if index <= 30:
			self.canvas.move('game_winner_even', 0, -10)
			self.canvas.move('game_winner_odd', 0, 10)

		if index == 31: self.done_animation = True

		if index >= 32:
			Prompt(self.canvas, 600, 400, 800, d.GAME_OVER_ACTIONS, self.handle_input, self.handle_enter, self.prompt_index, 'game_winner_prompt')

		if index < 32:
			self.canvas.after(0 if self.is_dev else 50)
			self.canvas.update()
			self.render(index+1)
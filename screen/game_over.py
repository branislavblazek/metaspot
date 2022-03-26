import consts as c
import data_general as d
from .prompt import Prompt

TEXT = 'GAME OVER!'
TEXT_LEN = len(TEXT)

class GameOver:
	def __init__(self, canvas, on_action):
		self.canvas = canvas
		self.done_animation = False
		self.prompt_index = 0
		self.on_action = on_action
		self.render()

	def handle_enter(self, active_index):
		self.on_action(active_index)
		self.render(33)

	def handle_input(self, active_index):
		self.prompt_index = active_index
		self.render(33)

	def render(self, index=0):
		if index > 32: 
			self.canvas.delete('game_over_prompt')

		if index == 0:
			text_even = '    '.join(TEXT[::2])
			text_odd = '    '.join(TEXT[1::2])
			self.canvas.create_text(580, 610, text=text_even, font=c.EXTRA_FONT, fill='green', tag='game_over_even')
			self.canvas.create_text(660, -10, text=text_odd, font=c.EXTRA_FONT, fill='green', tag='game_over_odd')

		if index <= 30:
			self.canvas.move('game_over_even', 0, -10)
			self.canvas.move('game_over_odd', 0, 10)

		if index == 31: self.done_animation = True

		if index >= 32:
			Prompt(self.canvas, 600, 400, 800, d.GAME_OVER_ACTIONS, self.handle_input, self.handle_enter, self.prompt_index, 'game_over_prompt')

		if index < 32:
			self.canvas.after(50)
			self.canvas.update()
			self.render(index+1)
import consts as c
from screen.select import Select

class Menu:
	def __init__(self, canvas, games, handle_action):
		self.canvas = canvas
		self.tag = 'menu'
		self.games = games
		self.selected_game = None
		self.selected_level = None
		self.game_index = 0
		self.level_index = 0
		self.on_action = handle_action

		self.render()

	def find_level(self, game): return game['value'] == self.selected_game

	def handle_select_input(self, active_index):
		if self.selected_game is None:
			self.game_index = active_index
		else: 
			self.level_index = active_index

		self.render()

	def handle_select_enter(self, active_index):
		if self.selected_game is None:
			value = self.games[active_index]['value']
		else:
			value = list(filter(self.find_level, self.games))[0]['levels'][active_index]['value']

		if value == c.EXIT_MENU:
			self.on_action(c.EXIT_MENU)
		if value == c.EXIT_LEVEL_MENU:
			self.selected_game = None
			self.render()
		else:
			if self.selected_game is None:
				self.selected_game = value
				self.selected_level = None
				self.level_index = 0
				self.render()
			else:
				self.selected_level = value
				self.on_action(self.selected_game, self.selected_level)

		self.render()

	def render(self):
		self.canvas.delete(self.tag)

		if self.selected_game is None:
			self.canvas.create_text(50, c.INTRO_COMPONENT_OFFSET, text="Select one of the avaible games:", font=c.REGULAR_FONT, fill='green', anchor='nw', tag=self.tag)
			Select(self.canvas, c.INTRO_SELECT_START[0], c.INTRO_SELECT_START[1], c.INTRO_SELECT_OFFSET, self.games, self.handle_select_input, self.handle_select_enter, self.game_index, self.tag)
		elif self.selected_game is not None:
			self.canvas.create_text(50, c.INTRO_COMPONENT_OFFSET, text="Select level you want to play:", font=c.REGULAR_FONT, fill='green', anchor='nw', tag=self.tag)
			levels = list(filter(self.find_level, self.games))[0]['levels']
			Select(self.canvas, c.INTRO_SELECT_START[0], c.INTRO_SELECT_START[1], c.INTRO_SELECT_OFFSET, levels, self.handle_select_input, self.handle_select_enter, self.level_index, self.tag)
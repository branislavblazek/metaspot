import sys
sys.path.append(".")
import consts as c
from utils import uppercase_string, is_uppercase_string
from ..game_over import GameOver
from ..game_winner import GameWinner

INTRO_START = 250
INTRO_LETTER_SIZE = 120
MAX_ROW_LENGTH = 10

INTRO_LETTERS = [
	{ 'letter': 'N', 'offset': 2 },
	{ 'letter': 'M', 'offset': 3 },
	{ 'letter': 'A', 'offset': -1 },
	{ 'letter': 'N', 'offset': 3 },
	{ 'letter': 'H', 'offset': -4 },
	{ 'letter': 'A', 'offset': 0 },
	{ 'letter': 'G', 'offset': -3 },
]

HANGMAN_COORDS = [(100,50,100,350), (100,100,150,50), (100,50,250,50), 
	(250,50,250,100), (250,100,30), (250,160,200,220), 
	(250,160,300,220), (250,160,250,260), (250,260,220,320), (250,260,280,320)]

class Hangman:
	def __init__(self, canvas, data, handle_unlock_next_level, handle_after_game, is_dev=False):
		self.canvas = canvas
		self.data = data
		self.data['data'] = uppercase_string(self.data['data'])
		self.tag = 'hangman'
		self.done_intro = False
		self.game_over = False
		self.game_winner = False
		self.used = []
		self.wrong = []
		self.guessed = []
		self.handle_unlock_next_level = handle_unlock_next_level
		self.handle_after_game = handle_after_game
		self.is_dev = is_dev
		self.render()

	def intro(self, index=0):
		text = '_' if index < 7 else ''
		x = INTRO_START + INTRO_LETTER_SIZE * (index % 7)
		offset = 0

		if index >= 7:
			offset = INTRO_LETTERS[index % 7]['offset'] * INTRO_LETTER_SIZE
			text = INTRO_LETTERS[index % 7]['letter']

		if index <= 14: self.canvas.create_text(x + offset, 300, text=text, font=c.EXTRA_FONT, fill='green', tag=self.tag)
		elif index == 15: self.canvas.create_text(700, 600, text=self.data['text'], font=c.REGULAR_FONT, fill='green', tag='level_text')
		elif index >= 16: self.canvas.coords('level_text', 700, 600 - 18 * (index % 16))

		if index <= 25:
			self.canvas.after(0 if self.is_dev else 200)
			self.canvas.update()
			if index == 25:
				self.done_intro = True
				self.canvas.after(0 if self.is_dev else 400)
				self.canvas.update()
				self.render()
			self.intro(index+1)

	def draw_alphabet(self):
		for i in range(65, 91):
			letter = chr(i)
			x = i - 65
			y = 420 if x < 13 else 540
			color = 'green' if letter not in self.used else 'black'
			self.canvas.create_text(100 + 80 * (x % 13), y, text=letter, font=c.HEADING_FONT, fill=color, tag=self.tag)

	def shape(self, x1, y1, x2, y2=None): 
		if y2 == None:
			self.canvas.create_oval(x1-x2,y1,x1+x2,y1+x2+x2,outline='green', width=3, tag=self.tag)
		else:
			self.canvas.create_line(x1,y1,x2,y2,fill='green', width=3,tag=self.tag)

	def draw_hangman(self):
		for i in range(len(self.wrong)): self.shape(*HANGMAN_COORDS[i])

	def draw_word(self):
		word = self.data['data']
		for letter_index in range(len(word)):
			is_used = word[letter_index] in self.used
			text = word[letter_index] if is_used else '_'
			x = 400 + 80 * (letter_index % MAX_ROW_LENGTH)
			y = 120 + 120 * (letter_index // MAX_ROW_LENGTH)
			self.canvas.create_text(x, y, text=text, font=c.HEADING_FONT, fill='green', tag=self.tag)

	def handle_input(self, event):
		letter = event.char
		uppercase = uppercase_string(letter)
		is_ok = is_uppercase_string(uppercase) and uppercase not in self.used
		if is_ok:
			self.used.append(uppercase)
			if uppercase in self.data['data']:
				self.guessed.append(uppercase)
			else:
				self.wrong.append(uppercase)
			self.render()

	def check_score(self):
		con = True
		corr_word = ''.join(sorted(set(self.data['data'])))
		is_wrong = len(''.join(self.wrong)) == 10
		is_right = ''.join(sorted(self.guessed)) == corr_word
		if is_wrong:
			self.game_over = True
			con = False
			self.render()
		elif is_right:
			self.game_winner = True
			con = False
			self.render()
		return con

	def render(self):
		self.canvas.delete(self.tag)
		self.canvas.delete('level_text')
		self.canvas.unbind_all('<Key>')

		if not self.done_intro: self.intro()
		elif self.game_over: GameOver(self.canvas, self.handle_after_game, self.is_dev)
		elif self.game_winner:
			self.handle_unlock_next_level()
			GameWinner(self.canvas, self.handle_after_game, self.is_dev)
		else:
			con = self.check_score()
			if con:
				self.draw_alphabet()
				self.draw_hangman()
				self.draw_word()
				self.canvas.bind_all('<Key>', self.handle_input)
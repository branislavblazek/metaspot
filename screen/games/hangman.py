import consts as c

INTRO_START = 250
INTRO_LETTER_SIZE = 110

INTRO_LETTERS = [
	{ 'letter': 'N', 'offset': 2 },
	{ 'letter': 'M', 'offset': 3 },
	{ 'letter': 'A', 'offset': -1 },
	{ 'letter': 'N', 'offset': 3 },
	{ 'letter': 'H', 'offset': -4 },
	{ 'letter': 'A', 'offset': 0 },
	{ 'letter': 'G', 'offset': -3 },
]

class Hangman:
	def __init__(self, canvas, data):
		self.canvas = canvas
		self.tag = 'hangman'
		self.done_intro = False
		self.guessed = []
		self.render()

	def intro(self, index=0):
		text = '_' if index < 7 else ''
		x = INTRO_START + INTRO_LETTER_SIZE * (index % 7)
		offset = 0

		if index >= 7:
			offset = INTRO_LETTERS[index % 7]['offset'] * INTRO_LETTER_SIZE
			text = INTRO_LETTERS[index % 7]['letter']

		if index <= 14: self.canvas.create_text(x + offset, 300, text=text, font=c.EXTRA_FONT, fill='green', tag=self.tag)
		elif index == 15: self.canvas.create_text(700, 600, text='level 1', font=c.REGULAR_FONT, fill='green', tag='level_text')
		elif index >= 16: self.canvas.coords('level_text', 700, 600 - 18 * (index % 16))

		if index <= 25:
			# UPDATE 00
			self.canvas.after(2)
			self.canvas.update()
			if index == 25:
				self.done_intro = True
				# UPDATE 00
				self.canvas.after(4)
				self.canvas.update()
				self.render()
			self.intro(index+1)

	def draw_alphabet(self):
		for i in range(65, 91):
			letter = chr(i)
			x = i - 65
			y = 420 if x < 13 else 540
			self.canvas.create_text(100 + 80 * (x % 13), y, text=letter, font=c.HEADING_FONT, fill='green', tag=self.tag)

	def line(self, x1, y1, x2, y2, fill=True): self.canvas.create_line(x1,y1,x2,y2,fill='green' if fill else 'black', width=3)

	def oval(self, x, y, r, fill=True): self.canvas.create_oval(x-r,y,x+r,y+r+r,outline='green' if fill else 'black', width=3)

	def draw_hangman(self):
		self.line(100,50,100,350)
		self.line(100,100,150,50)
		self.line(100,50,250,50)
		self.line(250,50,250,100)
		self.oval(250,100,30)
		self.line(250,160,200,220)
		self.line(250,160,300,220)
		self.line(250,160,250,260)
		self.line(250,260,220,320)
		self.line(250,260,280,320)

	def render(self):
		self.canvas.delete(self.tag)
		self.canvas.delete('level_text')

		if not self.done_intro: self.intro()
		else:
			self.draw_alphabet()
			self.draw_hangman()
import consts as c
from screen.select import Select

class Intro:
    def __init__(self, canvas):
        self.canvas = canvas
        self.active_index = 0
        self.choices = ['edit your name', 'start ://metaspot']
        
        self.canvas.create_text(450,100, text="://metaspot",font=c.HEADING_FONT, fill='green')
        self.canvas.create_text(65,585, text="version_0.1", font=c.SMALL_FONT, fill="green")
        self.canvas.create_text(800,585, text="made by: branislav", font=c.SMALL_FONT, fill="green")
        
        Select(canvas, c.INTRO_SELECT_START[0], c.INTRO_SELECT_START[1], c.INTRO_SELECT_OFFSET, self.choices, self.active_index)

        self.canvas.bind_all('<Up>', self.update_active_index)
        self.canvas.bind_all('<Down>', self.update_active_index)


    def update_active_index(self, a):
        add_number = 1 if a.keysym == 'Up' else -1 if a.keysym == 'Down' else 0

        length = len(self.choices)

        print(self.active_index, add_number, length)
        if self.active_index + add_number >= length:
            self.active_index = 0
        elif self.active_index < 0:
            self.active_index += add_number
        else:
            self.active_index += add_number
        print(self.active_index)

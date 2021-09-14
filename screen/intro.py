import consts as c
from screen.select import Select

class Intro:
    def __init__(self, canvas):
        self.canvas = canvas
        self.active_index = 0
        self.choices = ['edit your name', 'start ://metaspot']

        self.canvas.create_text(450,100, text="://metaspot",font=c.HEADING_FONT, fill='green')
        self.canvas.create_text(10,575, text="version_0.2", font=c.SMALL_FONT, fill="green", anchor="nw")
        self.canvas.create_text(670,575, text="made by: branislav", font=c.SMALL_FONT, fill="green", anchor="nw")

        self.render_select()

        self.canvas.bind_all('<Up>', self.update_active_index)
        self.canvas.bind_all('<Down>', self.update_active_index)

    def render_select(self):
        self.canvas.delete('intro_select')
        Select(self.canvas, c.INTRO_SELECT_START[0], c.INTRO_SELECT_START[1], c.INTRO_SELECT_OFFSET, self.choices, self.active_index, 'intro_select')

    def update_active_index(self, a):
        add_number = -1 if a.keysym == 'Up' else 1 if a.keysym == 'Down' else 0

        length = len(self.choices)

        new_value = self.active_index + add_number

        if new_value >= length:
            self.active_index = length -1
        elif new_value < 0:
            self.active_index = 0
        else:
            self.active_index = new_value

        self.render_select()

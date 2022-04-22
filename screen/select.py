from tkinter.tix import MAX
import consts as c

MAX_SHOW = 5

class Select(object):
    def __init__(self, canvas, x, y, offset, choices, on_input, on_select, active_index=0, tag=''):
        self.canvas = canvas
        self.tag = tag
        self.on_input = on_input
        self.on_select = on_select
        self.active_index = active_index
        self.choices = choices

        start = 0 if self.active_index < MAX_SHOW else (self.active_index + 1) % MAX_SHOW
        print(self.active_index, MAX_SHOW)
        slider = range(start, min(len(choices)+start, MAX_SHOW+start))
        for i in slider:
            is_unlocked = self.get_is_unlocked(choices[i])
            text = ''.join([choices[i]['text'], '' if is_unlocked else ' [locked]'])
            self.render_choice(x, y + (offset * ((i - start) % MAX_SHOW)), text, i == active_index)

        self.canvas.bind_all('<Up>', self.handle_input)
        self.canvas.bind_all('<Down>', self.handle_input)
        self.canvas.bind_all('<Return>', self.handle_enter)

    def get_is_unlocked(self, item):
        return item['unlocked'] if "unlocked" in item else True

    def render_choice(self, x, y, value, active=False):
        if active:
            self.canvas.create_text(x - c.SELECT_ACTIVE_OFFSET, y, text=c.SELECT_ACTIVE, font=c.REGULAR_FONT, fill="green", anchor="nw", tag=self.tag)
        self.canvas.create_text(x, y, text=value, font=c.REGULAR_FONT, fill="green", anchor="nw", tag=self.tag)

    def handle_enter(self, _):
        is_unlocked = self.get_is_unlocked(self.choices[self.active_index])
        if is_unlocked: self.on_select(self.active_index)

    def handle_input(self, input):
        add_number = -1 if input.keysym == 'Up' else 1 if input.keysym == 'Down' else 0
        length = len(self.choices)
        new_value = self.active_index + add_number
        to_return = new_value

        if new_value >= length:
            to_return = length -1
        elif new_value < 0:
            to_return = 0

        self.on_input(to_return)

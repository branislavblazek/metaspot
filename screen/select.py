import consts as c

class Select:
    def __init__(self, canvas, x, y, offset, choices, active_index=0, tag=''):
        self.canvas = canvas
        self.tag = tag

        for i in range(len(choices)):
            self.render_choice(x, y+(offset * i), choices[i], i == active_index)

    def render_choice(self, x, y, value, active=False):
        if active:
            self.canvas.create_text(x - c.SELECT_ACTIVE_OFFSET, y, text=c.SELECT_ACTIVE, font=c.SELECT_FONT, fill="green", anchor="nw", tag=self.tag)
        self.canvas.create_text(x, y, text=value, font=c.SELECT_FONT, fill="green", anchor="nw", tag=self.tag)

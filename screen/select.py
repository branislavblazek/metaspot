import consts as c

class Select:
    def __init__(self, canvas, x, y, offset, choices, active_index=0):
        self.canvas = canvas

        for i in range(len(choices)):
            self.render_choice(x, y+(offset * i), choices[i], i == active_index)

    def render_choice(self, x, y, value, active=False):
        text_value = '> ' + value if active else value
        self.canvas.create_text(x, y, text=text_value, font=c.SELECT_FONT, fill="green", anchor="nw")
        

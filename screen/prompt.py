import consts as c

class Prompt:
    def __init__(self, canvas, x, y, width, value, on_input, on_select, active_index, tag):
        self.canvas = canvas
        self.value = value
        self.on_input = on_input
        self.on_select = on_select
        self.active_index = active_index
        self.tag = tag

        self.render_prompt(x, y, width)

        self.canvas.bind_all('<Left>', self.handle_input)
        self.canvas.bind_all('<Right>', self.handle_input)
        self.canvas.bind_all('<Return>', self.handle_enter)


    def render_prompt(self, x, y, width):
        self.canvas.create_rectangle(x-width//2,y,x+width//2,y+40, fill='green', outline='', tag=self.tag)
        self.canvas.create_text(x, y, text=self.value['heading'], font=c.REGULAR_FONT, fill='black', anchor='n', tag=self.tag)

        length = len(self.value['data'])
        box_width = width // length

        for i in range(length):
            start = x + (i - 1) * box_width
            box_color = 'green' if i == self.active_index else 'black'
            text_color = 'black' if i == self.active_index else 'green'
            self.canvas.create_rectangle(start, y + 100, start + box_width, y+140, fill=box_color, outline='', tag=self.tag)
            self.canvas.create_text(start + box_width // 2, y + 100, text=self.value['data'][i]['text'], font=c.REGULAR_FONT, fill=text_color, anchor='n', tag=self.tag)

    def handle_enter(self, _):
        self.on_select(self.value['data'][self.active_index]['value'])

    def handle_input(self, input):
        add_number = -1 if input.keysym == 'Left' else 1 if input.keysym == 'Right' else 0
        length = len(self.value['data'])
        new_value = self.active_index + add_number
        to_return = new_value

        if new_value >= length:
            to_return = length -1
        elif new_value < 0:
            to_return = 0

        self.on_input(to_return)

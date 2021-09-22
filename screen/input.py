import consts as c

class Input:
    def __init__(self, canvas, x, y, width, value, on_select, name, tag):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.value = value
        self.on_select = on_select
        self.name = name
        self.tag = tag

        self.render_input()

        self.canvas.bind_all('<Key>', self.handle_input)
        self.canvas.bind_all('<Return>', self.handle_enter)
        self.canvas.bind_all('<BackSpace>', self.handle_remove)

    def render_input(self):
        x = self.x
        y = self.y
        width = self.width
        self.canvas.create_rectangle(x-width//2,y,x+width//2,y+40, fill='green', outline='', tag=self.tag)
        self.canvas.create_text(x, y, text=self.value['heading'], font=c.REGULAR_FONT, fill='black', anchor='n', tag=self.tag)

        self.canvas.create_rectangle(x-width//2,y+100,x+width//2,y+140, fill='black', outline='green', tag=self.tag)
        self.canvas.create_text(x, y + 100, text=self.name, font=c.REGULAR_FONT, fill='green', anchor='n', tag=self.tag)

    def handle_input(self, key):
        new_name = self.name + key.char
        self.name = new_name if len(new_name) <= 15 else self.name
        self.render_input()

    def handle_remove(self, _):
        if len(self.name) >= 1:
            self.name = self.name[:-1]
        else:
            self.name = ''
        self.render_input()

    def handle_enter(self, _):
        self.on_select(self.name)

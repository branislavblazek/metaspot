import consts as c
from screen.select import Select
from screen.prompt import Prompt
from screen.input import Input

class Intro:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tag = 'intro'
        self.active_index = 0
        self.exit_prompt_index = 0
        self.name = ''
        self.score = 0
        self.choices = [
            {
                'text': 'start ://metaspot',
                'value': 'start',
            },
            {
                'text': 'edit your name',
                'value': 'edit_name',
                'heading': 'Edit here your name:',
            },
            {
                'text': 'exit',
                'value': 'exit',
                'heading': 'Are you sure?',
                'data': [
                    {
                        'text': 'No!',
                        'value': False,
                    },
                    {
                        'text': 'Yes!',
                        'value': True,
                    }
                ]
            }
        ]
        self.active_choice = None
        self.render()

    def handle_select_enter(self, active_index):
        value = self.choices[active_index]['value']
        self.active_choice = value
        self.render()

    def handle_select_input(self, active_index):
        self.active_index = active_index
        self.render()

    def handle_exit_enter(self, chosen_value):
        if chosen_value == False:
            self.active_choice = None
            self.render()
        elif chosen_value == True:
            quit()

    def handle_exit_input(self, active_index):
        self.exit_prompt_index = active_index
        self.render()

    def handle_name_enter(self, new_name):
        self.name = new_name
        self.active_choice = None
        self.render()

    def render(self):
        self.canvas.delete(self.tag)

        self.canvas.create_text(c.HALF_WIDTH,100, text="://metaspot",font=c.HEADING_FONT, fill='green')
        self.canvas.create_text(10,575, text="version_0.3", font=c.SMALL_FONT, fill="green", anchor="nw")
        self.canvas.create_text(c.WIDTH-250,575, text="made by: branislav", font=c.SMALL_FONT, fill="green", anchor="nw")

        if self.active_choice == None:
            self.canvas.create_text(50, c.INTRO_COMPONENT_OFFSET, text="Welcome here, {}! [x{}]".format(self.name or '[no_username]', self.score), font=c.REGULAR_FONT, fill='green', anchor='nw', tag=self.tag)
            Select(self.canvas, c.INTRO_SELECT_START[0], c.INTRO_SELECT_START[1], c.INTRO_SELECT_OFFSET, self.choices, self.handle_select_input, self.handle_select_enter, self.active_index, self.tag)
        elif self.active_choice == 'edit_name':
            Input(self.canvas, c.HALF_WIDTH, c.INTRO_COMPONENT_OFFSET, c.INTRO_COMPONENT_WIDTH, self.choices[1], self.handle_name_enter, self.name, self.tag)
        elif self.active_choice == 'exit':
            Prompt(self.canvas, c.HALF_WIDTH, c.INTRO_COMPONENT_OFFSET, c.INTRO_COMPONENT_WIDTH, self.choices[2], self.handle_exit_input, self.handle_exit_enter, self.exit_prompt_index, self.tag)

import consts as c
import data as d
from screen.select import Select
from screen.prompt import Prompt
from screen.input import Input

class Intro:
    def __init__(self, canvas, name, score, handle_action, handle_name_change):
        self.canvas = canvas
        self.tag = 'intro'
        self.active_index = 0
        self.exit_prompt_index = 0
        self.name = name
        self.score = score
        self.choices = d.INTRO_ACTIONS
        self.active_choice = None
        self.on_action = handle_action
        self.on_name_change = handle_name_change
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
        self.on_name_change(new_name)
        self.active_choice = None
        self.render()

    def render(self):
        self.canvas.delete(self.tag)

        if self.active_choice == None:
            self.canvas.create_text(50, c.INTRO_COMPONENT_OFFSET, text="Welcome here, {}! [x{}]".format(self.name or '[no_username]', self.score), font=c.REGULAR_FONT, fill='green', anchor='nw', tag=self.tag)
            Select(self.canvas, c.INTRO_SELECT_START[0], c.INTRO_SELECT_START[1], c.INTRO_SELECT_OFFSET, self.choices, self.handle_select_input, self.handle_select_enter, self.active_index, self.tag)
        elif self.active_choice == c.EXIT_INTRO:
            self.on_action(c.EXIT_INTRO)
        elif self.active_choice == c.EDIT_NAME:
            Input(self.canvas, c.HALF_WIDTH, c.INTRO_COMPONENT_OFFSET, c.INTRO_COMPONENT_WIDTH, self.choices[1], self.handle_name_enter, self.name, self.tag)
        elif self.active_choice == c.EXIT_GAME:
            Prompt(self.canvas, c.HALF_WIDTH, c.INTRO_COMPONENT_OFFSET, c.INTRO_COMPONENT_WIDTH, self.choices[2], self.handle_exit_input, self.handle_exit_enter, self.exit_prompt_index, self.tag)

from consts import USER_FILE, USER_NAME, USER_SCORE
from data_general import MENU_GAMES
from utils import dict_to_int

class GetData:
    def __init__(self, file):
        try:
            lines = open(file, 'r').readlines()
            self.values = dict()
            for line in lines:
                pair = [i.strip() for i in line.strip().split(':')]
                self.values[pair[0]] = pair[1]

        except:
            self.values = None

    def get_value(self, value): return self.values[value]

    def get_values(self): return self.values

class SetData:
    def __init__(self, file, key, value):
        self.file = file
        self.data = GetData(file).get_values()
        if key in self.data:
            self.data[key] = value
            self.write_data()

    def write_data(self):
        file = open(self.file, 'w')
        for key in self.data.keys():
            file.write('{}: {}\n'.format(key, self.data[key]))

class GetName:
    def __init__(self): self.name = GetData(USER_FILE).get_value(USER_NAME)

    def __str__(self): return self.name

class GetScore:
    def __init__(self): self.score = GetData(USER_FILE).get_value(USER_SCORE)

    def __str__(self): return '{}'.format(self.score)

class SetName:
    def __init__(self, name): SetData(USER_FILE, USER_NAME, name)

class GetGames:
    def __init__(self):
        self.games_data = []

        for game in MENU_GAMES:
            updated_levels = []
            if 'levels_data' in game.keys():
                levels_data = dict_to_int(GetData(game['levels_data']).get_values())
                for current_level in game['levels']:
                    current_level_value = current_level['value'] if current_level['value'] else None
                    if current_level['value'] in levels_data.keys():
                        correct_level = current_level
                        correct_level['unlocked'] = True if levels_data[current_level['value']] == 1 else False
                        updated_levels.append(correct_level)
                    else:
                        updated_levels.append(current_level)
                game['levels'] = updated_levels
            self.games_data.append(game)

    def get_data(self): return self.games_data
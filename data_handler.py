from consts import USER_FILE, USER_NAME, USER_SCORE

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

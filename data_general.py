import consts as c

INTRO_ACTIONS = [
    {
        'text': 'start ://metaspot',
        'value': c.EXIT_INTRO,
    },
    {
        'text': 'edit your name',
        'value': c.EDIT_NAME,
        'heading': 'Edit here your name:',
    },
    {
        'text': 'exit',
        'value': c.EXIT_GAME,
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

MENU_GAMES = [
	{
		'text': 'Hangman',
		'value': c.START_HANGMAN,
        'levels': [
            {
                'text': 'Level 01',
                'value': 0,
                'unlocked': True
            },
            {
                'text': 'Level 02',
                'value': 1,
                'unlocked': False
            },
            {
                'text': 'Level 03',
                'value': 2,
                'unlocked': False
            },
            {
                'text': 'Level 04',
                'value': 3,
                'unlocked': False
            },
            {
                'text': 'go back',
                'value': c.EXIT_LEVEL_MENU,
            },
        ]
	},
	{
		'text': 'Crack the Code [under dev]',
		'value': c.START_CRACK_THE_CODE,
        'levels': [
            {
                'text': 'Level 01',
                'value': 0,
                'unlocked': True
            },
            {
                'text': 'Level 02',
                'value': 1,
                'unlocked': False
            },
            {
                'text': 'Level 03',
                'value': 2,
                'unlocked': False
            },
            {
                'text': 'Level 04',
                'value': 3,
                'unlocked': False
            },
            {
                'text': 'go back',
                'value': c.EXIT_LEVEL_MENU,
                'unlocked': False
            },
        ]
	},
	{
		'text': 'go back',
		'value': c.EXIT_MENU,
	},
]

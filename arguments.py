

PATH =      ['--path',        {'type': str, 'default': '.',               'help': 'Path to git repository (default: current directory)'}]
MAJOR =     ['--major',     {'type': str, 'default': 'break',           'help': 'Major version keyword (default: break)'}]
MINOR =     ['--minor',     {'type': str, 'default': 'feat',            'help': 'Minor version keyword (default: feat)'}]
PATCH =     ['--patch',     {'type': str, 'default': 'fix',             'help': 'Patch version keyword (default: fix)'}]
COLOR =     ['--color',     {'type': lambda x: (x == 'True'),      'default': False, 'help': 'Colorize output (default: True)'}]

OUTPUT =    ['--output',      {'type': str, 'default': 'CHANGELOG.md',    'help': 'Output file (default: CHANGELOG.md)'}]

FILE =      ['--file',        {'type': str, 'default': '',                'help': 'Path to file to be signed (default: none)'}]

VERSION =   ['--version',     {'type': str, 'default': '*',               'help': 'Version of commit'}]
HASH =      ['--hash',        {'type': str, 'default': '*',               'help': 'Hash of commit'}]
DATE =      ['--date',        {'type': str, 'default': '*',               'help': 'Date of commit'}]
TIME =      ['--time',        {'type': str, 'default': '*',               'help': 'Time of commit'}]
KEYWORD =   ['--keyword',     {'type': str, 'default': '*',               'help': 'Keyword of commit'}]
AUTHOR =    ['--author',      {'type': str, 'default': '*',               'help': 'Author of commit'}]

FORMAT =    ['--format',     {'type': str, 'default': 'table',           'help': 'Format of commit {table, csv, json} (default: table)'}]

SCHEMA =    ['--schema',     {'type': str, 'default': ['version', 'hash', 'date', 'time', 'keyword', 'author', 'subject'], 
                             'help': 'Schema of commit (default: version, hash, date, time, keyword, author, message)', 'nargs': '+'}]
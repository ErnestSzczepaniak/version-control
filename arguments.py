
PATH =      ['-p', '--path',        {'type': str, 'default': '.',               'help': 'Path to git repository (default: current directory)'}]
MAJOR =     ['-maj', '--major',     {'type': str, 'default': 'break',           'help': 'Major version keyword (default: break)'}]
MINOR =     ['-min', '--minor',     {'type': str, 'default': 'feat',            'help': 'Minor version keyword (default: feat)'}]
PATCH =     ['-pch', '--patch',     {'type': str, 'default': 'fix',             'help': 'Patch version keyword (default: fix)'}]

OUTPUT =    ['-o', '--output',      {'type': str, 'default': 'CHANGELOG.md',    'help': 'Output file (default: CHANGELOG.md)'}]

FILE =      ['-f', '--file',        {'type': str, 'default': '',                'help': 'Path to file to be signed (default: none)'}]

VERSION =   ['-v', '--version',     {'type': str, 'default': '*',               'help': 'Version of commit'}]
HASH =      ['-h', '--hash',        {'type': str, 'default': '*',               'help': 'Hash of commit'}]
DATE =      ['-d', '--date',        {'type': str, 'default': '*',               'help': 'Date of commit'}]
TIME =      ['-t', '--time',        {'type': str, 'default': '*',               'help': 'Time of commit'}]
KEYWORD =   ['-k', '--keyword',     {'type': str, 'default': '*',               'help': 'Keyword of commit'}]
AUTHOR =    ['-a', '--author',      {'type': str, 'default': '*',               'help': 'Author of commit'}]

FORMAT =    ['-fm', '--format',     {'type': str, 'default': 'table',           'help': 'Format of commit {table, csv, json} (default: table)'}]

SCHEMA =    ['-sh', '--schema',     {'type': str, 'default': ['version', 'hash', 'date', 'time', 'keyword', 'author', 'subject'], 
                             'help': 'Schema of commit (default: version, hash, date, time, keyword, author, message)', 'nargs': '+'}]
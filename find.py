import github

ARGUMENTS = [
    ['--path',      {'type': str, 'default': '.',       'help': 'Path to git repository (default: current directory)'}],
    ['--major',     {'type': str, 'default': 'break',   'help': 'Major version keyword (default: break)'}],
    ['--minor',     {'type': str, 'default': 'feat',    'help': 'Minor version keyword (default: feat)'}],
    ['--patch',     {'type': str, 'default': 'fix',     'help': 'Patch version keyword (default: fix)'}],
    ['--version',   {'type': str, 'default': '*',       'help': 'Version of commit'}],
    ['--hash',      {'type': str, 'default': '*',       'help': 'Hash of commit'}],
    ['--date',      {'type': str, 'default': '*',       'help': 'Date of commit'}],
    ['--time',      {'type': str, 'default': '*',       'help': 'Time of commit'}],
    ['--keyword',   {'type': str, 'default': '*',       'help': 'Keyword of commit'}],
    ['--author',    {'type': str, 'default': '*',       'help': 'Author of commit'}],
    ['--format',    {'type': str, 'default': 'table',   'help': 'Format of commit {table, csv, json} (default: table)'}],
    ['--schema',    {'type': str, 'default': [
        'version', 'hash', 'date', 'time', 'keyword', 'author', 'subject',
    ],                                                  'help': 'Schema of commit (default: version, hash, date, time, keyword, author, message)', 'nargs': '+', }],
    ['--reverse',   {'type': bool,  'default': True,            'help': 'Reverse order of commits (default: False)'}]
]

def execute(**kwargs):

    client = github.Github(kwargs['path'])

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])

    if commits is None: return

    filter = {key: value for key, value in kwargs.items() if key in ['version', 'hash', 'date', 'time', 'keyword', 'author']}

    if kwargs['reverse']:
        commits.reverse()

    for commit in commits:

        if commit.match(filter):

            print(commit.format_as(kwargs['format'], kwargs['schema']))


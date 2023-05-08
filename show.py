import github

ARGUMENTS = [
    ['--path',      {'type': str, 'default': '.',       'help': 'Path to git repository (default: current directory)'}],
    ['--major',     {'type': str, 'default': 'break',   'help': 'Major version keyword (default: break)'}],
    ['--minor',     {'type': str, 'default': 'feat',    'help': 'Minor version keyword (default: feat)'}],
    ['--patch',     {'type': str, 'default': 'fix',     'help': 'Patch version keyword (default: fix)'}]
]

def execute(**kwargs):

    client = github.Client(kwargs['path'])

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])
    
    if commits is None: return

    print(commits[-1].version)
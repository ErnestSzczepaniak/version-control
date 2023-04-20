import github

ARGUMENTS = [
    ['--path',      {'type': str, 'default': '.',       'help': 'Path to git repository (default: current directory)'}],
    ['--major',     {'type': str, 'default': 'break',   'help': 'Major version keyword (default: break)'}],
    ['--minor',     {'type': str, 'default': 'feat',    'help': 'Minor version keyword (default: feat)'}],
    ['--patch',     {'type': str, 'default': 'fix',     'help': 'Patch version keyword (default: fix)'}]
]

def execute(**kwargs):

    client = github.Github(kwargs['path'])

    commits = client.commits()
    
    if commits is None: return

    versions = client.versions(commits, kwargs['major'], kwargs['minor'], kwargs['patch'])

    print(versions[-1])
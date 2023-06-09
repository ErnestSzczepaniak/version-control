import github, pathlib, arguments

ARGUMENTS = [
    arguments.PATH,
    arguments.MAJOR,
    arguments.MINOR,
    arguments.PATCH
]

def execute(**kwargs):

    path_repository = pathlib.Path(kwargs['path']).absolute().as_posix()

    client = github.Client(path_repository)

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])
    
    if commits is None: return

    print(commits[-1].version)
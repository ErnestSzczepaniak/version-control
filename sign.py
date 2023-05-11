import github, pathlib, arguments

ARGUMENTS = [
    arguments.PATH,
    arguments.MAJOR,
    arguments.MINOR,
    arguments.PATCH,
    arguments.FILE
]


def execute(**kwargs):
    
    path_repository = pathlib.Path(kwargs['path']).absolute().as_posix()

    client = github.Client(path_repository)

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])
    
    if commits is None: return

    version = commits[-1].version

    if kwargs['file'] == '': return

    path_file = pathlib.Path(kwargs['file']).absolute()

    if not path_file.exists(): return

    path_file.rename(path_file.with_name(f'{path_file.stem}-{version}{path_file.suffix}'))

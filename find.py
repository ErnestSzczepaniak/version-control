import github, pathlib, arguments

ARGUMENTS = [
    arguments.PATH,
    arguments.MAJOR,
    arguments.MINOR,
    arguments.PATCH,
    arguments.FORMAT,
    arguments.SCHEMA,
    arguments.VERSION,
    arguments.HASH,
    arguments.DATE,
    arguments.TIME,
    arguments.KEYWORD,
    arguments.AUTHOR,
    arguments.SUBJECT
]

def execute(**kwargs):

    path_repository = pathlib.Path(kwargs['path']).absolute().as_posix()

    client = github.Client(path_repository)

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])

    if commits is None: return

    commits.reverse()

    filter = {key: value for key, value in kwargs.items() if key in ['version', 'hash', 'date', 'time', 'keyword', 'author', 'subject']}

    for commit in commits:

        if commit.match(filter):

            print(commit.show_as(kwargs['format'], kwargs['schema']))


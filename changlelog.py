import github, markdown

ARGUMENTS = [
    ['--path',      {'type': str,   'default': '.',             'help': 'Path to git repository (default: current directory)'}],
    ['--major',     {'type': str,   'default': 'break',         'help': 'Major version keyword (default: break)'}],
    ['--minor',     {'type': str,   'default': 'feat',          'help': 'Minor version keyword (default: feat)'}],
    ['--patch',     {'type': str,   'default': 'fix',           'help': 'Patch version keyword (default: fix)'}],
    ['--reverse',   {'type': bool,  'default': True,            'help': 'Reverse order of commits (default: False)'}],
    ['--output',    {'type': str,   'default': 'CHANGELOG.md',  'help': 'Output file (default: CHANGELOG.md)'}]
]

def execute(**kwargs):

    client = github.Github(kwargs['path'])

    url = client.url()

    commits = client.commits()

    if commits is None: return

    versions = client.versions(commits, kwargs['major'], kwargs['minor'], kwargs['patch'])

    if kwargs['reverse']:
        versions.reverse()
        commits.reverse()

    md = markdown.Markdown()

    last_version = None

    for index, commit in enumerate(commits):

        if last_version != versions[index]:
            link_tree = url + '/tree/' + commit.hash
            md.h2(f'**[{versions[index]}]({link_tree})**')
            md.line()


        link_commit = url + '/commit/' + commit.hash
        md.item(f'**[{commit.date}]** [[{commit.hash}]({link_commit})] ({commit.keyword}) - {commit.subject} ({commit.author})')

        if commit.body != '':
            md.text('')
            md.text('&nbsp;')
            for element in commit.body.split('\n'):
                md.text('')
                md.text(f'&emsp;&emsp;&emsp;{element}')
                md.text('')
            md.text('&nbsp;')

        last_version = versions[index]


    if kwargs['output'] == None:
        print(md.string)
        return

    with open(kwargs['output'], 'w') as file:
        file.write(md.string)


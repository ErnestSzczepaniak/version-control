import github, markdown, datetime

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

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])

    if commits is None: return

    if kwargs['reverse']:
        commits.reverse()

    md = markdown.Markdown()

    md.h1('Quick access')

    md.text('Current version:')
    md.item(f'**{commits[0].version}**')

    md.text('')
    md.text('Contributors:')

    contributors = []

    for commit in commits:
        if commit.author not in contributors:
            contributors.append(commit.author)

    for contributor in contributors:
        md.item(f'**{contributor}**')

    md.text('')
    md.text('Project timeframe:')

    date_start = commits[-1].date
    date_end = commits[0].date

    md.item(f'**{date_start} - {date_end}**')

    md.text('')
    md.text('Commit frequency:')

    period = datetime.datetime.strptime(date_end, '%d.%m.%Y') - datetime.datetime.strptime(date_start, '%d.%m.%Y')
    period = period.days + 1

    md.item(f'**{len(commits)}** commits over **{period}** days (**{round(len(commits) / period, 2)}** commits per day)')

    md.text('')
    md.text('Commit structure:')

    occurences = {}

    for commit in commits:
        if commit.keyword not in occurences:
            occurences[commit.keyword] = 0
        occurences[commit.keyword] += 1

    occurences = {k: v for k, v in sorted(occurences.items(), key=lambda item: item[1], reverse=True)}

    for keyword in occurences:
        md.item(f'**{keyword}** - {occurences[keyword]}')

    md.text('')
    md.text('Current version history:')

    for commit in commits:
        version = commit.version
        link = commit.version.replace('.', '')
        md.item(f'**[{version}](#{link})**')

    md.h1('Changelog')

    last_version = None

    for commit in commits:

        if last_version != commit.version:

            link_tree = url + '/tree/' + commit.hash

            md.h2(f'**[{commit.version}]({link_tree})**')

        link_commit = url + '/commit/' + commit.hash

        md.item(f'**[{commit.date}]** [[{commit.hash}]({link_commit})] ({commit.keyword}) - {commit.subject} (**{commit.author}** @ {commit.time})')

        if len(commit.body) > 1:
            md.text('')
            md.text('   ```')
            for element in commit.body[:-1]:
                md.text(f'   {element}')
            md.text('   ```')
            md.text('')

        last_version = commit.version


    if kwargs['output'] == None:
        print(md.string)
        return

    with open(kwargs['output'], 'w') as file:
        file.write(md.string)


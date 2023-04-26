import github, markdown, datetime, commit
from typing import List
from branch import Branch

ARGUMENTS = [
    ['--path',      {'type': str,   'default': '.',             'help': 'Path to git repository (default: current directory)'}],
    ['--major',     {'type': str,   'default': 'break',         'help': 'Major version keyword (default: break)'}],
    ['--minor',     {'type': str,   'default': 'feat',          'help': 'Minor version keyword (default: feat)'}],
    ['--patch',     {'type': str,   'default': 'fix',           'help': 'Patch version keyword (default: fix)'}],
    ['--reverse',   {'type': bool,  'default': True,            'help': 'Reverse order of commits (default: False)'}],
    ['--output',    {'type': str,   'default': 'CHANGELOG.md',  'help': 'Output file (default: CHANGELOG.md)'}]
]

def add_remote_address(md: markdown.Markdown, remote_address: str):
    md.text('Remote address:')
    md.item(f'**{remote_address}**')
    md.text('')

def add_branch_list(md: markdown.Markdown, branches: List[Branch]):
    md.text('Branches:')
    for branch in branches:
        if branch.active:
            md.item(f'**{branch.name} [current]** (**{branch.commits}** commits)')
        else:
            md.item(f'{branch.name} (**{branch.commits}** commits)')
    md.text('')


def add_current_version(md: markdown.Markdown, commits: List[commit.Commit]):
    md.text('Current version:')
    md.item(f'**{commits[0].version}**')
    md.text('')

def add_contributors(md: markdown.Markdown, commits: List[commit.Commit]):
    md.text('Contributors:')
    contributors = []
    for commit in commits:
        if commit.author not in contributors:
            contributors.append(commit.author)
    for contributor in contributors:
        md.item(f'**{contributor}**')
    md.text('')

def add_project_timeframe(md: markdown.Markdown, commits: List[commit.Commit]):
    md.text('Project timeframe:')
    date_start = commits[-1].date
    date_end = commits[0].date
    period = datetime.datetime.strptime(date_end, '%d.%m.%Y') - datetime.datetime.strptime(date_start, '%d.%m.%Y')
    days = period.days + 1
    md.item(f'**{date_start} - {date_end}** ({days} days)')
    md.text('')

def add_code_frequency(md: markdown.Markdown, commits: List[commit.Commit], difference):
    md.text('Code frequency:')
    date_start = commits[-1].date
    date_end = commits[0].date
    period = datetime.datetime.strptime(date_end, '%d.%m.%Y') - datetime.datetime.strptime(date_start, '%d.%m.%Y')
    period = period.days + 1
    md.item(f'**{len(commits)}** commits (**{round(len(commits) / period, 2)}** / day)')
    md.item(f'**{difference.files_changed}** files changed (**{round(difference.files_changed / period, 2)}** / day)')
    md.item(f'**{difference.insertions}** insertions (**{round(difference.insertions / period, 2)}** / day)')
    md.item(f'**{difference.deletions}** deletions (**{round(difference.deletions / period, 2)}** / day)')
    md.text('')

def add_commit_structure(md: markdown.Markdown, commits: List[commit.Commit]):
    md.text('Commit structure:')
    occurences = {}
    for commit in commits:
        if commit.keyword not in occurences:
            occurences[commit.keyword] = 0
        occurences[commit.keyword] += 1
    occurences = {k: v for k, v in sorted(occurences.items(), key=lambda item: item[1], reverse=True)}
    for keyword in occurences:
        percentage = round(occurences[keyword] / len(commits) * 100, 2)
        md.item(f'**{keyword}** - {occurences[keyword]} ({percentage}%)')
    md.text('')

def add_version_history(md: markdown.Markdown, commits: List[commit.Commit]):
    md.text('Version history:')
    for commit in commits:
        link = commit.version.replace('.', '')
        md.item(f'[**{commit.version}**](#{link})')
    md.text('')

def execute(**kwargs):

    client = github.Github(kwargs['path'])

    url = client.url()

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])

    if commits is None: return

    branches = client.branches()
    difference = client.difference(commits[-1], commits[0])

    if kwargs['reverse']:
        commits.reverse()

    md = markdown.Markdown()

    md.h1('Quick access')

    add_remote_address(md, url)
    add_branch_list(md, branches)
    add_current_version(md, commits)
    add_contributors(md, commits)
    add_project_timeframe(md, commits)
    add_code_frequency(md, commits, difference)
    add_commit_structure(md, commits)
    add_version_history(md, commits)

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


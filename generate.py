import github, mark, datetime, pathlib, arguments
from typing import List
from github import Commit, Branch

ARGUMENTS = [
    arguments.PATH,
    arguments.MAJOR,
    arguments.MINOR,
    arguments.PATCH,
    arguments.OUTPUT
]

def add_remote_address(md: mark.Markdown, url: github.Url):
    md.h4('Remote address:')
    md.item(f'https://github.com/{url.username}/{url.repository}')
    md.text('')

def add_connection_protocol(md: mark.Markdown, url: github.Url):
    md.h4('Connection protocol:')
    md.item(f'{url.protocol}')
    md.text('')

def add_branch_list(md: mark.Markdown, branches: List[Branch]):
    md.h4('Branches:')
    for branch in branches:
        if branch.active:
            md.item(f'{branch.name} [current] ({branch.commits} commits)')
        else:
            md.item(f'{branch.name} ({branch.commits} commits)')
    md.text('')


def add_current_version(md: mark.Markdown, commits: List[Commit]):
    md.h4('Current version:')
    md.item(f'{commits[0].version}')
    md.text('')

def add_contributors(md: mark.Markdown, commits: List[Commit]):
    md.h4('Contributors:')
    contributors = {}
    for commit in commits:
        if commit.author not in contributors:
            contributors[commit.author] = commit.email

    for contributor in contributors:
        md.item(f'{contributor} ({contributors[contributor]})')

    md.text('')

def add_project_timeframe(md: mark.Markdown, commits: List[Commit]):
    md.h4('Project timeframe:')
    date_start = commits[-1].date
    date_end = commits[0].date
    period = datetime.datetime.strptime(date_end, '%d.%m.%Y') - datetime.datetime.strptime(date_start, '%d.%m.%Y')
    days = period.days + 1
    md.item(f'{date_start} - {date_end} ({days} days)')
    md.text('')

def add_code_frequency(md: mark.Markdown, commits: List[Commit]):
    md.h4('Code frequency:')
    date_start = commits[-1].date
    date_end = commits[0].date
    period = datetime.datetime.strptime(date_end, '%d.%m.%Y') - datetime.datetime.strptime(date_start, '%d.%m.%Y')
    period = period.days + 1
    md.item(f'{len(commits)} commits ({round(len(commits) / period, 2)} / day)')

    total_files_changed = 0
    total_insertions = 0
    total_deletions = 0

    for commit in commits:
        total_files_changed += len(commit.changes)
        total_insertions += sum(change.insertions for change in commit.changes)
        total_deletions += sum(change.deletions for change in commit.changes)

    md.item(f'{total_files_changed} files changed ({round(total_files_changed / period, 2)} / day)')
    md.item(f'{total_insertions} insertions ({round(total_insertions / period, 2)} / day)')
    md.item(f'{total_deletions} deletions ({round(total_deletions / period, 2)} / day)')
    md.text('')

def add_commit_structure(md: mark.Markdown, commits: List[Commit]):
    md.h4('Commit structure:')
    occurences = {}
    for commit in commits:
        if commit.keyword not in occurences:
            occurences[commit.keyword] = 0
        occurences[commit.keyword] += 1
    occurences = {k: v for k, v in sorted(occurences.items(), key=lambda item: item[1], reverse=True)}
    for keyword in occurences:
        percentage = round(occurences[keyword] / len(commits) * 100, 2)
        md.item(f'{keyword} - {occurences[keyword]} ({percentage}%)')
    md.text('')

def add_version_oldest(md: mark.Markdown, commits: List[Commit]):
    md.h4('Oldest version:')
    link = commits[-1].version.replace('.', '')
    md.item(f'[{commits[-1].version}](#{link})')
    md.text('')

def add_version_newest(md: mark.Markdown, commits: List[Commit]):
    md.h4('Newest version:')
    link = commits[0].version.replace('.', '')
    md.item(f'[{commits[0].version}](#{link})')
    md.text('')

def add_version_table(md: mark.Markdown, commits: List[Commit]):
    md.h4('Version table based on new features:')
    groups = {}

    for commit in commits:
        version = commit.version
        major, minor = version.split('.')[:2]
        header = f'{major}.{minor}'
        if header not in groups:
            groups[header] = []
        groups[header].append(commit)

    max_items = max(len(groups[key]) for key in groups)

    table_rows = '| Feature | Fixes | ' + '| ' * (max_items - 2 ) + '|'

    cendating_rows = '| -: ' + '| :-: ' * max_items + '|'

    md.text(table_rows)
    md.text(cendating_rows)

    for key in groups:
        row = f'| {groups[key][-1].subject} | '
        for commit in groups[key]:
            link = commit.version.replace('.', '')
            row += f' [{commit.version}](#{link}) |'
        md.text(row)

def execute(**kwargs):

    path_repository = pathlib.Path(kwargs['path']).absolute().as_posix()

    client = github.Client(path_repository)

    url = client.url()

    commits = client.commits(kwargs['major'], kwargs['minor'], kwargs['patch'])

    if commits is None: return
    
    commits.reverse()

    branches = client.branches()

    md = mark.Markdown()

    md.h1(f'{url.repository}-v{commits[0].version} (by {url.username})')
    md.text('')

    md.text('This document was automatically generated by **version-control** software tool, created by Ernest Szczepaniak @ CODWAY, 2023.')

    md.h1('Table of contents')
    md.text('')

    md.item('[Overview](#overview)')
    md.text('  * [Remote address](#remote-address)')
    md.text('  * [Connection protocol](#connection-protocol)')
    md.text('  * [Branches](#branches)')
    md.text('  * [Current version](#current-version)')
    md.text('  * [Contributors](#contributors)')

    md.item('[Statistics](#statistics)')
    md.text('  * [Project timeframe](#project-timeframe)')
    md.text('  * [Code frequency](#code-frequency)')
    md.text('  * [Commit structure](#commit-structure)')

    md.item('[Version history](#version-history)')
    md.text('  * [Newest version](#newest-version)')
    md.text('  * [Oldest version](#oldest-version)')
    md.text('  * [Version table](#version-table)')
    
    md.item('[Changelog](#changelog)')

    md.h1('Overview')
    md.text('')

    add_remote_address(md, url)
    add_connection_protocol(md, url)
    add_branch_list(md, branches)
    add_current_version(md, commits)
    add_contributors(md, commits)

    md.h1('Statistics')
    md.text('')

    add_project_timeframe(md, commits)
    add_code_frequency(md, commits)
    add_commit_structure(md, commits)

    md.h1('Version history')
    md.text('')

    add_version_newest(md, commits)
    add_version_oldest(md, commits)
    add_version_table(md, commits)

    md.h1('Changelog')
    md.text('')

    last_version = None

    for commit in commits:

        if last_version != commit.version:

            link_tree = f'https://github.com/{url.username}/{url.repository}/tree/{commit.hash}'

            md.h2(f'[{commit.version}]({link_tree})')

        link_commit = f'https://github.com/{url.username}/{url.repository}/commit/{commit.hash[0:7]}'
        link_parent = f'https://github.com/{url.username}/{url.repository}/commit/{commit.parent[0:7]}'

        md.item(f'[{commit.date}] [[{commit.parent[0:7]}]({link_parent}) -> [{commit.hash[0:7]}]({link_commit})] ({commit.keyword}) - {commit.subject} ({commit.author} @ {commit.time})')

        if len(commit.body) > 1:
            md.text('')
            md.text('   ```')
            for element in commit.body[:-1]:
                md.text(f'   {element}')
            md.text('   ```')
            md.text('')

        files_changed = len(commit.changes)
        insertions = sum(change.insertions for change in commit.changes)
        deletions = sum(change.deletions for change in commit.changes)

        md.text('')
        md.text(f'   {files_changed} files changed ({insertions} insertions, {deletions} deletions):')
        md.text('')

        for change in commit.changes:
            md.text(f'   * `{change.filename} [+{change.insertions}, -{change.deletions}]`')

        md.text('')
        md.text('&nbsp;')

        last_version = commit.version

    if kwargs['output'] == None:
        print(md.string)
        return

    with open(kwargs['output'], 'w') as file:
        file.write(md.string)


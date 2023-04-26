import subprocess, pathlib
from typing import List
from commit import Commit
from branch import Branch
from difference import Difference

COMMANDS = {
    'branches':     'git -C {path} branch',
    'commits':      'git -C {path} rev-list --count {branch}',
    'difference':   'git -C {path} diff {commit_start} {commit_stop} --stat',
    'url':          'git -C {path} remote get-url origin',
    'log':          "git -C {path} log --pretty=format:'%h | %ad | %an | %s $ %b' --date=format:'%d.%m.%Y, %H:%M:%S'"
}

class Github():
    def __init__(self, path: str):
        self.path = pathlib.Path(path).absolute()

    def command_execute(self, command: str, **kwargs) -> List[str]:
        syntax = COMMANDS[command].format(path=self.path, **kwargs)
        output = subprocess.check_output(syntax, shell=True).decode()
        if output == '': return []
        return output.split('\n')

    def branches(self):
        lines = self.command_execute('branches')[:-1]
        branches = [Branch(line) for line in lines]

        for branch in branches:
            branch.commits = int(self.command_execute('commits', branch=branch.name)[0])

        return branches

    def difference(self, commit_start, commit_stop):
        lines = self.command_execute('difference', commit_start=commit_start.hash, commit_stop=commit_stop.hash)
        if lines == []: return None
        return Difference(lines[-2])

    def url(self):
        response = self.command_execute('url')[0]
        response = response[response.find(':')+1:-4]
        return f'https://github.com/{response}'

    def commits(self,  major: str = 'break', minor: str = 'feat', patch: str = 'fix'):
        lines = self.command_execute('log')
        if lines == []: return None

        items = {}
        current = ''

        for line in lines:
            if '|' in line:
                h, b = line.split(' $ ')
                items[h] = [b]
                current = h
            else:
                items[current].append(line)

        items = dict(reversed(items.items()))

        keywords = []

        for item in items:
            subject = item.split(' | ')[-1]
            keyword = subject.split(': ')[0]
            keywords.append(keyword)

        versions = self.versions(keywords, major, minor, patch)

        return [Commit(version, header, body) for version, (header, body) in zip(versions, items.items())]

    def versions(self, keywords: List[str], major: str = 'break', minor: str = 'feat', patch: str = 'fix'):
        version = [0, 0, 0]
        result = []
        for keyword in keywords:
            if keyword == patch:
                version[2] += 1
            elif keyword == minor:
                version[1] += 1
                version[2] = 0
            elif keyword == major:
                version[0] += 1
                version[1] = 0
                version[2] = 0
            result.append('.'.join([str(number) for number in version]))

        occurences = {}

        for version in result:
            if version not in occurences:
                occurences[version] = 0
            occurences[version] += 1

        versions = []

        for entry in occurences:
            if occurences[entry] == 1:
                versions.append(entry)
            else:
                for i in range(occurences[entry]):
                    versions.append(f'{entry}-rev.{i+1}')

        return versions
    
'0.5.0.rev.1'
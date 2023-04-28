import subprocess, pathlib, re
from typing import List
from commit import Commit
from branch import Branch

COMMANDS = {
    'branches':     'git -C {path} branch',
    'commits':      'git -C {path} rev-list --count {branch}',
    'show':         'git -C {path} show {hash} --numstat',
    'url':          'git -C {path} remote get-url origin',
    'log':          "git -C {path} log --pretty=format:'%h | %ad | %an | %s | %b $' --date=format:'%d.%m.%Y %H:%M:%S'"
}

PATTERN_LOG = re.compile(
    r'(?P<hash>[0-9a-f]{7}) \| '
    r'(?P<date>\d{2}\.\d{2}\.\d{4}) (?P<time>\d{2}:\d{2}:\d{2}) \| '
    r'(?P<author>.+) \| '
    r'(?P<keyword>\w+): (?P<subject>.+) \| '
    r'(?P<body>.*)', re.DOTALL
)

PATTERN_SHOW = re.compile(
    r'(?P<insertions>\d+)\t(?P<deletions>\d+)\t(?P<filename>.*)'
)

class Github():
    def __init__(self, path: str):
        self.path = pathlib.Path(path).absolute()

    def command_execute(self, command: str, split='\n', reverse=False, **kwargs) -> List[str]:
        syntax = COMMANDS[command].format(path=self.path, **kwargs)
        output = subprocess.check_output(syntax, shell=True).decode()
        if output == '': return []
        output = output.split(split)
        if reverse: output.reverse()
        return output

    def branches(self):
        lines = self.command_execute('branches')[:-1]
        branches = [Branch(line) for line in lines]

        for branch in branches:
            branch.commits = int(self.command_execute('commits', branch=branch.name)[0])

        return branches

    def url(self):
        response = self.command_execute('url')[0]
        response = response[response.find(':')+1:-4]
        return f'https://github.com/{response}'

    def create_commits(self):

        lines = self.command_execute('log', split='$', reverse=True)[:-1]

        commits = []

        for line in lines:
            
            if len(line) == 0: continue
            if line[0] == '\n': line = line[1:]
            
            match = PATTERN_LOG.match(line)
            if match is None: continue

            candidate = match.groupdict()

            if '\n' in candidate['body']:
                candidate['body'] = candidate['body'].split('\n')

            commit = Commit(**candidate)

            commits.append(commit)

        return commits

    def commits(self,  major: str = 'break', minor: str = 'feat', patch: str = 'fix'):

        commits = self.create_commits()

        self.add_versions(commits, major, minor, patch)
        self.add_modyfications(commits)

        return commits

    def add_modyfications(self, commits: List[Commit]):

        for commit in commits:

            lines = self.command_execute('show', hash=commit.hash)

            matches = PATTERN_SHOW.findall('\n'.join(lines))

            for match in matches:

                commit.files_changed.append(match[2])
                commit.insertions.append(int(match[0]))
                commit.total_insertions += int(match[0])
                commit.deletions.append(int(match[1]))
                commit.total_deletions += int(match[1])

            commit.total_files_changed = len(commit.files_changed)

    def add_versions(self, commits: List[Commit], major: str = 'break', minor: str = 'feat', patch: str = 'fix'):
        version = [0, 0, 0]
        result = []
        for commit in commits:
            if commit.keyword == patch:
                version[2] += 1
            elif commit.keyword == minor:
                version[1] += 1
                version[2] = 0
            elif commit.keyword == major:
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

        for commit, version in zip(commits, versions):
            commit.version = version
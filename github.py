import subprocess, re, json
from typing import List
from colorama import Fore
from dataclasses import dataclass, field

# /* ---------------------------------------------| datatypes |--------------------------------------------- */

FORMAT_TABLE = {
    'version': Fore.YELLOW + '{:<13}' + Fore.RESET,
    'hash': '{:<7}',
    'date': '{:<10}',
    'time': '{:<8}',
    'keyword': '{:<8}',
    'author': '{:<25}',
    'subject': '{:<50}'
}

@dataclass
class Change():
    filename: str = ''
    insertions: int = 0
    deletions: int = 0

@dataclass
class Commit():
    version: str = ''
    hash: str = ''
    parent: str = ''
    date: str = ''
    time: str = ''
    author: str = ''
    email: str = ''
    keyword: str = ''
    subject: str = ''
    body: List[str] = field(default_factory=lambda : [])
    changes: List[Change] = field(default_factory=lambda : [])

    def show_as(self, format: str, schema: List[str]):
        if format == 'table':
            return '  '.join(FORMAT_TABLE[key].format(getattr(self, key)) for key in schema)
        elif format == 'csv':
            return ', '.join([getattr(self, key) for key in schema])
        elif format == 'json':
            return json.dumps({key: getattr(self, key) for key in schema}, indent=4)
        else:
            raise ValueError(f"Format '{format}' is not supported")

    def match(self, filter):
        for key, value in filter.items():
            if value == '*': continue
            elif '*' in value:
                position = value.index('*')
                if value[:position] not in getattr(self, key): return False
                if value[position + 1:] not in getattr(self, key): return False
            elif getattr(self, key) != value:
                return False
        return True

@dataclass
class Branch():
    name: str = ''
    active: bool = False
    commits: int = 0

@dataclass
class Url():
    protocol: str = ''
    domain: str = ''
    username: str = ''
    repository: str = ''

# /* ---------------------------------------------| api |--------------------------------------------- */

class Api():
    def __init__(self, path: str):
        self.path = path

    def execute(self, syntax: str, split='\n', reverse=False) -> List[str]:
        output = subprocess.check_output(syntax, shell=True).decode()
        if output == '': return []
        output = output.split(split)
        if reverse: output.reverse()
        return output

    def branch(self):
        return self.execute(f'git -C {self.path} branch')[:-1]
    
    def rev_list(self, branch: str):
        return self.execute(f'git -C {self.path} rev-list --count {branch}')
    
    def remote_url(self):
        return self.execute(f'git -C {self.path} remote get-url origin')[0]
    
    def log(self):
        return self.execute(f"git -C {self.path} log --pretty=format:\"%H | %P | %ad | %an | %ae | %s | %b $\" --date=format:\"%d.%m.%Y %H:%M:%S\"", split='$', reverse=True)[1:]
    
    def show(self, hash: str):
        return self.execute(f'git -C {self.path} show {hash} --numstat')

# /* ---------------------------------------------| client |--------------------------------------------- */

PATTERN_LOG = re.compile(
    r'(?P<hash>[0-9a-f]{40}) \| '
    r'(?P<parent>[0-9a-f]{40}) \| '
    r'(?P<date>\d{2}\.\d{2}\.\d{4}) (?P<time>\d{2}:\d{2}:\d{2}) \| '
    r'(?P<author>.+) \| '
    r'(?P<email>.+) \| '
    r'(?P<keyword>\w+): (?P<subject>.+) \| '
    r'(?P<body>.*)', re.DOTALL
)

PATTERN_SHOW = re.compile(
    r'(?P<insertions>\d+)\t(?P<deletions>\d+)\t(?P<filename>.*)'
)

PATTERN_BRANCHES = re.compile(
    r'(?P<active>\*)? (?P<name>.+)'
)

PATTERN_REMOTE_URL_HTTPS = re.compile(
    r'https:\/\/github.com\/(?P<username>.+)\/(?P<repository>.+)(\.git)'
)

PATTERN_REMOTE_URL_SSH = re.compile(
    r'git@github.com:(?P<username>.+)\/(?P<repository>.+)(\.git)'
)

class Client(Api):
    def __init__(self, path: str):
        self.api = Api(path)

    def branches(self):

        response = self.api.branch()

        branches = []

        matches = PATTERN_BRANCHES.findall('\n'.join(response))

        for match in matches:

            branch = Branch(active=match[0] == '*', name=match[1])
            branches.append(branch)

        for branch in branches:
            branch.commits = int(self.api.rev_list(branch.name)[0])

        return branches

    def url(self) -> Url:

        response = self.api.remote_url()

        candidate = {'domain': 'github.com'}

        if match := PATTERN_REMOTE_URL_HTTPS.match(response):
            candidate = match.groupdict()
            candidate['protocol'] = 'https'
        elif match := PATTERN_REMOTE_URL_SSH.match(response):
            candidate = match.groupdict()
            candidate['protocol'] = 'ssh'

        if match is None: return Url()

        return Url(**candidate)


    def create_commits(self):

        lines = self.api.log()

        commits = []

        for line in lines:
            
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
        self.add_changes(commits)

        return commits

    def add_changes(self, commits: List[Commit]):

        for commit in commits:

            lines = self.api.show(commit.hash)

            matches = PATTERN_SHOW.findall('\n'.join(lines))

            for match in matches:

                change = Change(filename=match[2], insertions=int(match[0]), deletions=int(match[1]))

                commit.changes.append(change)


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
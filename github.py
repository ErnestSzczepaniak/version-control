import subprocess, pathlib
from typing import List
from commit import Commit
from branch import Branch

class Github():
    def __init__(self, path: str):
        self.path = pathlib.Path(path).absolute()

    def command_execute(self, command) -> List[str]:
        output = subprocess.check_output(command, shell=True).decode()
        if output == '': return []
        output = output.split('\n')
        return output

    def branches(self):
        syntax = f"git -C {self.path} branch"
        lines = self.command_execute(syntax)[:-1]
        return [Branch(line) for line in lines]
        

    def url(self):
        syntax = f"git -C {self.path} remote get-url origin"
        response = self.command_execute(syntax)[0]
        response = response[response.find(':')+1:-4]
        return f'https://github.com/{response}'

    def commits(self,  major: str = 'break', minor: str = 'feat', patch: str = 'fix'):
        syntax = f"git -C {self.path} log --pretty=format:'%h | %ad | %an | %s $ %b' --date=format:'%d.%m.%Y, %H:%M:%S'"
        lines = self.command_execute(syntax)
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

        commits = [Commit(header, body, version) for (header, body), version in zip(items.items(), versions)]

        for index, commit in enumerate(commits):
            commit.version = versions[index]

        return commits

    def versions(self, keywords: List[str], major: str = 'break', minor: str = 'feat', patch: str = 'fix'):
        version = [0, 0, 0]
        result = []
        for keyword in keywords:
            if keyword == patch:
                version[2] += 1
                result.append('.'.join([str(number) for number in version]))
            elif keyword == minor:
                version[1] += 1
                version[2] = 0
                result.append('.'.join([str(number) for number in version]))
            elif keyword == major:
                version[0] += 1
                version[1] = 0
                version[2] = 0
                result.append('.'.join([str(number) for number in version]))
            else:
                result.append('.'.join([str(number) for number in version]))
        return result
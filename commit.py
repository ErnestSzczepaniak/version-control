from typing import List
from colorama import Fore
import json

FORMAT_TABLE = {
    'version': Fore.YELLOW + '{:<11}' + Fore.RESET,
    'hash': '{:<7}',
    'date': '{:<10}',
    'time': '{:<8}',
    'keyword': '{:<8}',
    'author': '{:<25}',
    'subject': '{:<50}'
}

class Commit():
    def __init__(self, version: str, header: str, body: List[str]):
        self.version = version
        hash, datetime, author, subject = header.split(' | ')
        self.body = body
        self.hash = hash
        self.date, self.time = datetime.split(', ')
        self.author = author
        self.keyword, self.subject = subject.split(': ')

    def format_as(self, format: str, schema: List[str]):
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
            if getattr(self, key) != value:
                return False
        return True
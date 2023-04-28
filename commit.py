from typing import List
from colorama import Fore
import json
from dataclasses import dataclass, field

FORMAT_TABLE = {
    'version': Fore.YELLOW + '{:<11}' + Fore.RESET,
    'hash': '{:<7}',
    'date': '{:<10}',
    'time': '{:<8}',
    'keyword': '{:<8}',
    'author': '{:<25}',
    'subject': '{:<50}'
}

@dataclass
class Commit():
    version: str = ''
    hash: str = ''
    date: str = ''
    time: str = ''
    author: str = ''
    keyword: str = ''
    subject: str = ''
    body: List[str] = field(default_factory=lambda : [])
    files_changed: List[str] = field(default_factory=lambda : [])
    total_files_changed: int = 0
    insertions: List[int] = field(default_factory=lambda : [])
    total_insertions: int = 0
    deletions: List[int] = field(default_factory=lambda : [])
    total_deletions: int = 0

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
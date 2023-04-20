from typing import List
from colorama import Fore

class Commit():
    def __init__(self, header, body):
        hash, datetime, author, subject = header.split(' | ')
        self.hash = hash
        self.date = datetime.split(', ')[0]
        self.time = datetime.split(', ')[1]
        self.author = author
        self.keyword = subject.split(': ')[0]
        self.subject = subject.split(': ')[1]
        self.body = body
        self.version = ''

    def format_as_table(self, schema: List[str]):
        formated = {}

        formated['version'] = Fore.YELLOW + '{:<8}'.format(self.version) + Fore.RESET
        formated['hash'] = '{:<7}'.format(self.hash)
        formated['date'] = '{:<10}'.format(self.date)
        formated['time'] = '{:<8}'.format(self.time)
        formated['keyword'] = '{:<8}'.format(self.keyword)

        max_length = 50

        if len(self.subject) > max_length:
            self.subject = self.subject[:max_length - 6] + ' (...)'

        formated['subject'] = '{:<{}}'.format(self.subject, max_length)

        # if len(self.body) > max_length:
        #     self.body = self.body[:max_length - 6] + ' (...)'

        # formated['body'] = '{:<{}}'.format(self.body, max_length)

        formated['author'] = '{:<25}'.format(self.author)

        return '  '.join([formated[key] for key in schema])

    def format_as_csv(self, schema: List[str]):
        return ', '.join([getattr(self, key) for key in schema])

    def format_as_json(self, schema: List[str]):
        return {key: getattr(self, key) for key in schema}

    def format_as(self, format: str, schema: List[str]):
        if format == 'table':
            return self.format_as_table(schema)
        elif format == 'csv':
            return self.format_as_csv(schema)
        elif format == 'json':
            return self.format_as_json(schema)
        else:
            raise ValueError(f"Format '{format}' is not supported")


    def match(self, filter):
        for key, value in filter.items():
            if value == '*': continue
            if getattr(self, key) != value:
                return False
        return True
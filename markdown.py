class Markdown():
    def __init__(self):
        self.string = ''

    def parse_item(self, item):
        if type(item) == Markdown:
            return item.string
        return item

    def add_line(self, line):
        self.string += line + '\n'
        return self

    def h1(self, item):
        item = self.parse_item(item)
        return self.add_line('# ' + item)

    def h2(self, item):
        item = self.parse_item(item)
        return self.add_line('## ' + item)

    def h3(self, item):
        item = self.parse_item(item)        
        return self.add_line('### ' + item)

    def item(self, item):
        item = self.parse_item(item)
        return self.add_line('* ' + item)

    def text(self, item):
        item = self.parse_item(item)
        return self.add_line(item)
    
    def code(self, item):
        item = self.parse_item(item)
        return self.add_line('```' + item + '```')
    
    def bold(self, item):
        item = self.parse_item(item)
        return self.add_line('**' + item + '**')
    
    def link(self, item, url):
        item = self.parse_item(item)
        return self.add_line(f'[{item}]({url})')
    
    def line(self):
        return self.add_line('---')
    
    def quote(self, item):
        item = self.parse_item(item)
        return self.add_line('> ' + item)
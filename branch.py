class Branch():
    def __init__(self, string):
        self.name = string[2:]
        self.active = True if '*' in string else False
        self.commits = 0
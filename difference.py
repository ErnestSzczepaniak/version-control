class Difference():
    def __init__(self, string):
        files, insertions, deletions = string[1:].split(', ')
        self.files_changed = int(files.split(' ')[0])
        self.insertions = int(insertions.split(' ')[0])
        self.deletions = int(deletions.split(' ')[0])
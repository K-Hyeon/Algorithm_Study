class Record:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __eq__(self, rhs):
        return self.word == rhs.word

    def __ne__(self, rhs):
        return self.word != rhs.word

    def __lt__(self, rhs):
        return self.word < rhs.word

    def __gt__(self, rhs):
        return self.word > rhs.word

    def __str__(self):
        return '{}:{}'.format(str(self.word), str(self.meaning))

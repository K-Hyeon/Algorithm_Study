class HNode:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.freq)

    def __eq__(self, rhs):
        return self.freq == rhs.freq

    def __ne__(self, rhs):
        return self.freq != rhs.freq

    def __lt__(self, rhs):
        return self.freq < rhs.freq

    def __le__(self, rhs):
        return self.freq <= rhs.freq

    def __gt__(self, rhs):
        return self.freq > rhs.freq

    def __ge__(self, rhs):
        return self.freq >= rhs.freq

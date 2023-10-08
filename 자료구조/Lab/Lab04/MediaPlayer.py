import time
from queueADT import *
from random import randint

class Track:
    def __init__(self, title = None):
        self.title = title
        self.length = randint(3, 10)

    def __str__(self):
        return "{} : {}".format(self.title, self.length)

class MediaPlayerQueue(CircularQueue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while not self.isEmpty():
            current_track = self.dequeue()
            print("Now playing {}".format(current_track.title))
            #random length
            time.sleep(current_track.length)
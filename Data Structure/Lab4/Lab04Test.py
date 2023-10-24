from queueADT import *
from MediaPlayer import *
from TCS import *
from Maze import *

def testCircularQueue():
    print('[ Test Queue ]')
    q = CircularQueue()
    for i in range(10):
        q.enqueue(i)
    print('enqueue() X 9: ', end='')
    q.print()
    print('  dequeue() -->', q.dequeue())
    print('  dequeue() -->', q.dequeue())
    print('  dequeue() -->', q.dequeue())
    print('dequeue() X 3: ', end='')
    q.clear()
    q.enqueue('aaa')
    q.enqueue('bbb')
    q.enqueue('ccc')
    q.enqueue('ddd')
    print('enqueue() X 4: ', end='')
    q.print()
    print('  dequeue() -->', q.dequeue())
    print('  dequeue() X 9: ', end='')
    q.print()
    print('peek() -->', q.peek())
    print('\n')

def testCircularDeue():
    print('[ Test Deqeue ]')
    q = CircularDeque()
    for i in range(10):
        q.enqueue(i)
    print('enqueue() X 9: ', end='')
    q.print()
    print('  dequeue() -->', q.deleteFront())
    print('  dequeue() -->', q.deleteFront())
    print('  dequeue() -->', q.deleteFront())
    print('dequeue() X 3: ', end='')
    q.clear()

    q.addRear('aaa')
    q.addRear('bbb')
    q.addRear('ccc')
    q.addRear('ddd')
    print('enqueue() X 4: ', end='')
    q.print()
    print('  dequeue() -->', q.deletRear())
    print('  dequeue() X 9: ', end='')
    q.print()
    print('peek() -->', q.getFront())
    print('peek() -->', q.getRear())
    print('\n')

def testMPQ():
    track1 = Track("white whistle")
    track2 = Track("butter butter")
    track3 = Track("oh black star")
    track4 = Track("watch that chicken")
    track5 = Track("Don't go")

    mp = MediaPlayerQueue()
    mp.add_track(track1)
    mp.add_track(track2)
    mp.add_track(track3)
    mp.add_track(track4)
    mp.add_track(track5)
    mp.play()

def runSimulation():
    done = TicketCounterSimulation(3, 15, 1, 5)
    done.run()

def testMaze():
    m = Maze()
    m.DFS1()
    m.DFS2()
    m.DFS3()
    m.BFS1()
    m.BFS2()


def main():
    #testCircularQueue()
    #testCircularDeue()
    #testMPQ()
    #runSimulation()
    testMaze()


if __name__ == "__main__":
    main()

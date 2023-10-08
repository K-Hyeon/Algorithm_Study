from queueADT import *
from Stack import *

class Cell:
    def __init__(self, r=0, c=0):
        self.row = r
        self.col = c

    def __str__(self):
        return '(' + str(self.row) + ',' + str(self.col) + ')'
        # return print('({},{})'.format(self.row, self.col)


class Maze:
    MAZE_SIZE = 6

    def getMap(self):
        map = [['e', '1', '1', '1', '1', '1'],
               ['0', '0', '1', '0', '0', '1'],
               ['1', '0', '0', '0', '1', '1'],
               ['1', '0', '1', '0', '1', '1'],
               ['1', '0', '1', '0', '0', '1'],
               ['1', '1', '1', '1', '0', 'X']]
        return map

    def isValidPos(self, x, y, map):
        if ((x < 0) or (y < 0) or (x >= self.MAZE_SIZE) or (y >= self.MAZE_SIZE)):
            return False
        else:
            return (map[y][x] == '0') or (map[y][x] == 'x')

    def DFS1(self):
        map = self.getMap()
        deq = CircularDeque()
        deq.addFront(Cell(0,0))
        print("\nDFS1: using Deque Data Structure:")
        while not deq.isEmpty():
            here = deq.deleteFront()
            print(here, end='->')
            x = here.row
            y = here.col

            if map[y][x] == 'X':
                return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map): deq.addFront(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.addFront(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.addFront(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.addFront(Cell(x, y + 1))

        return False

    def DFS2(self):
        map = self.getMap()
        deq = Stack()
        deq.push(Cell(0,0))
        print("\n\nDFS2: using Stack Data Structure:")
        while not deq.isEmpty():
            here = deq.pop()
            print(here, end='->')
            x = here.row
            y = here.col

            if map[y][x] == 'X':
                return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map): deq.push(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.push(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.push(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.push(Cell(x, y + 1))

        return False

    def DFS3(self):
        map = self.getMap()
        deq = CircularDeque()
        deq.addRear(Cell(0,0))
        print("\n\nDFS3: using Deque Data Structure:")
        while not deq.isEmpty():
            here = deq.deletRear()
            print(here, end='->')
            x = here.row
            y = here.col

            if map[y][x] == 'X':
                return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x - 1, y, map): deq.addRear(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): deq.addRear(Cell(x + 1, y))
                if self.isValidPos(x, y - 1, map): deq.addRear(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): deq.addRear(Cell(x, y + 1))

        return False

    def BFS1(self):
        map = self.getMap()
        que = CircularDeque()
        que.addFront(Cell(0, 0))
        print("\n\nBFS1: using Deque Data Structure:")

        while not que.isEmpty():
            here = que.dequeue()
            print(here, end='->')
            x = here.row
            y = here.col
            if (map[y][x] == 'X'):
                return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x, y - 1, map): que.enqueue(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): que.enqueue(Cell(x, y + 1))
                if self.isValidPos(x - 1, y, map): que.enqueue(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): que.enqueue(Cell(x + 1, y))
        return False

    def BFS2(self):
        map = self.getMap()
        que = CircularQueue()
        que.enqueue(Cell(0, 0))
        print("\n\nBFS2: using Queue Data Structure:")

        while not que.isEmpty():
            here = que.dequeue()
            print(here, end='->')
            x = here.row
            y = here.col
            if (map[y][x] == 'X'):
                return True
            else:
                map[y][x] = '.'
                if self.isValidPos(x, y - 1, map): que.enqueue(Cell(x, y - 1))
                if self.isValidPos(x, y + 1, map): que.enqueue(Cell(x, y + 1))
                if self.isValidPos(x - 1, y, map): que.enqueue(Cell(x - 1, y))
                if self.isValidPos(x + 1, y, map): que.enqueue(Cell(x + 1, y))
        return False

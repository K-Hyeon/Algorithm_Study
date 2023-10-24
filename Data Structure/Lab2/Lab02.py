import random

class Matrix:
    rnb = random.Random()

    def __init__(self, rows, cols, f='r'):
        self.M = []
        if f == 'r':
            self.rMatrix(rows, cols)
        else:
            self.zMatrix(rows, cols)

    def rMatrix(self, rows, cols):
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(Matrix.rnb.randint(1, 10))

    def zMatrix(self, rows, cols):
        while len(self.M) < rows:
            self.M.append([])
            while len(self.M[-1]) < cols:
                self.M[-1].append(0)

    def mPrint(self):
        for rows in self.M:
            print([x for x in rows])
        print()

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.M])

    def __repr__(self):
        return "Matrix({},{})".format(len(self.M), len(self.M[0]))

    def __add__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA, colsA, 'z')
        for row in range(rowsA):
            for col in range(colsA):
                C.M[row][col] = self.M[row][col] + other.M[row][col]
        return C


    def __sub__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        C = Matrix(rowsA, colsA, 'z')
        for row in range(rowsA):
            for col in range(colsA):
                C.M[row][col] = self.M[row][col] - other.M[row][col]
        return C

    def __mul__(self, other):
        rowsA = len(self.M)
        colsA = len(self.M[0])
        rowsB = len(other.M)
        colsB = len(other.M[0])

        # Verify that two matrices can be multiplied
        if colsA != rowsB:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        C = Matrix(rowsA, colsB, 'z')
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    C.M[i][j] += self.M[i][k] * other.M[k][j]
        return C

    def transpose(self):
        rows = len(self.M)
        cols = len(self.M[0])
        transposed = Matrix(cols, rows, 'z')

        for i in range(rows):
            for j in range(cols):
                transposed.M[j][i] = self.M[i][j]

        return transposed



class EightQueens:
    rnb = random.Random()

    def __init__(self):
        self.bd=list(range(8))

    def runEQ(self,nos):
        found=0
        tries=0
        while found < nos:
            EightQueens.rnb.shuffle(self.bd)
            tries+=1

            if not self.has_clashes():
                found += 1
                print("Solution {}, {}, {} ".format(found, self.bd, tries))
                # reset tries
                tries = 0

    # Check if there are any clashes between queens
    # nos : number of solutions
    def has_clashes(self):
        for col in range(1, len(self.bd)):
            if self.col_clashes(col):
                return True
        return False

    # Check if a queen in a given column clashes with queens in previous columns
    def col_clashes(self, k):
        for i in range(k):
            if self.dclashes(i, self.bd[i], k, self.bd[k]):
                return True
        return False

    # Check if two queens in different columns clash diagonally
    def dclashes(self,x0,y0,x1,y1):
        d1 = abs(x0 - y0)
        d2 = abs(x1 - y1)
        return d1 == d2

class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append(-1)


    def play_ttt(self):
        win = False
        move = 0
        while not win:
            self.printBoard()

            if move%2 == 0:
                turn = 'X'
            else:
                turn = 'O'

            print("Turn for player".format(turn))

            user = self.getInput(turn)
            while self.board[user] != -1:
                print("Invalid input")
                user = self.getInput(turn)

            self.board[user] = 1 if turn == "O" else 0
            move += 1
            if move > 3:
                winner = self.check_win()
                if winner != -1:
                    print(" The winner is {}".format("X" if winner == 1 else "O"))
                    win = True

                # Make sure that all compartments are tied when filled
                if move == 9:
                    print("It's a tie!")
                    win = True


    def getInput(self, turn):
        while True:
            try:
                user = int(input("Enter a position (1-9) for player {}: ".format(turn)))
                if 1 <= user <= 9:
                    return user - 1
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def check_win(self):
        win_cord=((1,2,3),(4,5,6),(7,8,9), (1,4,7),(2,5,8),(3,6,9), (1,5,9),(3,5,9))
        for each in win_cord:
            if (self.board[each[0]-1] == self.board[each[1]-1]) and (self.board[each[1]-1] == self.board[each[2]-1]):
                return self.board[each[0]-1]
        return -1

    def printBoard(self):
        horizontal_line = "-------------"
        print(horizontal_line)
        for i in range(0, 9, 3):
            row = self.board[i:i + 3]
            row_str = " | ".join(["X" if val == 0 else "O" if val == 1 else " " for val in row])
            print("| {} |".format(row_str))
            if i < 6:
                print(horizontal_line)
        print(horizontal_line)
    def quit_game(self):
        print("Congratulations on your victory!")

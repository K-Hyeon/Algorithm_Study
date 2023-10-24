from Lab02 import Matrix, EightQueens, TicTacToe

def useMatrix():
    # Create First Matrix
    m1 = Matrix(5, 5, 'r')
    print("Matrix 1:")
    print(m1)
    m1.mPrint()


    # Create a second matrix(zero matrix)
    m2 = Matrix(5, 5, 'z')
    print("Matrix 2:")
    m2.mPrint()

    # Adding two matrices
    m_add = m1 + m2
    print("Matrix 1 + Matrix 2:")
    m_add.mPrint()

    # Subtracting two matrices
    m_sub = m1 - m2
    print("Matrix 1 - Matrix 2:")
    m_sub.mPrint()

    # multiplying two matrices
    m_mul = m1 * m2
    print("Matrix 1 * Matrix 2:")
    m_mul.mPrint()

    m_mul = m1 * m1
    print("Matrix 1 * Matrix 1:")
    m_mul.mPrint()

    # Transpose a matrix
    m_transposed = m1.transpose()
    print("Transpose of Matrix 1:")
    m_transposed.mPrint()


def useEightQueens():
    e1 = EightQueens()

    # Find 10 solutions to the Eight Queens problem
    print("Finding 10 solutions to the Eight Queens problem:")
    e1.runEQ(10)
    print()

    # Check if there are any clashes in the current board configuration
    if e1.has_clashes():
        print("Current board has clashes.")
    else:
        print("Current board has no clashes.")

    # Check if a specific column has clashes
    col_to_check = 3
    if e1.col_clashes(col_to_check):
        print("Column {} has clashes.".format(col_to_check))
    else:
        print("Column {} has no clashes.".format(col_to_check))

def useTicTacToe():
    t1 = TicTacToe()
    t1.play_ttt()
    t1.quit_game()

def main():
    #useMatrix()
    #useEightQueens()
    useTicTacToe()


if __name__ =='__main__':
    main()

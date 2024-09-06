# 0 for empty square
# sudoku = [
#     [0, 0, 0,  0, 0, 0,  0, 0, 0],
#     [0, 0, 0,  0, 0, 0,  0, 0, 0],
#     [0, 0, 0,  0, 0, 0,  0, 0, 0],

#     [0, 0, 0,  0, 0, 0,  0, 0, 0],
#     [0, 0, 6,  0, 0, 0,  0, 0, 0],
#     [0, 0, 0,  0, 0, 0,  0, 0, 0],

#     [0, 0, 0,  0, 0, 0,  0, 0, 0],
#     [0, 0, 0,  0, 0, 0,  0, 0, 0],
#     [0, 0, 0,  0, 0, 0,  0, 0, 0]
# ]

sudoku = [
    [0, 0, 2,  6, 0, 0,  0, 0, 0],
    [0, 5, 0,  0, 3, 0,  0, 0, 2],
    [0, 1, 0,  0, 7, 0,  0, 5, 0],

    [0, 0, 8,  4, 0, 0,  7, 0, 0],
    [0, 0, 0,  0, 9, 0,  0, 0, 0],
    [0, 0, 5,  0, 0, 2,  6, 0, 0],

    [0, 7, 0,  0, 5, 0,  0, 3, 0],
    [4, 0, 0,  0, 1, 0,  0, 7, 0],
    [0, 0, 0,  0, 0, 8,  4, 0, 0]
]


def print_sudoku(sudoku):
    for r in range(len(sudoku)):
        if r%3 == 0 and r != 0:
            print('- - - - - - - - - - - -')

        for c in range(len(sudoku[0])):
            if c%3 == 0 and c != 0:
                print(' | ', end='')

            if c == 8:
                print(sudoku[r][c])
            else:
                print(str(sudoku[r][c]) + ' ',end='')

# print_sudoku(sudoku)

def find_empty_square(sudoku):
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            if sudoku[row][col] == 0:
                return row, col
            
    return None, None
            

def is_valid(sudoku, digit, row, col):
    # Check row
    row_digits = sudoku[row]
    if digit in row_digits:
        return False
    
    # Check column
    col_digits = [sudoku[i][col] for i in range(9)]
    if digit in col_digits:
        return False
    
    # Check 3*3 box
    row_start = row // 3
    col_start = col // 3

    for r in range(row_start*3, row_start*3 + 3):
        for c in range(col_start*3, col_start*3 + 3):
            if sudoku[r][c] == digit:
                return False

    return True


def sudoku_solve(sudoku):
    # print(sudoku)
    row, col = find_empty_square(sudoku)

    if row is None:
        return True
    
    for digit in range(1,10):
        if is_valid(sudoku, digit, row, col):
            sudoku[row][col] = digit
            if sudoku_solve(sudoku):
                return True
            
        sudoku[row][col] = 0

    return False


print_sudoku(sudoku)
sudoku_solve(sudoku)
print('_______________________')
print_sudoku(sudoku)

import random
from copy import deepcopy


board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

magicBool = True


# Отрисовка поля
def print_board(board):
    n_board = deepcopy(board)

    for i in range(len(n_board)):
        for j in range(len(n_board[i])):
            n_board[i][j] = str(n_board[i][j])
            if n_board[i][j] == '0':
                n_board[i][j] = '    '
            else:
                length = len(n_board[i][j])
                if length == 1:
                    n_board[i][j] = n_board[i][j] + '   '
                if length == 2:
                    n_board[i][j] = n_board[i][j] + '  '
                if length == 3:
                    n_board[i][j] = n_board[i][j] + ' '

    print(n_board[0][0] + '|' + n_board[0][1] + '|' + n_board[0][2] + '|' + n_board[0][3])
    print('----' + '+' + '----' + '+' + '----' + '+' + '----')
    print(n_board[1][0] + '|' + n_board[1][1] + '|' + n_board[1][2] + '|' + n_board[1][3])
    print('----' + '+' + '----' + '+' + '----' + '+' + '----')
    print(n_board[2][0] + '|' + n_board[2][1] + '|' + n_board[2][2] + '|' + n_board[2][3])
    print('----' + '+' + '----' + '+' + '----' + '+' + '----')
    print(n_board[3][0] + '|' + n_board[3][1] + '|' + n_board[3][2] + '|' + n_board[3][3])
    print('===================')


def add_item(board):
    while True:
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        if board[a][b] == 0:
            board[a][b] = 2
            break
    return board


# Вспомогательная функция проверяющая остались ли пустые клетки на поле
def blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    return True


def compress(board):
    for _ in range(3):
        for i in range(4):
            for j in range(3):
                if board[i][-j-1] == 0:
                    board[i][-j-1] = board[i][-j-2]
                    board[i][-j-2] = 0
    return board


# Работает только в правую сторону, если перемещение происходит в другую сторону, необходимо
# предварительно повернуть поле функцией rotate.
def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][-j-1] == board[i][-j-2] and board[i][-j-1] != 0:
                board[i][-j-1] *= 2
                board[i][-j-2] = 0
    return board


# times - кол-во поворотов по часовой стрелке(1 - 90'; 2 - 180'; 3 - 270'; 4 - 360')
def rotate(board, times):
    while times > 0:
        a = list(zip(*reversed(board)))
        for i in a:
            board.append(list(i))
            del board[0]
        times -= 1
        if times == 0:
            return board
        return rotate(board, times)


def game_status(board):
    for i in range(len(board)):
        if 0 in board[i]:
            return 'norm'
        if i == 3 and 0 not in board[i]:
            return 'game over'


def magic(board):
    compress(board)
    merge(board)
    compress(board)


def right(board):
    magic(board)


def left(board):
    rotate(board, 2)
    magic(board)
    rotate(board, 2)


def up(board):
    rotate(board, 1)
    magic(board)
    rotate(board, 3)


def down(board):
    rotate(board, 3)
    magic(board)
    rotate(board, 1)


while True and game_status(board) != 'game over':

    if magicBool:
        add_item(board)
    magicBool = True
    print_board(board)
    key = input('Enter key ("r" for reset): ')

    if key == 'd':
        newBoard = deepcopy(board)
        right(board)
        if newBoard == board:
            magicBool = False
        continue

    elif key == 'a':
        newBoard = deepcopy(board)
        left(board)
        if newBoard == board:
            magicBool = False
        continue

    elif key == 'w':
        newBoard = deepcopy(board)
        up(board)
        if newBoard == board:
            magicBool = False
        continue

    elif key == 's':
        newBoard = deepcopy(board)
        down(board)
        if newBoard == board:
            magicBool = False
        continue

    elif key == 'r':
        board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        continue

    else:
        break

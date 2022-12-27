import re
import numpy as np


class Settings:
    ROWS = 6
    COLUMNS = 7
    NONE_COLOR = 0
    WHITE = 1
    BLACK = 2
    EMPTY = 42
    PLAYER = 1
    PIECES = {WHITE: 'X', BLACK: 'O', NONE_COLOR: '.'}
    BOARD = np.zeros((ROWS, COLUMNS), dtype=np.int32)


def print_board(board: np.ndarray):
    print('\n')
    print(' ' + ' '.join(['1', '2', '3', '4', '5', '6', '7']) + ' ', '---------------', sep='\n')
    for row in board:
        print(
            ('┊' + np.array2string(row, separator='┊')[1:-1] + '┊')
            .replace('0', Settings.PIECES[Settings.NONE_COLOR])
            .replace('1', Settings.PIECES[Settings.WHITE])
            .replace('2', Settings.PIECES[Settings.BLACK])
        )
    print('---------------', end='\n\n')


def check_win(board: np.ndarray, player: int):
    for x in range(4):
        for y in range(3):
            new_board = board[x:4 + x, y:4 + y]
            for row in new_board:
                if (row == player).all():
                    return True
            for row in np.transpose(new_board):
                if (row == player).all():
                    return True
            if (new_board.diagonal() == player).all() or (np.fliplr(new_board).diagonal() == player).all():
                return True


def main():
    while True:
        print_board(np.fliplr(np.flip(Settings.BOARD)))
        if Settings.EMPTY == 0:
            print('Draw')
            return
        try:
            number = input(f'Player_{Settings.PLAYER} : ')
        except KeyboardInterrupt:
            print('\nGoodBy :)')
            return
        if re.match(r'[1-7]$', number):
            Settings.BOARD = np.transpose(Settings.BOARD)
            column = int(number) - 1
            res = np.where(Settings.BOARD[column] == 0)[0]
            if res.size:
                Settings.BOARD[column][res[0]] = Settings.PLAYER
                Settings.EMPTY -= 1
                win = check_win(Settings.BOARD, Settings.PLAYER)
                if win:
                    Settings.BOARD = np.transpose(Settings.BOARD)
                    print_board(np.fliplr(np.flip(Settings.BOARD)))
                    print(f'Player {Settings.PLAYER} is winner')
                    return
                Settings.PLAYER = 2 if Settings.PLAYER == 1 else 1
            Settings.BOARD = np.transpose(Settings.BOARD)


if __name__ == '__main__':
    main()

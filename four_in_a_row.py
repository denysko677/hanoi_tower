def create_board(rows, cols):
    """
    Функція для створення гри "Чотири в ряд" з заданою кількістю рядків і стовпців.

    :param rows: Кількість рядків на дошці
    :param cols: Кількість стовпців на дошці
    :return: Початкова дошка
    """
    return [[' ' for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    """
    Функція для відображення гри "Чотири в ряд".

    :param board: Текуща дошка гри
    """
    for row in board:
        print('|'.join(row))
    print(' ' + ' '.join(str(i) for i in range(len(board[0]))))


def check_win(board, row, col, player):
    """
    Функція для перевірки, чи є переможець.

    :param board: Текуща дошка гри
    :param row: Рядок, де було зроблено останній хід
    :param col: Стовпець, де було зроблено останній хід
    :param player: Гравець, який зробив останній хід
    :return: True, якщо гравець переміг, інакше False
    """
    # Перевіряємо горизонтальну лінію
    if col + 3 < len(board[0]):
        if all(board[row][col + i] == player for i in range(4)):
            return True

    # Перевіряємо вертикальну лінію
    if row + 3 < len(board):
        if all(board[row + i][col] == player for i in range(4)):
            return True

    # Перевіряємо діагональні лінії
    if row + 3 < len(board) and col + 3 < len(board[0]):
        if all(board[row + i][col + i] == player for i in range(4)):
            return True
    if row - 3 >= 0 and col + 3 < len(board[0]):
        if all(board[row - i][col + i] == player for i in range(4)):
            return True

    return False


def is_valid_move(board, col):
    """
    Перевіряє, чи є допустимим хід вказаний стовпець.

    :param board: Текуща дошка гри
    :param col: Стовпець, в який гравець хоче зробити хід
    :return: True, якщо хід допустимий, інакше False
    """
    return ' ' in board[0][col]


def drop_piece(board, col, player):
    """
    Розміщує фігуру гравця в вказаному стовпці.

    :param board: Текуща дошка гри
    :param col: Стовпець, в який гравець хоче зробити хід
    :param player: Гравець, який робить хід ('X' або 'O')
    """
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            break


def main():
    ROWS = 6
    COLS = 7
    board = create_board(ROWS, COLS)
    player = 'X'

    while True:
        print_board(board)
        col = int(input(f"Гравець {player}, оберіть стовпець (0-{COLS - 1}): "))
        
        if is_valid_move(board, col):
            drop_piece(board, col, player)
            if check_win(board, ROWS - 1, col, player):
                print_board(board)
                print(f"Гравець {player} переміг!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Недопустимий хід. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

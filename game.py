# Объявить класс.
class Board:

    # Инициализировать игровое поле - список списков с пробелами.
    # Пробелы - это пустые клетки.
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле. 
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)



# Создать игровое поле - обЪект класса Board.
game = Board()
# Отрисовать поле в терминале.
game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
game.make_move(2, 2, 'X')
print('Ход сделан!')
# Перерисовать поле с учетом сделанного хода.
game.display()
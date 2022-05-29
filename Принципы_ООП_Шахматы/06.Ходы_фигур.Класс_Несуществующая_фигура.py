# Стас Волик. Шахматы. 6.Ходы фигур. Класс "Несуществующая (прозрачная) фигура"

class Color():
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Empty(object):
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        '''Метод возбуждает исключение при попытке получить возможные ходы
        прозрачной фигуры'''
        raise Exception("Error!")

    def __str__(self):
        return "."


class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.IMG[1 if self.color == Color.WHITE else 0]


class Pawn(ChessMan):
    IMG = ("♙", "♟")

    def get_moves(self, board, x, y):
        '''Метод возвращает возможные ходы "Пешки" в виде списка списков с координатами [[x, y]]'''
        moves = []
        if self.color == Color.BLACK and y < 7 and board.get_color(x, y+1) == Color.EMPTY:
            moves.append([x, y])
        return moves


class King(ChessMan):
    IMG = ("♔", "♚")

    def get_moves(self, board, x, y):
        '''Метод возвращает возможные ходы "Короля".
        Метод не реализован, возвращает пустой список'''
        moves = []
        return moves


class Board(object):
    def __init__(self):
        self.board = [[Empty() for i in range(8)] for j in range(8)]
        self.board[1][2] = Pawn(Color.BLACK) # черная "Пешка" на второй линии сверху в позиции 3
        self.board[0][4] = King(Color.BLACK) # черный "Король" на первой линии сверху в позиции 5
        self.board[6][2] = Pawn(Color.WHITE) # белая "Пешка" на второй линии снизу в позиции 2
        self.board[7][4] = King(Color.WHITE) # белый "Король" на первой линии снизу в позиции 5

    def get_color(self, x, y):
        '''Метод возвращает цвет фигуры, стоящей на клетке шахматной доски'''
        return self.board[y][x].color

    def get_moves(self, x, y):
        '''Метод возвращает возможные ходы фигуры, стоящей на клетке шахматной доски''' 
        return self.board[y][x].get_moves(self, x, y+1)

    def __str__(self):
        res = ""
        for y in range(8):
            res += "".join(map(str, self.board[y])) + "\n"
        return res


print(Board()) # отобразить существующие фигуры на "Шахматной доске"

print(Board().get_moves(2, 1)) # запросить возможные ходы для черной "Пешки" в позиции 2:1 по x и y соответственно
# в данном примере реализован ход пешки со стартовой позиции на 1 шаг по прямой
# OUT: [[2, 2]]

print(Board().get_moves(4, 0)) # запросить возможные ходы для черного "Короля" в позиции 2:1 по x и y соответственно
# поскольку метод для "Короля" пока ещё не реализован и возвращает пустой список, то:
# OUT: []

# print(Board().get_moves(3, 1)) # запросить возможные ходы для "Несуществующей фигуры" в позиции 3:1 по x и y соответственно
# OUT: Exception: Error!

# coding: utf-8
# Стас Волик. Шахматы. 11.Улучшенная доска

# перед запуском программы прописать кодировку терминала на utf-8
# 65001 - Кодировка UTF-8
# >>> chcp 65001

class Color():
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Empty(object):
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        '''Метод возбуждает исключение при попытке получить возможные ходы
        "прозрачной" фигуры'''
        raise Exception("Error !")

    def __str__(self):
        return "  "


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
    SPACE_COLOR_WHITE = 209
    SPACE_COLOR_BLACK = 94

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

    def move(self, xy_from, xy_to):
        '''Метод двигает фигуру, на её месте оставляет "прозрачную" фигуру''' 
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __str__(self):
        res = "  a  b  c  d  e  f  g  h \n"
        for y in range(8):
            res += "\033[0m" + str(8 - y)
            for x in range(8):
                color = self.SPACE_COLOR_BLACK if (x + y) % 2 else self.SPACE_COLOR_WHITE
                # res += "\033[48;5;%sm%s" % (color, self.board[y][x])          # формат_1
                # res += "\033[48;5;{}m{}".format(color, self.board[y][x])      # формат_2
                res += f"\033[48;5;{color}m{self.board[y][x]}"                  # формат_3
            res += "\n"
        res += "\033[0m"
        return res


b = Board()
print(b) # отобразить существующие фигуры на "Шахматной доске"

# m - это список ВСЕХ возможных ходов черной "Пешки" в позиции 2:1 по x и y соответственно
m = b.get_moves(2, 1)
# print(m) # OUT: [[2, 2]]

# m[0] - это возможный ход черной "Пешкой", в данном случае он единственный - вперед на 1 в позицию 
# print(m[0]) # OUT: [2, 2]

# сделать ход пешкой
b.move([2, 1], m[0])

print(b) # отобразить существующие фигуры на "Шахматной доске"

# Стас Волик. Шахматы. 10.Перемещение фигуры на цветной доске

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
        return " "


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

    def move(self, xy_from, xy_to):
        '''Метод двигает фигуру, на её месте оставляет "прозрачную" фигуру''' 
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __str__(self):
        colors = [0, 46] # голубые клетки
        # colors = [0, 43] # желтые клетки
        res = ""
        i = 0
        for y in range(8):
            for x in range(8):
                res += set_color(colors[i]) + str(b.board[y][x]) + ""
                i = 1 - i
            i = 1 - i
            res += set_color(colors[i]) + "\n"
        return res


def set_color(color):
    '''Функция устанавливает цвет'''
    # return "\033[%sm" % color              # формат_1
    # return "\033[{}m".format(color)        # формат_2
    return f"\033[{color}m"                  # формат_3


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

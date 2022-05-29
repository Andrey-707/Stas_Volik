# Стас Волик. Шахматы. 5.Класс "Цвет фигуры"

class Color():
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.IMG[1 if self.color == Color.WHITE else 0]


class Pawn(ChessMan):
    IMG = ("♙", "♟")


class King(ChessMan):
    IMG = ("♔", "♚")


class Board(object):
    def __init__(self):
        self.board = [["." for i in range(8)] for j in range(8)]
        self.board[1][2] = Pawn(Color.BLACK) # черная "Пешка" на второй линии сверху в позиции 3
        self.board[0][4] = King(Color.BLACK) # черный "Король" на первой линии сверху в позиции 5
        self.board[6][2] = Pawn(Color.WHITE) # белая "Пешка" на второй линии снизу в позиции 2
        self.board[7][4] = King(Color.WHITE) # белый "Король" на первой линии снизу в позиции 5

    def __str__(self):
        res = ""
        for y in range(8):
            # для приведения каждого элемента списка к строке используется map()
            res += "".join(map(str, self.board[y])) + "\n"
        return res


# на "Шахматной доске" размером 8х8 клеток размещены:
# черная "Пешка" на второй линии сверху в позиции 3;
# черный "Король" на первой линии сверху в позиции 5;
# белая "Пешка" на второй линии снизу в позиции 2;
# белый "Король" на первой линии снизу в позиции 5.
print(Board())

# Стас Волик. Шахматы. 4.Общий класс "Шахматная фигура". Класс "Король".

class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.IMG[self.color]


class Pawn(ChessMan):
    IMG = ("♙", "♟")


class King(ChessMan):
    IMG = ("♔", "♚")


class Board(object):
    def __init__(self):
        self.board = [["." for i in range(8)] for j in range(8)]
        self.board[1][2] = Pawn(0) # черная "Пешка" на второй линии сверху в позиции 3
        self.board[0][4] = King(0) # черный "Король" на первой линии сверху в позиции 5
        self.board[7][4] = King(1) # белый "Король" на первой линии снизу в позиции 5

    def __str__(self):
        res = ""
        for y in range(8):
            # для приведения каждого элемента списка к строке используется map()
            res += "".join(map(str, self.board[y])) + "\n"
        return res


# на "Шахматной доске" размером 8х8 клеток размещена черная "Пешка" на второй линии сверху в позиции 3, а также
# два "Короля", черный размещен на первой линии сверху в позиции 5, а белый - на первой линии снизу в позиции 5
print(Board())

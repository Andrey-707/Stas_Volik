# Стас Волик. Шахматы. 3.Размещение фигуры "Пешка" на "Шахматной доске".

class Pawn(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♙", "♟")[self.color]


class Board(object):
    def __init__(self):
        self.board = [["." for i in range(8)] for j in range(8)]
        self.board[1][2] = Pawn(0) # черная "Пешка" на второй линии сверху в позиции 3

    def __str__(self):
        res = ""
        for y in range(8):
            # для приведения каждого элемента списка к типу 'str' используется map()
            res += "".join(map(str, self.board[y])) + "\n"
        return res


print(Board()) # на "Шахматной доске" размером 8х8 клеток размещена черная "Пешка" на второй линии сверху в позиции 3
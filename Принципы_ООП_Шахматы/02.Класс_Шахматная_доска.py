# Стас Волик. Шахматы. 2.Класс "Шахматная доска".

class Board(object):
    def __init__(self):
        # создание методом копирования не совсем корректно (т.к. используется ссылочная модель), но
        # для наглядности того, что нужно создать подходит
        # self.board = [["."] * 8] * 8

        # для создания двумерного массива корректно использовать "list comprehensions"
        self.board = [["." for i in range(8)] for j in range(8)]
        
    def __str__(self):
        res = ""
        for y in range(8):
            res += "".join(self.board[y]) + "\n"
        return res


print(Board()) # пустая доска 8х8 клеток

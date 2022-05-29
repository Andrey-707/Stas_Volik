# Стас Волик. Шахматы. 1.Класс "Пешка".

class Pawn(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ("♙", "♟")[self.color]


print(Pawn(0)) # черная пешка
print(Pawn(1)) # белая пешка
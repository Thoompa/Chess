from Piece import Piece


class Rook(Piece):
    def __init__(self, square, colour):
        self.colour = colour
        self.square = square

        if self.colour == 'w':
            self.character = 'R'
        elif self.colour == 'b':
            self.character = 'r'
        else:
            raise NameError

    def moves(self):
        pass

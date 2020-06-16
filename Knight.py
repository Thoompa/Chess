from Piece import Piece


class Knight(Piece):
    def __init__(self, square, colour):
        self.colour = colour
        self.square = square

        if self.colour == 'w':
            self.character = 'N'
        elif self.colour == 'b':
            self.character = 'n'
        else:
            raise NameError

    def moves(self):
        pass

from Piece import Piece


class King(Piece):
    def __init__(self, square, colour):
        self.colour = colour
        self.square = square

        if self.colour == 'w':
            self.character = 'K'
        elif self.colour == 'b':
            self.character = 'k'
        else:
            raise NameError

    def moves(self):
        pass

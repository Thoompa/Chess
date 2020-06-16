from Piece import Piece


class Queen(Piece):
    def __init__(self, square, colour):
        self.colour = colour
        self.square = square

        if self.colour == 'w':
            self.character = 'Q'
        elif self.colour == 'b':
            self.character = 'q'
        else:
            raise NameError

    def moves(self):
        pass

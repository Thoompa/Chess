from Piece import Piece


class Bishop(Piece):
    def __init__(self, square, colour):
        self.colour = colour
        self.square = square

        if self.colour == 'w':
            self.character = 'B'
        elif self.colour == 'b':
            self.character = 'b'
        else:
            raise NameError

    def moves(self):
        pass

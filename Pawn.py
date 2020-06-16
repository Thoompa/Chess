from Piece import Piece


class Pawn(Piece):
    def __init__(self, square, colour):
        self.colour = colour
        self.square = square

        if self.colour == 'w':
            self.character = 'P'
        elif self.colour == 'b':
            self.character = 'p'
        else:
            raise NameError

    def moves(self):
        self.available_moves.append(self.square[0] + '3')
        if self.colour == 'w':
            if self.square[1] == '2':
                self.available_moves.append(self.square[0] + '4')

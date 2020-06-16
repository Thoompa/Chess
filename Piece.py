class Piece(object):
    character = ''
    available_moves = []
    square = ''
    colour = ''

    def moves(self):
        pass

    def __str__(self):
        return self.character

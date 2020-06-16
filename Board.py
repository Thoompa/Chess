from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from Pawn import Pawn



class Board:
    available_moves = []

    def __init__(self):
        self.board = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR']
        self.move = 'w'  # whose move is it?
        self.castling = 'KQkq'  # who can castle
        self.en_passant = '-'  # which square is en passant available on
        self.halfMove = 0  # number of half moves since last capture or pawn move
        self.fullMove = 1  # move number

        # Create piece objects
        self.board[0] = [Rook('a8', 'b'), Knight('b8', 'b'), Bishop('c8', 'b'), Queen('d8', 'b'), King('e8', 'b'),
                         Bishop('f8', 'b'), Knight('g8', 'b'), Rook('h8', 'b')]
        self.board[1] = [Pawn('a7', 'b'), Pawn('b7', 'b'), Pawn('c7', 'b'), Pawn('d7', 'b'), Pawn('e7', 'b'),
                         Pawn('f7', 'b'), Pawn('g7', 'b'), Pawn('h7', 'b')]
        self.board[7] = [Rook('a1', 'w'), Knight('b1', 'w'), Bishop('c1', 'w'), Queen('d1', 'w'), King('e1', 'w'),
                         Bishop('f1', 'w'), Knight('g1', 'w'), Rook('h1', 'w')]
        self.board[6] = [Pawn('a2', 'w'), Pawn('b2', 'w'), Pawn('c2', 'w'), Pawn('d2', 'w'), Pawn('e2', 'w'),
                         Pawn('f2', 'w'), Pawn('g2', 'w'), Pawn('h2', 'w')]

    def print(self):
        # print layout of top of board
        print('. . a b c d e f g h . .')
        print('. +-----------------+ .')
        # print board contents
        for i in range(0, 8):
            print(str(8 - i) + ' | ' + ' '.join(map(str, self.board[i])) + ' | ' + str(8 - i))
        # prints layout of bottom of board
        print('. +-----------------+ .')
        print('. . a b c d e f g h . .')

    def moves(self):
        for row in self.board:
            for piece in row:
                if piece.colour == self.move:
                    print(piece.colour)
        return self.available_moves

    def reset(self):
        # resets board to starting position
        board = ['rnbqkbnr', 'pppppppp', '........', '........', '........', '........', 'PPPPPPPP', 'RNBQKBNR', 'w',
                 'KQkq', '-', 0, 1]

    def clear(self):
        # clears board
        board = ['........', '........', '........', '........', '........', '........', '........', '........']

    def get_move(self):
        return self.move

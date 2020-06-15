class Board:
    moves = []

    def __init__(self):
        self.board = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR']
        self.move = 'w'  # whose move is it?
        self.castling = 'KQkq'  # who can castle
        self.en_passant = '-'  # which square is en passant available on
        self.halfMove = 0  # number of half moves since last capture or pawn move
        self.fullMove = 1  # move number
        # for i in range(8):
        #     self.board[0][i]

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
        return self.moves

    def reset(self):
        # resets board to starting position
        board = ['rnbqkbnr', 'pppppppp', '........', '........', '........', '........', 'PPPPPPPP', 'RNBQKBNR', 'w',
                 'KQkq', '-', 0, 1]

    def clear(self):
        # clears board
        board = ['........', '........', '........', '........', '........', '........', '........', '........']

    def get_move(self):
        return self.move

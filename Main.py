from Board import Board


board = Board()
while True:
    board.print()
    # print who is to move
    if board.get_move() == 'w':
        response = input("White's move (Type '?' for list of available moves)")
    else:
        response = input("Black's move (Type '?' for list of available moves)")
    if response == '?':
        moves = board.moves()
        for move in moves:
            print(move)

#import Chess as c

board = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR','w','KQkq','-',0,1]

move = 'Nc3'
piece = move[0]

if piece == 'N':
    if board[8] == 'w':
        pass
    else:
        pass
elif piece == 'R':
    pass
elif piece == 'B':
    pass
elif piece == 'Q':
    pass
elif piece == 'K':
    pass
elif piece == 'P':
    pass
else:
    raise IndexError

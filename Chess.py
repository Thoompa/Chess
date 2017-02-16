import testingAvailableMoves as am
board = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR','w','KQkq','-',0,1]
global moves
Gmoves = am.availableMoves(board)

def printBoard():
    #print layout of top of board
    #print('\n' * 50)
    print('. . a b c d e f g h . .')
    print('. +-----------------+ .')
    #print board contents
    for i in range(0,8):
        print(str(8 - i) +' | ' + ' '.join(map(str,board[i])) + ' | ' + str(8 - i))
    #prints layout of bottom of board
    print('. +-----------------+ .')
    print('. . a b c d e f g h . .')
    #print who is to move
    if (board[8] == 'w'):
        print("White's move (Type '?' for list of available moves)")
    else:
        print("Black's move (Type '?' for list of available moves)")

def findPiece(piece):
    for i in range(0,8):
        n = 8
        for x in board[i]:
            if x == piece:
                n = chr(ord('a') + 8 - n)
                return n + str(8 - i)
            n -= 1
    raise IndexError

def let2num(let):
    try:
        return ord(let) - ord('a')
    except:
        raise IndexError

def movePiece(old,new,piece):
    try:
        oldNum = 8 - int(old[1])
        newNum = 8 - int(new[1])
        newLet = let2num(new[0])
        if newLet > 7 or newLet < 0:
            raise IndexError
        i = ord(old[0]) - ord('a')
        if board[oldNum][i] == piece:
            board[newNum] = board[newNum][:newLet] + piece + board[newNum][newLet+1:]
            board[oldNum] = board[oldNum][:i] + '.' + board[oldNum][i+1:]
    except:
        raise IndexError

def move():
    while True:
        moves = Gmoves
        try:
            move = input('')
            if move == "?":
                for i in moves:
                    print(i[0])
            else:
                for i in range(len(moves)):
                    if moves[i][0] == move:
                        print(move + ' hi')
                        move = moves[i]
                        if len(move[0]) == 2:
                            if board[8] == 'w':
                                move = ('P' + move[0],move[1])
                            else:
                                move = ('p' + move[0], move[1])
                        movePiece(move[1], move[0][-2] + move[0][-1], move[0][0])
                        moves = am.availableMoves(board)
                        if (board[8] == 'w'):
                            board[8] = 'b'
                        else:
                            board[8] == 'w'
                    else:
                        raise IndexError
            break
        except IndexError:
            print('Invalid Move')

def FENtoBoard(FEN):
    pass

def boardtoFEN():
    FEN = ''
    for i in range(8):
        count = 0
        for j in range(len(board[i])):
            if board[i][j] != '.':
                FEN += board[i][j]
            else:
                count += 1
                if j != 7:
                    if board[i][j+1] != '.':
                        FEN += str(count)
                        count = 0
                else:
                    FEN += str(count)
        if i != 7:
            FEN += '/'
        else:
            FEN += ' '
    FEN += ' '.join(map(str, board[8:]))
    return FEN

def resetBoard():
    #resets board to starting position
    board = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR','w','KQkq','-',0,1]

def clearBoard():
    #clears board
    board = ['........','........','........','........','........','........','........','........','w','KQkq','-',0,1]
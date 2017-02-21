board = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR','w','KQkq','-',0,1]
#Gmoves = am.availableMoves(board)

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

class pieceClass(object):

    def __init__(self, piece, square):
        self.piece = piece
        self.square = square
        self.moves = []
        self.availableMoves()

    def availableMoves(self):
        if self.piece.upper() == 'P':
            whiteOrBlack = 1
            if self.piece.islower():
                whiteOrBlack = -1
            if self.square[1] == '2' or self.square[1] == '7':
                pieceInSquare = isOccupied(self.square[0] + str(int(self.square[1]) + (2 * whiteOrBlack)))
                if pieceInSquare == self.square[0] + str(int(self.square[1]) + (2 * whiteOrBlack)):
                    print('MEME')
                    self.moves.append((pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + (10 * whiteOrBlack)))
            if pieceInSquare == rowcolToSquare(int(self.square) + (10 * whiteOrBlack)):
                self.moves.append((pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + (9 * whiteOrBlack)))
            if pieceInSquare[0] == 'x':
                self.moves.append((rowcolToSquare(self.square)[0] + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + (11 * whiteOrBlack)))
            if pieceInSquare[0] == 'x':
                self.moves.append((rowcolToSquare(self.square)[0] + pieceInSquare, rowcolToSquare(self.square)))

        elif self.piece.upper() == 'N':
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 19))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 21))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 8))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 12))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 12))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 8))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 21))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 19))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))

        elif self.piece.upper() == 'R':
            blocked = False
            move = 0
            while not (blocked):
                move += 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move += 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))

        elif self.piece.upper() == 'B':
            blocked = False
            move = 0
            while not (blocked):
                move += 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move += 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))

        elif self.piece.upper() == 'Q':
            blocked = False
            move = 0
            while not (blocked):
                move += 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move += 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move += 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            blocked = False
            move = 0
            while not (blocked):
                move += 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            move = 0
            blocked = False
            while not (blocked):
                move -= 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))

        elif self.piece.upper() == 'K':
            # just have to make sure square isn't defended
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 9))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 10))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 11))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 1))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 1))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 11))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 10))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 9))
            if pieceInSquare != ' ':
                self.moves.append((self.piece + pieceInSquare, rowcolToSquare(self.square)))
         #available moves

def initialiseBoard():
    piecesOnBoard = {}
    for i in range(8):
        for j in range(8):
            selectedPiece = board[i][j]
            if selectedPiece != '.':
                name = selectedPiece + '1'
                iterable = 1
                while True:
                    name = name[:-1] + str(iterable)
                    try:
                        piecesOnBoard[name]
                        iterable += 1
                    except KeyError:
                        #print(name)
                        break
                piecesOnBoard[name] = pieceClass(selectedPiece, rowcolToSquare(str(i) + str(j)))
                print(piecesOnBoard[name].piece + ' ' + piecesOnBoard[name].square)

    '''list = []
    for key, value in piecesOnBoard.items():
        list.append(key)
    list.sort()
    print(list)'''


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
'''
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
'''

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

def rowcolToSquare(pieceSquare):
    try:
        return chr(int(str(pieceSquare)[1]) + 97) + str(8-int(str(pieceSquare)[0]))
    except TypeError:
        print(pieceSquare)
        print(type(pieceSquare))
        raise TypeError

def squareToRowCol(pieceSquare):
    return str(8-int(pieceSquare[1])) + str(ord(pieceSquare[0]) - 97)

def isOccupied(pieceSquare):
    try:
        pieceSquareInt = int(pieceSquare)
    except ValueError:
        pieceSquareInt = int(squareToRowCol(pieceSquare))
    pieceSquareInt = str(pieceSquareInt)
    if int(pieceSquareInt) < 10 or pieceSquareInt[1] == '8' or pieceSquareInt[1] == '9' or int(pieceSquareInt) > 87:
        return ' '
    occupied = board[8-int(pieceSquareInt[0])][int(pieceSquareInt[1])]
    if occupied == '.':
        return rowcolToSquare(pieceSquareInt)
    elif (occupied.isupper() and board[8] == 'b') or (occupied.islower() and board[8] == 'w'):
        return 'x' + rowcolToSquare(pieceSquareInt)
    else:
        return ' '

initialiseBoard()
# create a dictionary of all legal moves (list moves for each piece)
moves = []
cboard = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR','w','KQkq','-',0,1]

def availableMoves(board):
    cboard = board
    for row in range(8):
        column = 0
        for piece in cboard[row]:
            column += 1
            pieceSquare = str(8 - row) + str(column - 1)
            if cboard[8] == 'w':
                if piece.isupper():
                    whatPiece(piece,pieceSquare)
            else:
                if piece.islower():
                    whatPiece(piece,pieceSquare)
    return moves

def whatPiece(piece,square):
    if piece.upper() == 'P':
        whiteOrBlack = 1
        if cboard[8] == 'b':
            whiteOrBlack = -1
        if square[0] == '2' or square[0] == '7':
            pieceInSquare = isOccupied(str(int(square) + (20 * whiteOrBlack)))
            if pieceInSquare == rowcolToSquare(int(square) + (20 * whiteOrBlack)):
                moves.append((pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) + (10 * whiteOrBlack)))
        if pieceInSquare == rowcolToSquare(int(square) + (10 * whiteOrBlack)):
            moves.append((pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) + (9 * whiteOrBlack)))
        if pieceInSquare[0] == 'x':
            moves.append((rowcolToSquare(square)[0] + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) + (11 * whiteOrBlack)))
        if pieceInSquare[0] == 'x':
            moves.append((rowcolToSquare(square)[0] + pieceInSquare, rowcolToSquare(square)))
    elif piece.upper() == 'N':
        pieceInSquare = isOccupied(str(int(square) + 19))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) + 21))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) + 8))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) + 12))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) - 12))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) - 8))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) - 21))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = isOccupied(str(int(square) - 19))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
    elif piece.upper() == 'R':
        blocked = False
        move = 0
        while not(blocked):
            move += 1
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not(blocked):
            move -= 1
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not(blocked):
            move += 10
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not(blocked):
            move -= 10
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
    elif piece.upper() == 'B':
        blocked = False
        move = 0
        while not (blocked):
            move += 9
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move += 11
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move -= 11
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move -= 9
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
    elif piece.upper() == 'Q':
        blocked = False
        move = 0
        while not (blocked):
            move += 9
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move += 10
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move += 11
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move -= 1
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        blocked = False
        move = 0
        while not (blocked):
            move += 1
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move -= 11
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move -= 10
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        move = 0
        blocked = False
        while not (blocked):
            move -= 9
            pieceInSquare = isOccupied(str(int(square) + move))
            if pieceInSquare[0] == 'x':
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
                blocked = True
            elif pieceInSquare == ' ':
                blocked = True
            else:
                moves.append((piece + pieceInSquare, rowcolToSquare(square)))
    elif piece.upper() == 'K':
        #just have to make sure square isn't defended
        pieceInSquare = isOccupied(str(int(square) + 9))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) + 10)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) + 11)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) - 1)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) + 1)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) - 11)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) - 10)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
        pieceInSquare = (isOccupied(str(int(square) - 9)))
        if pieceInSquare != ' ':
            moves.append((piece + pieceInSquare, rowcolToSquare(square)))
    else:
        print(piece)

def rowcolToSquare(pieceSquare):
    try:
        return chr(int(str(pieceSquare)[1]) + 97) + str(int(str(pieceSquare)[0]))
    except TypeError:
        print(pieceSquare)
        print(type(pieceSquare))
        raise TypeError
def isOccupied(pieceSquare):
    if int(pieceSquare) < 10 or pieceSquare[1] == '8' or pieceSquare[1] == '9' or int(pieceSquare) > 87:
        return ' '
    occupied = cboard[8-int(pieceSquare[0])][int(pieceSquare[1])]
    if occupied == '.':
        return rowcolToSquare(pieceSquare)
    elif (occupied.isupper() and cboard[8] == 'b') or (occupied.islower() and cboard[8] == 'w'):
        return 'x' + rowcolToSquare(pieceSquare)
    else:
        return ' '

'''
cboard = ['rnbqkbnr','pppppppp','........','........','........','........','PPPPPPPP','RNBQKBNR','w','KQkq','-',0,1]
#c.movePiece('g2','c6','P')
c.printBoard()
availableMoves()
print(cboard)
'''
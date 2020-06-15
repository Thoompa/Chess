class Piece(object):

    def __init__(self, character, square, colour):
        self.character = character
        self.square = square
        self.colour = colour
        self.moves = []
        self.availableMoves()

    def availableMoves(self):
        if self.character.upper() == 'P':
            whiteOrBlack = -1
            if self.character.islower():
                whiteOrBlack = 1
            if self.square[1] == '2' or self.square[1] == '7':
                pieceInSquare = isOccupied(self.square[0] + str(int(self.square[1]) + (2 * whiteOrBlack)))
                if pieceInSquare == self.square[0] + str(int(self.square[1]) + (2 * whiteOrBlack)):
                    self.moves.append((pieceInSquare, self.square))
                    print(self.moves)
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + (10 * whiteOrBlack)))
            if pieceInSquare == rowcolToSquare(int(squareToRowCol(self.square)) + (10 * whiteOrBlack)):
                self.moves.append((pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + (9 * whiteOrBlack)))
            if pieceInSquare[0] == 'x':
                self.moves.append((self.square)[0] + pieceInSquare, self.square)
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + (11 * whiteOrBlack)))
            if pieceInSquare[0] == 'x':
                self.moves.append((self.square)[0] + pieceInSquare, self.square)

        elif self.character.upper() == 'N':
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 19))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 21))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 8))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 12))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 12))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 8))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 21))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 19))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))

        elif self.character.upper() == 'R':
            blocked = False
            move = 0
            while not (blocked):
                move += 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move += 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))

        elif self.character.upper() == 'B':
            blocked = False
            move = 0
            while not (blocked):
                move += 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move += 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))

        elif self.character.upper() == 'Q':
            blocked = False
            move = 0
            while not (blocked):
                move += 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move += 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move += 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            blocked = False
            move = 0
            while not (blocked):
                move += 1
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 11
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 10
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))
            move = 0
            blocked = False
            while not (blocked):
                move -= 9
                pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + move))
                if pieceInSquare[0] == 'x':
                    self.moves.append((self.character + pieceInSquare, self.square))
                    blocked = True
                elif pieceInSquare == ' ':
                    blocked = True
                else:
                    self.moves.append((self.character + pieceInSquare, self.square))

        elif self.character.upper() == 'K':
            # just have to make sure square isn't defended
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 9))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 10))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 11))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 1))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) + 1))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 11))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 10))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
            pieceInSquare = isOccupied(str(int(squareToRowCol(self.square)) - 9))
            if pieceInSquare != ' ':
                self.moves.append((self.character + pieceInSquare, self.square))
         #available moves

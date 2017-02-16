import Chess as c

notQuit = True
while notQuit:
    print('Menu\n')
    print('1. New Game:')
    print('2. Continue Game:')
    print('3. Print FEN:')
    print('4. Import FEN:')
    print('5. Available moves')
    print('6. Save game (in development)')
    print('7. Quit:\n')
    command = input('Which option? ')
    invalid = True
    if command == '1':
        c.resetBoard()
        command = '2'
    if command == '2':
        c.printBoard()
        while True:
            c.move()
            c.printBoard()
    elif command == '3':
        print(c.boardtoFEN())
    elif command == '4':
        FEN = input('FEN:')
        c.FENtoBoard(FEN)
    elif command == '5':
        c.am.availableMoves(c.board)
    elif command == '6':
        pass
    elif command == '7':
        notQuit = False
    else:
        print("Invalid option")


#testfrog
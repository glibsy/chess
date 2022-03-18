
class fen():
    def boardToFen(board):
        fen = ""
        emptySquares = 0
        count = 0
        for i in board:
            count += 1

            if i == "0":
                emptySquares += 1
            else:
                
                if emptySquares != 0:
                    fen += str(emptySquares)
                    emptySquares = 0
                fen += i
            
            if count % 8 == 0 and emptySquares != 0:
                fen += str(emptySquares)
                emptySquares = 0
                
            
            if count % 8 == 0 and count != 64:
                fen += '/'
        
        return fen
    
    def fenToBoard(fen):
        board = ""

        for i in fen:
            if i.isnumeric():
                board += "0" * int(i)
            elif i.isalpha():
                board += i

        return board
#6r1/R4p2/1pp5/3bk3/6p1/2PB4/2P2PPP/6K1 b - - 0 25
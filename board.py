class Board():


    def __init__(self):
        self.board = ""
    def getBoard(self):
        return self.board
    def setBoard(self, b):
        self.board = b

    def setStartingPosition(self):
        self.board = "rnbqkbnrpppppppp00000000000000000000000000000000PPPPPPPPRNBQKBNR"

    def makeMove(self, move):
        b = self.board
        i_sq = self.notationToSq(move[0:2])
        f_sq = self.notationToSq(move[2::])
        piece = self.board[i_sq]

        if i_sq != 63:
            b = b[:i_sq] + b[i_sq + 1::]
            b = b[:f_sq] + piece + b[f_sq + 1::]
        else:
            b = b[:i_sq]
            b = b + piece

        print(b)
        self.board = b
        
    def getDirections(self):
        return [-8,8,-1,1,-9,-7,7,9]

    def getMoves(self):
        b = self.board
        moves = []
        square = 0
        for i in b:
            if i == "p":
                moves.extend(self.getBlackPawnMoves(square))
            elif i == "P":
                moves.extend(self.getWhitePawnMoves(square))
            elif i.lower() == "r":
                moves.extend(self.getRookMoves(square))
            elif i.lower() == "n":
                moves.extend(self.getKnightMoves(square))
            elif i.lower() =="b":
                moves.extend(self.getBishopMoves(square))
            elif i.lower() == "q":
                moves.extend(self.getQueenMoves(square))
            elif i.lower() == "k":
                moves.extend(self.getKingMoves(square))
            square += 1
        return moves

    def toSquare(self, rank, file):
        return rank * 8 + file
    def toCoords(self, square):
        file = int(float(square)) % 8
        rank = int((square - file) / 8)
        return rank, file

    def sqToNotation(self, square):
        rank = square % 8
        square = square - square % 8
        file =  8 - int(square / 8)

        dic = {
            0 : 'a',
            1 : 'b',
            2 : 'c',
            3 : 'd',
            4 : 'e',
            5 : 'f',
            6 : 'g',
            7 : 'h',
        }

        return dic[rank] + str(file)

    def notationToSq(self, square):
        square = str(square)
        file = square[0]
        rank = square [1]

        dic = {
            'a' : 0,
            'b' : 1,
            'c' : 2,
            'd' : 3,
            'e' : 4,
            'f' : 5,
            'g' : 6,
            'h' : 7,
        }

        file = dic[file]
        rank = (8 - int(rank)) * 8

        return file + rank

    def isFriendly(self, p1, p2):
        if p1.islower() and p2.islower():
            return True
        elif p1.isupper() and p2.isupper():
            return True
        else:
            return False


    def numToEdge(self, square):
        file = square % 8
        rank = int((square - file) / 8)


        n = rank
        s = 7 - rank
        w = file
        e = 7 - file

        nw = min(n ,w)
        ne = min(n , e)
        sw = min(s, w)
        se = min(s, e)

        return n, s, w , e, nw, ne, sw, se
    
    def generateSlidingPieces(self, square):
        moves = []
        numToEdge = self.numToEdge(square)
        direc = self.getDirections()
        b = self.getBoard()
        los = True
        captured = False
        movesOnBoard = []
        a_piece = b[square]
        d_piece = ""
        
        for i in range(len(direc)):
            los = True
            for j in range(1,8):
                endSquare = square + direc[i] * j

                if numToEdge[i] -j >= 0 and los and a_piece != "0":
                    #print(endSquare)
                    d_piece = b[endSquare]
                    if b[endSquare] != "0":
                        if  self.isFriendly(a_piece, d_piece):
                            los = False
                        else:
                            moves.append(self.sqToNotation(square) + self.sqToNotation(endSquare))
                            los = False
                    else:
                        moves.append(self.sqToNotation(square) + self.sqToNotation(endSquare))

        movesOnBoard = []
        movesOnBoard.append(moves)
        return movesOnBoard


    def getKingMoves(self, square):
        moves = self.generateSlidingPieces(square)
        output = []
        for direction in moves:
            if len(direction) > 0:
                output.append(direction[0])
        return output
    
    def getQueenMoves(self, square):
        moves = self.generateSlidingPieces(square)
        output = []
        for i in moves:
            output.extend(i)
        return output


    def getRookMoves(self, square):
        moves = self.generateSlidingPieces(square)
        output = []
        for direction in moves[0:4]:
            output.extend(direction)
        return output
    
    def getBishopMoves(self, square):
        moves = self.generateSlidingPieces(square)
        output = []
        for direction in moves[4:8]:
            output.extend(direction)
        return output
    
    def getKnightMoves(self, square):
        b = self.board
        p, q = self.toCoords(square)
        moves = []

        n = 8
        m = 8

        # All possible moves of a knight
        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]
 
        count = 0
 
    # Check if each possible move
    # is valid or not
        for i in range(8):
         
        # Position of knight after move
            x = p + X[i]
            y = q + Y[i]
 
        # count valid moves
            endSquare = self.toSquare(x, y)
            if(x >= 0 and y >= 0 and x < n and y < m):
                
                if(not self.isFriendly(b[square] , b[endSquare])):
                    print(endSquare)
                    moves.append(self.sqToNotation(square) + self.sqToNotation(endSquare))

        return moves

    def getWhitePawnMoves(self, square):
        moves = []
        moves.append(self.sqToNotation(square) + self.sqToNotation(square -8))
        if int((square - (square % 8)) / 8) == 6:
            moves.append(self.sqToNotation(square) + self.sqToNotation(square - 16))
        return moves
    def getBlackPawnMoves(self, square):
        moves = []
        moves.append(self.sqToNotation(square) + self.sqToNotation(square + 8))
        if int((square-(square%8))/8) == 1:
            moves.append(self.sqToNotation(square) + self.sqToNotation(square + 16))
        return moves
    #def getBlackPawnMoves():
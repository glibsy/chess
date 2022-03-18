import pygame
from fen import fen
from Piece import *
from board import Board

b = Board()
class Displaygame():

    def getSquare(x, y, cell):
        sq = x - (x % cell), y - (y%cell)
        num = 0
        for i in range(8):
            for j in range(8):

                if (j*cell, i*cell) == sq:
                    return num
                else:
                    num+=1
    def getMoves(piece, square):

        if piece == "P":
            return b.getWhitePawnMoves(square)
        if piece == "p":
            return b.getBlackPawnMoves(square)
        piece = piece.lower()
        if piece == "k":
            return b.getKingMoves(square)
        elif piece =="q":
            return b.getQueenMoves(square)
        elif piece == "n":
            return b.getKnightMoves(square)
        elif piece == "b":
            return b.getBishopMoves(square)
        elif piece == "r":
            return b.getRookMoves(square)
        else:
            return
    #initialize pygame module, customize display window
    pygame.init()   
    win_area = 600
    screen = pygame.display.set_mode([win_area, win_area])
    pygame.display.set_caption("Chess")

    running = ("True")

    
    #square rgb colors
    light = (247, 231, 156)
    dark = (178, 137, 97)
    color = light


    rank = 0
    file = 0
    count = 0


    cell_area = int(win_area / 8)

    #load image
    pieces = pygame.image.load("images/chess_pieces.png")
    pieces = pygame.transform.scale(pieces, (6 * cell_area,2 * cell_area))


    #partition image to capture each individual piece on a chessgame
    wk_coords = (0,0,cell_area, cell_area)
    wq_coords = (cell_area, 0, cell_area,cell_area)
    wb_coords = (cell_area * 2, 0, cell_area, cell_area)
    wn_coords = (cell_area * 3, 0, cell_area, cell_area )
    wr_coords = (cell_area * 4, 0, cell_area, cell_area)
    wp_coords = (cell_area * 5, 0, cell_area, cell_area)

    bk_coords = (0,cell_area,cell_area, cell_area)
    bq_coords = (cell_area, cell_area, cell_area,cell_area)
    bb_coords = (cell_area * 2, cell_area, cell_area, cell_area)
    bn_coords = (cell_area * 3, cell_area, cell_area, cell_area)
    br_coords = (cell_area * 4, cell_area, cell_area, cell_area)
    bp_coords = (cell_area * 5, cell_area, cell_area, cell_area)



    #translate game notation to corresponding chess piece on image
    piece_notation = {
        "p" : bp_coords,
        "r" : br_coords,
        "n" : bn_coords,
        "b" : bb_coords,
        "q" : bq_coords,
        "k" : bk_coords,

        "P" : wp_coords,
        "R" : wr_coords,
        "N" : wn_coords,
        "B" : wb_coords,
        "Q" : wq_coords,
        "K" : wk_coords
    }

    #game is a string of length 64 that contains a character for each square on the
    #chessboard. 
    f = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    game = fen.fenToBoard(f)
    isPressed = False  
    boardObject = Board()
    boardObject.setBoard(game)

            
    #game loop
    while(running):
        boardObject.setBoard(game)
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0 :
                    color = light
                else:
                    color = dark


        
            
                if count >= 63:
                    count = 0
                else:
                    count += 1

                #get piece
                square = game[count-1]
                
                rank = i * cell_area
                file = j * cell_area

                pygame.draw.rect(screen, color, pygame.Rect(file,rank,cell_area,cell_area), 0)
                

                if square != "0":
                    screen.blit(pieces, (file, rank), piece_notation[square])
                
                    
        #track mouse on screen
        x,y = pygame.mouse.get_pos()
        sq = int(getSquare(x, y, cell_area))
        #record mouse events
         
        if isPressed:
            piece = piece
        else:
            piece = game[sq]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    isPressed = True

                    #record initial square 
                    i_square = sq
                    game = game[:i_square] + "0" + game[i_square + 1:]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    isPressed = False
                    f_square = sq
                    #print(piece, getMoves(piece, i_square))
                    if f_square in getMoves(piece, i_square):
                        game = game[:f_square] + piece + game[f_square + 1:]
                    else:
                        print("not a legal move")
                        game = game[:i_square] + piece + game[i_square + 1:]
                    
                    #game = game[:f_square] + piece + game[f_square + 1:]
            
        #move piece when drag and dropped
        if isPressed and piece != "0":
            screen.blit(pieces, (x - (cell_area / 2), y - (cell_area / 2)), piece_notation[piece])
            pygame.display.update(x,y,cell_area,cell_area)
        
        b.setBoard(game)


        #update game position according to display
        pygame.display.flip()
  
        #display 64 squares on a game
        
    pygame.quit()
    


Displaygame()

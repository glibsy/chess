import pygame
from fen import fen
from board import Board


class display():
    def __init__(self, w):
        pygame.init()
        self.win_area = w
        self.cell_area = int(self.win_area / 8)
        self.screen = pygame.display.set_mode([self.win_area, self.win_area])
        pygame.display.set_caption("Chess")

        #load image
        self.pieces = pygame.image.load("images/chess_pieces.png")
        self.pieces = pygame.transform.scale(self.pieces, (6 * self.cell_area,2 * self.cell_area))


    #partition image to capture each individual piece on a chessgame
        wk_coords = (0,0,self.cell_area, self.cell_area)
        wq_coords = (self.cell_area, 0, self.cell_area,self.cell_area)
        wb_coords = (self.cell_area * 2, 0, self.cell_area, self.cell_area)
        wn_coords = (self.cell_area * 3, 0, self.cell_area, self.cell_area )
        wr_coords = (self.cell_area * 4, 0, self.cell_area, self.cell_area)
        wp_coords = (self.cell_area * 5, 0, self.cell_area, self.cell_area)

        bk_coords = (0,self.cell_area,self.cell_area, self.cell_area)
        bq_coords = (self.cell_area, self.cell_area, self.cell_area,self.cell_area)
        bb_coords = (self.cell_area * 2, self.cell_area, self.cell_area, self.cell_area)
        bn_coords = (self.cell_area * 3, self.cell_area, self.cell_area, self.cell_area)
        br_coords = (self.cell_area * 4, self.cell_area, self.cell_area, self.cell_area)
        bp_coords = (self.cell_area * 5, self.cell_area, self.cell_area, self.cell_area)



    #translate game notation to corresponding chess piece on image
        self.piece_notation = {
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
    
    def getSquare(self, x, y):
        x = x - (x % self.cell_area)
        y = y - (y % self.cell_area)

        return int(y / self.cell_area) * 8 + int(x / self.cell_area)

    def drawBoard(self):

        light = (247, 231, 156)
        dark = (178, 137, 97)
        color = light

        r = 0
        f = 0

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0 :
                    color = light
                else:
                    color = dark

                r = i * self.cell_area
                f = j * self.cell_area

                pygame.draw.rect(self.screen, color, pygame.Rect(f,r,self.cell_area,self.cell_area), 0)
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
    
    def drawPieces(self, b):
        for i in range(8):
            for j in range(8):
                square = i * 8 + j
                piece = b[square]
                if piece != "0":

                    self.screen.blit(self.pieces, (j * self.cell_area, i * self.cell_area), self.piece_notation[piece])


    def getMouseEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button  == 1:
                    return "click"
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    return "release"
    
    def dragAndDrop(self, x, y, piece):
        self.screen.blit(self.pieces, (x - (self.cell_area / 2), y - (self.cell_area / 2)), self.piece_notation[piece])
        pygame.display.update(x,y,self.cell_area,self.cell_area)


    def updateScreen(self):
        pygame.display.flip()


        

        


                
                
                    
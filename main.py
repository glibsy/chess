import pygame
from display import display
from board import Board
from fen import fen
import time

if __name__ == "__main__":
    d = display(600)
    b = Board()
    #b.setBoard(fen.fenToBoard("8/8/8/4Q3/8/8/8/8"))
    b.setStartingPosition()
    isRunning = True
    isPressed = False

    i_sq = 40
    f_sq = 0
    while(isRunning):
        
        d.drawBoard()
        d.drawPieces(b.getBoard())
        x,y = pygame.mouse.get_pos()
        sq = d.getSquare(x, y)
        
        if isPressed != True:
            piece = b.getBoard()[i_sq]

        mouseState = d.getMouseEvent()
        if isPressed == True and piece != "0":
            d.dragAndDrop(x, y, piece)
        if mouseState == "quit":
            isRunning = False
        elif mouseState == "click":
            i_sq = sq
            piece = b.getBoard()[i_sq]
            isPressed = True
        elif mouseState == "release":
            f_sq = sq
            isPressed = False

        b.generateSlidingPieces(sq)
        d.updateScreen()
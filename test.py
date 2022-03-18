from board import Board
from fen import fen
b = Board()

#b.setBoard(fen.fenToBoard("8/8/8/4Q3/8/8/8/8"))
b.setStartingPosition()


b.makeMove("e2e4")
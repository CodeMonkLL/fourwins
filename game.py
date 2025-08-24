from player import Player
from board import Board

class Game:
    def __init__(self, board: Board, player1: Player, player2: Player):
        self._actualplayer = 1
        self._gameTurn = 1
        self._Player1 = player1
        self._Player2 = player2
        self._board = board

    def switchActualplayer(self):
        self._actualplayer = 2 if self._actualplayer == 1 else 1

    def resetGameTurn(self):
        self._gameTurn = 1

    def maxGameTurnReached(self):
        if self._gameTurn >= self._board.rows * self._board.columns:
            print("------------------------------------------------")
            print("Maximale Spielzüge erreicht, unentschieden")
            return True
        return False

    def doGameTurn(self):
        columinput = int(input(f"Gib die gewünschte Spalte ein (1-{self._board.columns}): "))
        
        while not (1 <= columinput <= self._board.columns):
            print("Ungültige Eingabe. Bitte erneut versuchen.")
            columinput = int(input(f"Gib die gewünschte Spalte ein (1-{self._board.columns}): "))

        success = self._board.setChip(columinput - 1, self._actualplayer)

        while not success:
            print("Spalte voll! Bitte wähle eine andere.")
            columinput = int(input(f"Gib die gewünschte Spalte ein (1-{self._board.columns}): "))
            success = self._board.setChip(columinput, self._actualplayer)

        self._gameTurn += 1
        self._board.printBroad()

        if self._board.finishGame():
            return True
        if self.maxGameTurnReached():
            return True
        return False

from board import Board
from player import Player
from game import Game


print("Willkommen beim Vier Gewinnt Konsolenspiel")
print("Gib bitte den Namen für Spieler 1 ein:")
namep1 = input("Name 1 eingeben:")
print("Gib bitte den Namen für Spieler 2 ein:")
namep2 = input("Name 2 eingeben:")

player1 = Player(1,namep1)
player2 = Player(2,namep2)

broad = Board()

game = Game(broad, player1, player2)


while True:
    finished = game.doGameTurn()
    if finished:
        print("Spiel zuende")
        break
    else:
        game.switchActualplayer()


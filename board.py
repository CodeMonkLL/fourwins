class Board:

    def __init__(self,rows:int = 6, columns:int = 7):
        self.rows = rows
        self.columns = columns
        self.broad: list[list[int]] = []  
        self.createBroad()
        self.printBroad()

    def createBroad(self):
        self.broad = [] 
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(0)
            self.broad.append(row)

    def printBroad(self):
        for row in self.broad:
            print(row)

    def setChip(self, column: int, player: int):
        """
        Setzt den Chip des Spielers in die gewählte Spalte.
        Der Chip fällt automatisch in die unterste freie Reihe.
        """
        if column < 0 or column >= self.columns:
            print("Ungültige Spalte!")
            return False

        for row in reversed(range(self.rows)):
            if self.broad[row][column] == 0:
                self.broad[row][column] = player
                return True

        print("Spalte voll!")
        return False

        

    def checkStatus(self):
        """
        Prüft, ob ein Spieler vier Chips in einer Reihe hat.
        Gibt 1 oder 2 zurück, wenn ein Spieler gewonnen hat, sonst 0.
        """
        for reihe in range(self.rows):
            for spalte in range(self.columns):
                spieler = self.broad[reihe][spalte]
                if spieler == 0:
                    continue

                # Horizontal prüfen
                if spalte <= self.columns - 4:
                    if all(self.broad[reihe][spalte + i] == spieler for i in range(4)):
                        return spieler

                # Vertikal prüfen
                if reihe <= self.rows - 4:
                    if all(self.broad[reihe + i][spalte] == spieler for i in range(4)):
                        return spieler

                # Diagonal rechts unten prüfen
                if reihe <= self.rows - 4 and spalte <= self.columns - 4:
                    if all(self.broad[reihe + i][spalte + i] == spieler for i in range(4)):
                        return spieler

                # Diagonal links unten prüfen
                if reihe <= self.rows - 4 and spalte >= 3:
                    if all(self.broad[reihe + i][spalte - i] == spieler for i in range(4)):
                        return spieler

        return 0
    

    def finishGame(self):
        status = self.checkStatus()
        if status == 0:
            print("Das Spiel läuft weiter.")
            return False
        elif status == 1:
            print("Spieler 1 hat gewonnen")
            return True
        elif status == 2:
            print("Spieler 2 hat gewonnen")
            return True
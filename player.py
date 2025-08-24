class Player:
    def __init__(self,player:int, name:str):
        
        self.player = player
        self.name = name
        self.color = None
        self.selectColor()
        self.callname()
        

    def callname(self):
        print(f"Player {self.name} startet mit der Farbe {self.color}")

    def selectColor(self):
        if self.player == 1:
            self.color = "Blau"
        elif self.player == 2:
            self.color = "Rot"
        else: 
            self.color = "Unbekannt"
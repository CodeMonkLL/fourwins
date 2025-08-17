class Broad:

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

if __name__ == "__main__":
    broad = Broad()
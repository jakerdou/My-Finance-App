class TransCategory:
    name = ""
    isExpense = True
    catTransList = []

    def __init__(self):
        name = ""
        isExpense = True
        catTransList = []

    def printCat(self):
        print("Name: " + self.name)
        print("Number of transactions: " + str(len(self.catTransList)))

    #FIXME: thinking we should maybe add transactions through this class

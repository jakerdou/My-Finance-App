import Transaction as trans
import TransCategory as transCat

class PaymentMethod:
    name = ""
    balance = 0.0
    #transList = []
    categoryList = []

    def __init__(self):
        name = ""
        balance = 0.0

    def AddTransaction(self, catAddingTo, transToAdd):
        if(not catAddingTo.isExpense):
            modifier = 1
        else:
            modifier = -1

        transToAdd.transCategory = catAddingTo

        #add to list (pass catAddingTo by reference)
        catAddingTo.catTransList.append(transToAdd)

        #add or subtract from balance
        self.balance = self.balance + modifier * transToAdd.amount


    def RemoveTransaction(self, catRemovingFrom, transToRemove):
        print("this function is not working yet")


    def AddCategory(self, categoryToAdd):
        self.categoryList.append(categoryToAdd)

    def RemoveCategory(self, categoryToRemove):
        print("this function is not working yet")

    def printPM(self):
        print("Name: " + self.name)
        print("Balance: $" + str(self.balance))

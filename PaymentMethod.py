import Transaction as trans
import TransCategory as transCat

class PaymentMethod:
    name = ""
    balance = 0.0
    transList = []
    categoryList = []

    def __init__(self):
        name = ""
        balance = 0.0

    def AddTransaction(self, transToAdd):
        if(not transToAdd.transCategory.isExpense):
            modifier = 1
        else:
            modifier = -1

        #add to list
        self.transList.append(transToAdd)

        #add or subtract from balance
        self.balance = self.balance + modifier * transToAdd.amount


    def RemoveTransaction(self, indexToRemove): #maybe change to where you're referencing an object and not an index
        if(not self.transList[indexToRemove].transCategory.isExpense):
            modifier = -1
        else:
            modifier = 1

        #add or subtract from balance
        self.balance = self.balance + modifier * self.transList[indexToRemove].amount

        #remove from list
        del self.transList[indexToRemove]


    def AddCategory(self, categoryToAdd):
        self.categoryList.append(categoryToAdd)

    def RemoveCategory(self, indexToRemove):
        del self.categoryList[indexToRemove]

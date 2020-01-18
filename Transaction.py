import datetime
import TransCategory as transCat

class Transaction:
    description = ""
    dateOfTrans = datetime.datetime(1970,1,1)
    amount = 0.0
    transCategory = transCat.TransCategory() #will need to change this when I get category working

    def __init__(self):
        description = ""
        dateOfTrans = datetime.datetime(1970,1,1)
        amount = 0.0
        transCategory = transCat.TransCategory()

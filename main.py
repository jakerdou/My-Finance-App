import datetime
import AppUser as au
import PaymentMethod as pm
import Transaction as trans
import TransCategory as transCat

#*************************FIXME: get rid of FIXMEs in all files**************************************

userList = []
selection = ""
currUser = 0 #FIXME: need to get this to actually keep track of current user
stars = "***********************************************************"

#FIXME: get rid of this, just using it so i dont have to type it each time
me = au.AppUser()
me.name = "James Robinson"
me.email = "jakerdou@tamu.edu"
myCash = pm.PaymentMethod()
myCash.name = "Cash"
myCash.balance = 450.0
me.pmList.append(myCash)
userList.append(me)
#FIXME: this



while(not (selection == "0")):
    print("\n*************************MAIN MENU*************************")
    print("* Current User: " + userList[currUser].name + "                            *")
    print("*                                                         *")
    print("* Enter 0 for: exit                                       *")
    print("* Enter 1 for: add user                                   *")
    print("* Enter 2 for: add payment method                         *")
    print("* Enter 3 for: add category to payment method             *")
    print("* Enter 4 for: add transaction to payment method          *")
    print("* Enter 5 for: switch to different user                   *")
    print(stars + "\n")

    selection = input("Enter your selection: ")
    print(stars + "\n")


    if(selection == "1"):
        print()
        newUser = au.AppUser()
        newUser.name = input("What is the user's name? ")
        newUser.email = input("What is the user's email? ")
        userList.append(newUser)
        print("\nUser Added!\n" + stars + "\n")


    if(selection == "2"):
        if(len(userList) == 0):
            print("\nYou must create a user before adding payment methods.")
            print(stars + "\n")
        else:
            newPM = pm.PaymentMethod()
            newPM.name = input("What kind of payment method? ")
            newPM.balance = input("What balance is on it? ")
            userList[currUser].pmList.append(newPM)
            print("\nPayment Method Added!\n" + stars + "\n")


    if(selection == "3"):
        if(len(userList) == 0 or len(userList[currUser].pmList) == 0):
            print("\nYou must create a user with payment methods before adding transactions.")
            print(stars + "\n")
        else:
            print("Payment methods for this user: ")
            for i in range(len(userList[currUser].pmList)):
                print("Enter " + str(i) + " for: " + userList[currUser].pmList[i].name)

            pmSelected = int(input("\nWhich payment method would you like to add a category to? "))
            #FIXME: need to validate input

            newCat = transCat.TransCategory
            newCat.name = input("What is the name of the category? ")
            expenseYorN = input("Is the category an expense? (Enter 'y' if yes) ")

            if(expenseYorN == "y"):
                newCat.isExpense = True
            else:
                newCat.isExpense = False

            userList[currUser].pmList[pmSelected].categoryList.append(newCat)
            print("\nCategory Added!\n" + stars + "\n")


    if(selection == "4"):
        if(len(userList) == 0 or len(userList[currUser].pmList) == 0):
            print("\nYou must create a user with payment methods before adding transactions.")
            print(stars + "\n")
        else:
            print("Payment methods for this user: ")
            for i in range(len(userList[currUser].pmList)):
                print("Enter " + str(i) + " for: " + userList[currUser].pmList[i].name)

            pmSelectedInd = int(input("\nWhich payment method would you like to add a transaction to? "))
            pmSelected = userList[currUser].pmList[pmSelectedInd]
            #FIXME: need to validate input

            #check if this payment method has categories to add to
            if(len(pmSelected.categoryList) == 0):
                print("\nYou must first create categories for this payment method.")
                print(stars + "\n")
            else:
                newTrans = trans.Transaction()
                #FIXME: need to add date
                newTrans.description = input("Enter a description of the transaction: ")
                newTrans.amount = float(input("Enter the amount of the transaction: ")) #FIXME: need to validate input

                #put transaction in category
                print("\nCategories for this payment method:")
                for i in range(len(pmSelected.categoryList)):
                    print("Enter " + str(i) + " for: " + pmSelected.categoryList[i].name)

                catSelected = int(input("\nWhich category does the transaction fit into? "))
                newTrans.category = pmSelected.categoryList[catSelected]

                #add transaction to list
                userList[currUser].pmList[pmSelectedInd].transList.append(newTrans)
                print("\nTransaction Added!\n" + stars + "\n")

#QUESTIONS
#Is python the right language for iOS dev?
#Do I need setters and getters for variables?
#Do I need to make variables private?

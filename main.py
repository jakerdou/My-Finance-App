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
myFood = transCat.TransCategory()
myFood.name = "Food"
myWhata = trans.Transaction()
myWhata.description = "whataburger"
myWhata.amount = 4.20
myWhata.transCategory = myFood

userList.append(me)
me.pmList.append(myCash)
myCash.AddCategory(myFood)
myCash.AddTransaction(myFood, myWhata)
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
    print("* Enter 5 for: view payment methods                       *")
    print("* Enter 6 for: view categories                            *")
    print("* Enter 7 for: view transactions                          *")
    print("* Enter 8 for: switch to different user                   *")
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
            print("\nYou must create a user with payment methods before adding categories.")
            print(stars + "\n")
        else:
            print("Payment methods for this user: ")
            for i in range(len(userList[currUser].pmList)):
                print("Enter " + str(i) + " for: " + userList[currUser].pmList[i].name)

            pmSelected = int(input("\nWhich payment method would you like to add a category to? "))
            #FIXME: need to validate input

            newCat = transCat.TransCategory
            newCat.name = input("What is the name of the category? ")
            expenseYorN = input("Is the category an expense? (Enter 'y' or 'n') ")

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

            pmSelectedIndex = int(input("\nWhich payment method would you like to add a transaction to? "))
            pmSelected = userList[currUser].pmList[pmSelectedIndex]
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

                catSelectedIndex = int(input("\nWhich category does the transaction fit into? "))
                catSelected = pmSelected.categoryList[catSelectedIndex]

                newTrans.category = catSelected

                #add transaction to list
                pmSelected.AddTransaction(catSelected, newTrans)
                #FIXME: add "x amount has been added/subtracted from balance of y"
                print("\nTransaction Added!\n" + stars + "\n")


    if(selection == "5"):
        #check if they have payment methods
        print("Payment Methods for " + userList[currUser].name + "\n")
        for i in userList[currUser].pmList:
            i.printPM()
            print()

        print(stars + "\n")


    if(selection == "6"):
        if(len(userList) == 0 or len(userList[currUser].pmList) == 0):
            print("\nYou must create a user with payment methods before viewing categories.")
            print(stars + "\n")
        else:
            print("Payment methods for " + userList[currUser].name + "\n")
            for i in range(len(userList[currUser].pmList)):
                print("Enter " + str(i) + " for: " + userList[currUser].pmList[i].name)

            pmSelectedIndex = int(input("\nWhich payment method would you like to view the categories of? "))
            #FIXME: need to validate input

            if(len(userList[currUser].pmList[pmSelectedIndex].categoryList) == 0):
                print("You must add categories to this payment method before viewing them.")
                print(stars + "\n")
            else:
                print("Categories for " + userList[currUser].pmList[pmSelectedIndex].name + "\n")
                for i in userList[currUser].pmList[pmSelectedIndex].categoryList:
                    i.printCat()
                    print()

                print(stars + "\n")


    if(selection == "7"):
        if(len(userList) == 0 or len(userList[currUser].pmList) == 0):
            print("\nYou must create a user with payment methods before viewing transactions.")
            print(stars + "\n")
        else:
            print("Payment methods for this user: ")
            for i in range(len(userList[currUser].pmList)):
                print("Enter " + str(i) + " for: " + userList[currUser].pmList[i].name)

            pmSelectedIndex = int(input("\nWhich payment method would you like to view the transactions of? "))
            pmSelected = userList[currUser].pmList[pmSelectedIndex]
            #FIXME: need to validate input

            #check if this payment method has categories view
            if(len(pmSelected.categoryList) == 0):
                print("\nYou must first create categories for this payment method.")
                print(stars + "\n")
            else:
                print("\nCategories for this payment method:")
                for i in range(len(pmSelected.categoryList)):
                    print("Enter " + str(i) + " for: " + pmSelected.categoryList[i].name)

                #FIXME: need to add feature that lets you see transactions of all categories
                catSelectedIndex = int(input("\nWhich category would you like to view the transactions of? "))
                catSelected = pmSelected.categoryList[catSelectedIndex]

                if(len(catSelected.catTransList) == 0):
                    print("\nYou must first add transactions before you can view them.")
                    print(stars + "\n")
                else:
                    print("TRANSACTIONS\n")
                    for i in catSelected.catTransList:
                        i.printTrans()
                        print()

                    print(stars + "\n")



    if(selection == "8"):
        print("this selection is not working yet\n" + stars + "\n")

#QUESTIONS
#Is python the right language for iOS dev?
#Do I need setters and getters for variables?
#Do I need to make variables private?

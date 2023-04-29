import time


def infocustomer():
    userinfo = {"Ahmet": 0, "Zeynep": 0}
    return userinfo


amountbanks = infocustomer()


def entry():
    print("--- Welcome to MUBU Bank V.0.1 ---")
    print("1. Login \n2. Exit")
    userchoice = input(">>>")
    while True:
        if userchoice == "1":
            loginuser()
            services()
            break
        if userchoice == "2":
            print("Exited")
            break
        else:
            userchoice = input("Please enter valid number")


def loginuser():
    global username
    complete = False
    user = {"Ahmet": "1234", "Zeynep": "4321"}

    while not complete:
        username = input("Username:")
        password = input("Password:")

        if not username in user:  # check to see if user does not exists
            print("Input username again!")
            continue
        if password == user[username]:  # check to see if password match
            print(" Welcome", username, "!")
            complete = True
        else:
            print("Input password again")


def services():
    print("Please enter the number of the service:")
    print("1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Logout")
    num = int(input(">>>"))
    while True:
        if num == 1:
            WithdrawMoney()
            break
        if num == 2:
            DepositMoney()
            break
        if num == 3:
            TransferMoney()
            break
        if num == 4:
            AccountInformation()
            break
        if num == 5:
            Logout()
            break
        else:
            num = int(input("Please enter valid number"))


def WithdrawMoney():
    withdrawn = int(input("Please enter the amount you want to withdraw:"))
    if amountbanks[username] >= withdrawn:
        amountbanks[username] -= withdrawn
        print(f"{withdrawn} TL withdrawn from your account\nGoing back to main menu...")
        services()
    else:
        print(f"you don't have {withdrawn} TL in your account\nGoing back to main menu...")
        services()


def DepositMoney():
    deposit = int(input("Please enter the amount you want to drop:"))
    amountbanks[username] += deposit
    print(f"{deposit} TL added to your account\nGoing back to main menu...")
    services()


def TransferMoney():
    transferred = int(input("Please enter the amount you want to transfer:"))
    if amountbanks[username] >= transferred:
        amountbanks[username] -= transferred

        #########################################
        # user_transfer = ""
        # users = infocustomer()
        # for i in users:
        #    if i != username:
        #        user_transfer = i

        # amountbanks[user_transfer] += transferred
        #########################################

        # user_transfer = input("To who you want to transfer")
        # amountbanks[user_transfer] += transferred

        print(f"Money transferred successuffly!\nGoing back to main menu...")
        services()
    else:
        print("Sorry!, you don't have the entered amount\nGoing back to main menu...")
        print("1. Go back to main menu\n2. Transfer again")
        num = int(input(">>>"))
        while True:
            if num == 1:
                services()
                break
            if num == 2:
                TransferMoney()
                break
            else:
                num = input("Please enter valid number")


def AccountInformation():
    user = {"Ahmet": "1234", "Zeynep": "4321"}
    print(f"------- MUBU Bank -------\n{time.asctime()}\n----------------------------")
    print(f"Your Name:{username}\nYour Password:{user[username]}\nYour Amount(TL): {amountbanks[username]}")
    print("Going back to main menu...")
    services()


def Logout():
    print(f"Good Bye {username} !")
    entry()


entry()





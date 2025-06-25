#User Made functions
def createAccount(name,balence,accounts):
    accounts[name] = balence 

def closeAccount(name,accounts):
    if name in accounts.keys():
        accounts.pop(name) 
    else:
        print("Invalid account") 

def withdraw(name,amount,accounts):
    if name in accounts.keys():
        accounts[name] = accounts[name] - amount
    else:
        print("Invalid account") 

def deposit(name,amount,accounts):
    if name in accounts.keys():
        accounts[name] = accounts[name] + amount
    else:
        print("Invalid account") 

def transfer(account_1,account_2,amount,accounts):
    if account_1 in accounts.keys() and account_2 in accounts.keys():
        withdraw(account_1,amount,accounts)
        deposit(account_2,amount,accounts) 
    else:
        print("One of those accounts is not valid.")


#Program
def main():
    accounts = {"John Pork":500}
    check = True
    while check == True:
        print("Welcome to the bank!")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Transfer")
        print("6. Quit")
        option = int(input("Enter the number of your option from the list above: "))
        if option == 1:
            accountname = input("Enter the name of your account: ")
            balence = float(input("Enter the account balence: "))
            createAccount(accountname,balence,accounts)
            print(accounts) 
        elif option == 2:
            accountname = input("Enter the name of the account you would like to close: ")
            closeAccount(accountname,accounts) 
            print(accounts) 
        elif option == 3:
            accountname = input("Enter the name of your account: ")
            amount = float(input("Enter the amount you would like to withdraw: "))
            withdraw(accountname,amount,accounts) 
            print(accounts) 
        elif option == 4:
            accountname = input("Enter the name of your account: ")
            amount = float(input("Enter the amount you would like to deposit: "))
            deposit(accountname,amount,accounts) 
        elif option == 5:
            account_1 = input("Enter the name of the account you wish to transfer from: ")
            account_2 = input("Enter the name of the account you would like to transfer to: ")
            amount = float(input("Enter the amount you would like to transfer: "))
            transfer(account_1,account_2,amount,accounts)
            print(accounts) 
        elif option == 6:
            print("Thanks for visiting!")
            check = False

main() 
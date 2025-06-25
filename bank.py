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
        if amount > accounts[name]:
            print("amount excedes account balence.")
            return False 
        else:
            accounts[name] = accounts[name] - amount
            return True 
    else:
        print("Invalid account") 
        return False 

def deposit(name,amount,accounts):
    if name in accounts.keys():
        accounts[name] = accounts[name] + amount
    else:
        print("Invalid account") 

def transfer(account_1,account_2,amount,accounts):
    if account_1 in accounts.keys() and account_2 in accounts.keys():
        if withdraw(account_1,amount,accounts) == True:
            deposit(account_2,amount,accounts) 
        else:
            print("Invalid amount")
    else:
        print("One of those accounts is not valid.")

def printAccounts(accounts):
    for name in accounts: 
        print(f"Account name: {name}, account balence: {accounts[name]}") 


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
        option = (input("Enter the number of your option from the list above: "))
        if option.isnumeric() == True: 
            if int(option) == 1:
                accountname = input("Enter the name of your account: ").strip()
                balence = float(input("Enter the account balence: "))
                createAccount(accountname,balence,accounts)
                printAccounts(accounts) 
            elif int(option) == 2:
                accountname = input("Enter the name of the account you would like to close: ").strip()
                closeAccount(accountname,accounts) 
                printAccounts(accounts) 
            elif int(option) == 3:
                accountname = input("Enter the name of your account: ").strip()
                amount = float(input("Enter the amount you would like to withdraw: "))
                withdraw(accountname,amount,accounts) 
                printAccounts(accounts) 
            elif int(option) == 4:
                accountname = input("Enter the name of your account: ").strip()
                amount = float(input("Enter the amount you would like to deposit: "))
                deposit(accountname,amount,accounts) 
                printAccounts(accounts)
            elif int(option) == 5:
                account_1 = input("Enter the name of the account you wish to transfer from: ").strip()
                account_2 = input("Enter the name of the account you would like to transfer to: ").strip()
                amount = float(input("Enter the amount you would like to transfer: "))
                transfer(account_1,account_2,amount,accounts)
                printAccounts(accounts) 
            elif int(option) == 6:
                print("Thanks for visiting!")
                check = False
        else:
            print("Invalid input")

main() 
def showBalance(balance):
    print(f"Your Balace is {balance:.2f} rupees")
def deposit():
    amount=int(input("Enter how many rupee you want to deposit: "))
    if amount<0:
        print(f"{amount} that is not a valid amount")
        return 0
    else:
        print(f"sucessfully deposit {amount} rupee")
        return amount
def withdraw(balance):
    amount=float(input("Enter amount to withdraw:"))
    if amount>balance:
        print("insufficient amount:")
    elif amount<0:
        print("invalid amount")
    else:
        print(f"sucessfully withdraw {amount} rupee")
        return amount
def main():
    balance = 0
    isRunning=True
    while(isRunning):
        print("_______Welcome in Banking program_________")
        print("1. Show Balanace")
        print("2. Deposit")
        print("3. withdraw")
        print("4. exit")

        choice = input("Enter your choice (1-4): ")
        if choice=='1':
            showBalance(balance)
        elif choice=='2':
            balance+=deposit()
        elif choice == '3':
            balance-=withdraw(balance)
        elif choice == '4':
            isRunning=False
        else:
            print("!that's not valid, Enter valid value 1-4: ")
    print("Thank yoy! Have a nice day sir! ")
if __name__=='__main__':
    main()
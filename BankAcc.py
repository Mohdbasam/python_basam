class BankAcc:
    Bank_name = "State bank of india"
    Branch = "Calicut"
    def __init__(self,name,num,acctype,bal):
        self.name = name
        self.account_number = num
        self.account_type = acctype
        self.balance = bal
    def display(self):
        print(__class__.Bank_name)
        print(__class__.Branch)
        print("Name : ",self.name)
        print("Acc No. : ",self.account_number)
        print("Acc type : ",self.account_type)
        print("Balance : ",self.balance)
        print("\n")
    def deposit(self):
        a = int(input("Enter the amount to deposit : "))
        self.balance+=a
        print(f"Amount after deposit is {self.balance} : ")
    def withdraw(self):
        print(self.balance)
        b = int(input("Enter the amount to widthraw : "))
        if b < self.balance:
            print(f"{b} has been withdrew")
            self.balance-=b
            print(f"current balance is : {self.balance}")
        else:
            print(f"Account balance is low pls enter a amount lower than {self.balance}")
    def option(self):
        while True:
            opt= int(input("1.Deposit \n2.Withdraw\n3.Exit\nEnter your choice : "))
            if opt == 1:
                    self.deposit()
                    break
            elif opt == 2:
                    self.withdraw()
                    break
            else :
                        print("Exiting..!")
                        break
while True:

    pin = int(input("Enter your pin number : "))

    if pin == 1020:
        customer1 = BankAcc("asif", 85236144514, "savings", 500)
        customer1.display()
        customer1.option()


    elif pin == 2040:
        customer2 = BankAcc("Basam", 56489456146, "savings", 1000)
        customer2.display()
        customer2.option()

    elif pin == 3060:
        customer3 = BankAcc("Aseeb", 446446456, "savings", 10000)
        customer3.display()
        customer3.option()

    elif pin == 4080:
        customer4 = BankAcc("Sinu sangeeth", 916916158156, "current acc", 0)
        customer4.display()
        customer4.option()

    elif pin == 5090:
        customer5 = BankAcc("safwan", 986547455236, "savings", 102)
        customer5.display()
        customer5.option()
    else:
        print("Enter correct pin")
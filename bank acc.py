from asyncore import ExitNow


class BankAcc:
    Bank_name = "State bank of india"
    Branch = "Calicut"
    def __init__(self,name,num,type,bal):
        self.name = name
        self.account_number = num
        self.account_type = type
        self.balance = bal
    def display(self):
        print(__class__.Bank_name)
        print(__class__.Branch)
        print(self.name)
        print(self.account_number)
        print(self.account_type)
        print(self.balance)
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
            elif opt == 2:
                    self.withdraw()
            else :
                        print("Exiting..!")
                        break

customer1 = BankAcc ("asif",85236144514,"savings",500)
customer1.display()
customer1.option()

customer2 = BankAcc ("Basam",56489456146,"savings",1000)
customer2.display()
customer2.option()

customer3 = BankAcc ("Aseeb",446446456,"savings",10000)
customer3.display()
customer3.option()

customer4 = BankAcc ("Sinu sangeeth",916916158156,"current acc",0)
customer4.display()
customer4.option()


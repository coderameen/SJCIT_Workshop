class BankManagementSystem:
    #constructor
    def __init__(self):
        self.acc_no = None
        self.acc_holder = None
        self.__balance = 0
        
    def add_newuser(self,acc_no,acc_holder,amount):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.__balance = amount
        print(f"{acc_holder} has been created successfully!!")
    
    #check balance of customer
    def check_balance(self,acc_no):
        if acc_no == self.acc_no:
            print(f"The Account holder is {self.acc_holder} | Balance is: {self.__balance}")
        else:
            print("Invalid Account Number!!")

    #credit the amount
    def credit_amount(self,acc_no,amount):
        if acc_no == self.acc_no:
            self.__balance += amount
            print(f"{amount} has been credited successfully")
        else:
            print("Invalid Acc no!!")
    
    def withdraw_amount(self,acc_no,amount):
        if acc_no == self.acc_no:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} has been withdraw successfully!!!")
            else:
                print("Insufficient Balance!!")
        else:
            print("Invaild Acc No.")
            
    def update_user(self,acc_no,new_user):
        if acc_no == self.acc_no:
            self.acc_holder = new_user
            print(f"{new_user} has been updated succussfully!!")
        else:
            print("Invalid Account Number!!")

c1 = BankManagementSystem()
c1.add_newuser('SBI01','Alen',1000)
c1.check_balance('SBI01')
c1.credit_amount('SBI01',500)
c1.check_balance('SBI01')
c1.withdraw_amount('SBI01',1300)
c1.check_balance('SBI01')
c1.update_user('SBI01','Alen Walker')
c1.check_balance('SBI01')

c2 = BankManagementSystem()
c2.add_newuser('SBI02','BOB',800)
c2.check_balance('SBI02')
c2.withdraw_amount('SBI02',700)
c2.check_balance('SBI02')
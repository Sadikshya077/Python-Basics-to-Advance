import random
from ErrorHandling import WithdrawAmountError, DepositAmountError
class Bank:
    def __init__(self,name,initial_balance,phone):
        self.name=name
        self.initial_balance=initial_balance
        self.phone=phone
        self.account_number=''.join(str(random.randint(0,9)) for i in range(16))

    def withdraw(self,withdraw):
        if withdraw<self.initial_balance:
            self.initial_balance=self.initial_balance-withdraw
            print(f'Balance withdrawn from A/C no. {self.account_number}')
        else:
            raise WithdrawAmountError('Error: Withdraw amount must be less than available balance.')
        
    def deposit(self,deposit):
        if deposit>100:
            self.initial_balance=self.initial_balance+deposit
            print(f'Balance deposited to A/C no. {self.account_number}')
        else:
            raise DepositAmountError('Error: Deposit amount must be greater than 100')
        
    def userDetails(self):
        print(f'Account Holder name:{self.name}')
        print(f'Account number: {self.account_number}')
        print(f'Initial Balance: {self.initial_balance}')
        print(f'Phone number: {self.phone}')
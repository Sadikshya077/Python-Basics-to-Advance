from Bank import Bank
from Storage import all_accounts 
from Functions import find_account
from ErrorHandling import WithdrawAmountError, DepositAmountError, AccountNotFoundError
def bankApp():
    while True:
        print('Welcome to the Banking App')
        print('1. Create Account\n2. Deposit Amount\n3. Withdraw Amount\n4. User Details\n5.Exit')
        choice =int(input('Enter your choice: '))
        if choice==1:
            print('Create Account')
            y_n=input('Do you really want to create account? (yes/no)')
            if y_n=='yes':
                name=input('Enter account holder name: ')
                initial_amount=float(input('Enter initial amount: '))
                phone=input('Enter phone number: ')   
            if initial_amount>100:
                b=Bank(name,initial_amount,phone)
                all_accounts.append(b)
                print(f'Account created with name {name} and account number {b.account_number}')  
            else:
                print('Continue with the transactions')
            
        elif choice==2:
            print('Deposit Amount')
            y_n=input('Do you really want to deposit amount? (yes/no)')
            if y_n=='yes':
                ac_no=input('Enter your account number')
                try:
                    find_acc=find_account(ac_no)
                    if find_acc:
                        balance=int(input('Enter the amount you want to deposit: '))
                        find_acc.deposit(balance)
                except AccountNotFoundError as ae:
                    print(ae)
                except DepositAmountError as de:
                    print(de)
                except ValueError:
                    print('Error: Only number values can be entered.')
                    
            else:
                print('Continue with the transactions')
                
        elif choice==3:
            print('Withdraw Amount')
            y_n=input('Do you really want to withdraw amount? (yes/no)')
            if y_n=='yes':
                ac_no=input('Enter your account number')
                try:
                    find_acc=find_account(ac_no)
                    if find_acc:
                        balance=int(input('Enter the amount you want to withdraw: '))
                        find_acc.withdraw(balance)
                except AccountNotFoundError as ae:
                    print(ae)
                except WithdrawAmountError as we:
                    print(we)
                except ValueError:
                    print('Error: Only number values can be entered.')
            else:
                print('Continue with the transactions')
        elif choice==4:
            print('User Details')
            y_n=input('Do you really want to see the user details? (yes/no)')
            if y_n=='yes':
                ac_no=input('Enter your account number')
                try:
                    find_acc=find_account(ac_no)
                    if find_acc:
                        find_acc.userDetails()
                except AccountNotFoundError as ae:
                    print(ae)
                except ValueError:
                    print('Error: Only number values can be entered.')
            else:
                print('Continue with the transactions')
        elif choice==5:
            print('Thank you for choosing us.')
            break
        else:
            print('Invalid input. Try Again!')
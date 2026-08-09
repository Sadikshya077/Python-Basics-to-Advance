from Storage import all_accounts
from ErrorHandling import AccountNotFoundError
def find_account(acc_number):
    for account in all_accounts:
        if account.account_number==acc_number:
            return account
        else:
            raise AccountNotFoundError('Error: Account not found')
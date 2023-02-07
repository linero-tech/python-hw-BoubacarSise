
def task9():
    return """"
    INPUT account_number, password, withdrawal_amount
    IF account_number AND password NOT FOUND in the database
    OUTPUT "Invalid account number or password."
    ELSE
    account_balance = retrieve_balance(account_number)
    IF withdrawal_amount > account_balance
    OUTPUT "Transaction failed. Insufficient funds."
    ELSE
    account_balance = account_balance - withdrawal_amount
    update_balance(account_number, account_balance)
    dispense_cash(withdrawal_amount)
    OUTPUT "Withdrawal successful. Your new balance is: " + account_balance
    """

from datetime import datetime

class Transaction:
    def __init__(self, date: str, amount: int):
        self.date = date
        self.amount = amount

class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def add_deposit(self, amount: int):
        self.transactions.append(Transaction(self.current_date(), amount))

    def add_withdrawal(self, amount: int):
        self.transactions.append(Transaction(self.current_date(), -amount))

    def all_transactions(self):
        return self.transactions

    def current_date(self):
        return datetime.now().strftime("%d-%m-%Y")

class StatementPrinter:
    def print(self, transactions):
        print("DATE | AMOUNT | BALANCE")
        balance = 0
        for transaction in transactions:
            balance += transaction.amount
            print(f"{transaction.date} || {transaction.amount} || {balance}")

class Account:
    def __init__(self, transaction_repository: TransactionRepository, statement_printer: StatementPrinter):
        self.transaction_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self, amount: int):
        self.transaction_repository.add_deposit(amount)

    def withdraw(self, amount: int):
        self.transaction_repository.add_withdrawal(amount)

    def print_statement(self):
        self.statement_printer.print(self.transaction_repository.all_transactions())

if __name__ == "__main__":
    account = Account(TransactionRepository(), StatementPrinter())
    account.deposit(1000)
    account.deposit(2000)
    account.withdraw(500)
    account.print_statement()

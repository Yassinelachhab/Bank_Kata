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
        statement_lines = []
        for transaction in transactions:
            balance += transaction.amount
            statement_lines.append(f"{transaction.date} | {transaction.amount} | {balance}")
        for line in reversed(statement_lines):
            print(line)

class Account:
    def __init__(self, transaction_repository: TransactionRepository, statement_printer: StatementPrinter):
        self.transaction_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        self.transaction_repository.add_deposit(amount)

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        self.transaction_repository.add_withdrawal(amount)

    def print_statement(self):
        self.statement_printer.print(self.transaction_repository.all_transactions())

if __name__ == "__main__":
    account = Account(TransactionRepository(), StatementPrinter())
    
    while True:
        action = input("Enter 'd' to deposit, 'w' to withdraw, 's' to show statement, or 'q' to quit: ").strip().lower()
        if action == 'd':
            account.deposit()
        elif action == 'w':
            account.withdraw()
        elif action == 's':
            account.print_statement()
        elif action == 'q':
            break
        else:
            print("Invalid input. Please try again.")
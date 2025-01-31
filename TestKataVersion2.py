from abc import ABC, abstractmethod
from datetime import datetime

class AccountService(ABC):
    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod
    def withdraw(self, amount: int):
        pass

    @abstractmethod
    def print_statement(self):
        pass

class Transaction:
    def __init__(self, date: str, amount: int):
        self.date = date
        self.amount = amount

class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount: int):
        self.transactions.append(Transaction(self.current_date(), amount))

    def get_all_transactions(self):
        return self.transactions

    def current_date(self):
        return datetime.now().strftime("%d-%m-%Y")

class StatementPrinter:
    def print_statement(self, transactions):
        print("DATE | AMOUNT | BALANCE")
        balance = 0
        statement_lines = []
        for transaction in transactions:
            balance += transaction.amount
            statement_lines.append(f"{transaction.date} | {transaction.amount} | {balance}")
        for line in reversed(statement_lines):
            print(line)

class BankAccount(AccountService):
    def __init__(self, transaction_repository: TransactionRepository, statement_printer: StatementPrinter):
        self.transaction_repository = transaction_repository
        self.statement_printer = statement_printer

    def deposit(self, amount: int):
        self.transaction_repository.add_transaction(amount)

    def withdraw(self, amount: int):
        self.transaction_repository.add_transaction(-amount)

    def print_statement(self):
        self.statement_printer.print_statement(self.transaction_repository.get_all_transactions())

# Exemple d'utilisation
if __name__ == "__main__":
    account = BankAccount(TransactionRepository(), StatementPrinter())

    while True:
        action = input("Entrer 'd' pour déposer, 'w' pour retirer, 's' pour afficher le relevé ou 'q' pour quitter : ").strip().lower()
        if action == 'd':
            amount = int(input("Entrez le montant à déposer : "))
            account.deposit(amount)
        elif action == 'w':
            amount = int(input("Entrez le montant à retirer : "))
            account.withdraw(amount)
        elif action == 's':
            account.print_statement()
        elif action == 'q':
            break
        else:
            print("Entrée invalide. Veuillez réessayer.")
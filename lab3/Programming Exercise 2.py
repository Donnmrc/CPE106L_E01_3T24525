class SavingsAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __lt__(self, other):
        if isinstance(other, SavingsAccount):
            return self.name < other.name
        return NotImplemented

    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        sorted_accounts = sorted(self.accounts)
        return "\n".join(str(account) for account in sorted_accounts)

def main():
    bank = Bank()
    bank.add_account(SavingsAccount("Charlie", 1500))
    bank.add_account(SavingsAccount("Alice", 2400))
    bank.add_account(SavingsAccount("Bob", 1200))

    print("Accounts sorted by name:")
    print(bank)

if __name__ == "__main__":
    main()

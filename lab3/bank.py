class SavingsAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def __str__(self):
        sorted_accounts = sorted(self.accounts)  # Sorts using __lt__ from SavingsAccount
        return "\n".join(str(account) for account in sorted_accounts)


def main():
    bank = Bank()

    # Adding accounts to the bank, adding our names as well
    bank.addAccount(SavingsAccount("Charlie", 2500))
    bank.addAccount(SavingsAccount("Alice", 1500))
    bank.addAccount(SavingsAccount("Bob", 2000))
    bank.addAccount(SavingsAccount("Donn", 3000))
    bank.addAccount(SavingsAccount("Andrew", 23))

    print("Accounts sorted by name:")
    print(bank)


if __name__ == "__main__":
    main()

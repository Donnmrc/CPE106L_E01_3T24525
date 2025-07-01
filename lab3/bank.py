from savingsaccount import SavingsAccount

class Bank:
    """A simple bank holding multiple savings accounts."""

    def __init__(self):
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def __str__(self):
        # Sort accounts by name using __lt__ in SavingsAccount
        sorted_accounts = sorted(self.accounts)
        return "\n\n".join(str(account) for account in sorted_accounts)


def main():
    # Sample accounts, we added our names too
    acc1 = SavingsAccount("Charlie", "1234", 1000.00)
    acc2 = SavingsAccount("Alice", "5678", 2500.00)
    acc3 = SavingsAccount("Bob", "4321", 1500.00)
    acc4 = SavingsAccount("Andrew", "6000", 23.00)
    acc5 = SavingsAccount("Donn", "9999", 3000.00)

    # Create a bank and add accounts
    bank = Bank()
    bank.addAccount(acc1)
    bank.addAccount(acc2)
    bank.addAccount(acc3)
    bank.addAccount(acc4)
    bank.addAccount(acc5)

    # Display sorted accounts
    print("Accounts sorted by name:\n")
    print(bank)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()


# ---------------------------------------------
# Bank Account Class Program
# ---------------------------------------------
# This program creates a BankAcct class that stores
# name, account number, amount, and interest rate.
# It includes methods for deposits, withdrawals,
# adjusting interest, calculating interest by days,
# and displaying account info using __str__.
# A test function is included to demonstrate usage.
# ---------------------------------------------


class BankAcct:
    """A simple bank account class with interest calculations."""

    def __init__(self, name, acct_num, amount, interest_rate):
        # State information
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.interest_rate = interest_rate  # annual interest rate as decimal

    # -----------------------------
    # Adjust interest rate
    # -----------------------------
    def adjust_interest(self, new_rate):
        """Updates the interest rate."""
        self.interest_rate = new_rate

    # -----------------------------
    # Deposit money
    # -----------------------------
    def deposit(self, amount):
        """Adds money to the account."""
        self.amount += amount

    # -----------------------------
    # Withdraw money
    # -----------------------------
    def withdraw(self, amount):
        """Withdraws money if funds are available."""
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds for withdrawal.")

    # -----------------------------
    # Get balance
    # -----------------------------
    def get_balance(self):
        """Returns the current balance."""
        return self.amount

    # -----------------------------
    # Calculate interest for X days
    # -----------------------------
    def calc_interest(self, days):
        """Calculates interest earned over a number of days."""
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

    # -----------------------------
    # String representation
    # -----------------------------
    def __str__(self):
        """Returns formatted account information."""
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:,.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%\n")


# ---------------------------------------------
# Test Function
# ---------------------------------------------
def test_bank_acct():
    """Tests all methods of the BankAcct class."""

    # Create an account
    acct = BankAcct("Shelia Foxx", 123456, 1000.00, 0.05)

    print("Initial Account Info:")
    print(acct)

    # Test deposit
    acct.deposit(500)
    print("After depositing $500:")
    print(acct)

    # Test withdrawal
    acct.withdraw(200)
    print("After withdrawing $200:")
    print(acct)

    # Test interest adjustment
    acct.adjust_interest(0.07)
    print("After adjusting interest rate to 7%:")
    print(acct)

    # Test interest calculation
    interest_30 = acct.calc_interest(30)
    print(f"Interest earned in 30 days: ${interest_30:,.2f}")

    # Final balance display
    print("Final Account Summary:")
    print(acct)


# ---------------------------------------------
# Run test function
# ---------------------------------------------
test_bank_acct()

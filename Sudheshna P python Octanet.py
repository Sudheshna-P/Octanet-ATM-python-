class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.account = Account()

class CheckBalance:
    @staticmethod
    def display_balance(account):
        print(f"Account Balance: ₹{account.get_balance()}")

class Account:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -₹{amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer to {recipient.user_id}: -₹{amount}")
            recipient.transaction_history.append(f"Transfer from {self.user_id}: +₹{amount}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

class Transaction:
    @staticmethod
    def display_transaction_history(account):
        transactions = account.get_transaction_history()
        if not transactions:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in transactions:
                print(transaction)

class ATM:
    @staticmethod
    def start(user):
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")

        if user_id == user.user_id and pin == user.pin:
            print("Login successful!\n")
            ATM.show_menu(user)
        else:
            print("Invalid credentials. Exiting.")

    @staticmethod
    def show_menu(user):
        while True:
            print("\nATM Menu:")
            print("1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Check Balance")
            print("6. Quit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                Transaction.display_transaction_history(user.account)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: ₹"))
                user.account.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter deposit amount: ₹"))
                user.account.deposit(amount)
            elif choice == '4':
                recipient_id = input("Enter recipient's User ID: ")
                recipient = users.get(recipient_id)
                if recipient:
                    amount = float(input("Enter transfer amount: ₹"))
                    user.account.transfer(recipient.account, amount)
                else:
                    print("Recipient not found.")
            elif choice == '5':
                CheckBalance.display_balance(user.account)
            elif choice == '6':
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

# Main function
def main():
    # Creating users for testing
    user1 = User("123456", "7890")
    user2 = User("987654", "0123")

    # Storing users in a dictionary for quick lookup
    global users
    users = {user1.user_id: user1, user2.user_id: user2}

    # Starting the ATM application
    ATM.start(user1)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

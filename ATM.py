class ATM:
    def __init__(self):
        self.users = {}

    def create_account(self):
        print("\n--- Create Account ---")
        name = input("Enter your name: ")
        pin = input("Set your 4-digit PIN: ")
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN. Please try again.")
            return
        self.users[pin] = {"name": name, "balance": 0.0}
        print(f"Account successfully created for {name}!")

    def authenticate(self):
        print("\n--- Authenticate ---")
        pin = input("Enter your 4-digit PIN: ")
        if pin in self.users:
            return pin
        else:
            print("Invalid PIN. Please try again.")
            return None

    def deposit(self, pin):
        print("\n--- Deposit Money ---")
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.users[pin]["balance"] += amount
            print(f"Deposited ₹{amount:.2f}. Current balance: ₹{self.users[pin]['balance']:.2f}")
        else:
            print("Invalid amount. Please try again.")

    def withdraw(self, pin):
        print("\n--- Withdraw Money ---")
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= self.users[pin]["balance"]:
            self.users[pin]["balance"] -= amount
            print(f"Withdrew ₹{amount:.2f}. Current balance: ₹{self.users[pin]['balance']:.2f}")
        else:
            print("Invalid amount or insufficient balance. Please try again.")

    def check_balance(self, pin):
        print("\n--- Check Balance ---")
        balance = self.users[pin]["balance"]
        print(f"Your current balance is: ₹{balance:.2f}")

    def menu(self):
        while True:
            print("\n--- Welcome to ATM ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_account()
            elif choice == "2":
                pin = self.authenticate()
                if pin:
                    while True:
                        print("\n--- ATM Menu ---")
                        print("1. Deposit Money")
                        print("2. Withdraw Money")
                        print("3. Check Balance")
                        print("4. Logout")
                        sub_choice = input("Enter your choice: ")

                        if sub_choice == "1":
                            self.deposit(pin)
                        elif sub_choice == "2":
                            self.withdraw(pin)
                        elif sub_choice == "3":
                            self.check_balance(pin)
                        elif sub_choice == "4":
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    atm.menu()

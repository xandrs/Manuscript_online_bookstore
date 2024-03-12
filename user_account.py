class UserAccount:
    def __init__(self, username, password, email, initial_balance=0):
        self.username = username
        self.password = password
        self.email = email
        self.balance = initial_balance
        self.amount = 0  # Initialize amount attribute
        self.total_spent = 0  # Initialize total_spent attribute to 0

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def deposit_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposit of 💲{amount:.2f} successful. Current balance: 💲{self.balance:.2f}")
        else:
            print("❌ Invalid amount. Please enter a positive value.")

    def get_balance(self):
        return self.balance
    
    def deduct_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_spent += amount  # Update total_spent
            return True
        else:
            return False

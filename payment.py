class Payment:
    def process_payment(self, user_account, total_price):
        if user_account.deduct_amount(total_price):
            print(f"✅ Payment processed successfully! Remaining balance: 💲{user_account.balance:.2f}")
        else:
            print("Insufficient funds. Payment failed ❌")

class Order:
    def __init__(self, user, books):
        self.user = user
        self.books = books

    def generate_order_summary(self):
        summary = "😀 Order Summary:\n"
        summary += f"User: {self.user.user_account.username}\n"
        summary += "📗 Books:\n"
        for book in self.books:
            summary += f"📍 {book.title} (💲{book.price:.2f})\n"
        # total_price = sum(book.price for book in self.books)
        # summary += f"Total Price: 💲{total_price:.2f}"
        return summary

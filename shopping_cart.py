class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, book):
        self.items.append(book)

    def remove_from_cart(self, book):
        if book in self.items:
            self.items.remove(book)
        else:
            print("Book not found in the cart 🚫.")

    def view_cart(self):
        if self.items:
            print("Items in the cart ⬇️")
            for item in self.items:
                print("📍", item)
        else:
            print("Your cart is empty 🗑️")

    def checkout(self):
        total_price = sum(book.price for book in self.items)
        print(f"Total price: 💲{total_price:.2f}")
        self.items = []
        print("Thank you for your purchase! 🙏")

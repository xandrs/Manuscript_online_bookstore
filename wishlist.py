class Wishlist:
    def __init__(self):
        self.items = []

    def add_to_wishlist(self, book):
        self.items.append(book)
        print(f"{book.title} added to wishlist 💚")

    def remove_from_wishlist(self, book):
        if book in self.items:
            self.items.remove(book)
            print(f"{book.title} removed from wishlist 💔")
        else:
            print("Book not found in the wishlist ❗️")

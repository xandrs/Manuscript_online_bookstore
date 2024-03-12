class Book:
    def __init__(self, title, author, price, isbn):
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn

    def __str__(self):
        return f"💲{self.price} 📌{self.title} by {self.author}"
    
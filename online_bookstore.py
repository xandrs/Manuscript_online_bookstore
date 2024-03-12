class OnlineBookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} has been added to the store ➕.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} has been removed from the store ❌")
        else:
            print("Book not found in the store ❗️")

    def display_books(self):
        print("Books available in the store ⬇️ ⬇️ ⬇️")
        for book in self.books:
            print("📗", book)

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                print("📗", book)

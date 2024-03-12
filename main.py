from online_bookstore import OnlineBookStore
from user_account import UserAccount
from user import User
from book import Book
from order import Order
from review import Review
from payment import Payment


def login():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")
    return username, password

def main():
    bookstore = OnlineBookStore()

    # Adding books to the store
    print("\n***   BookStore:       © MANUSCRIPT 📚  ***\n")
    print("Available books:")
    book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 11.99, "978-0747532743")
    book2 = Book("The Da Vinci Code", "Dan Brown", 10.99, "978-0307474278")
    book3 = Book("The Lord of the Rings", "J.R.R. Tolkien", 16.49, "978-0544003415")
    book4 = Book("Python Crash Course", "Eric Matthes", 20.25, "978-1718502703")
    book5 = Book("OOAD", "Edwin Mach", 29.01, "978-1670943163")
    bookstore.add_book(book1)
    bookstore.add_book(book2)
    bookstore.add_book(book3)
    bookstore.add_book(book4)
    bookstore.add_book(book5)

    while True:
        username, password = login()
        # user_account is the instance of the UserAccount class. 
        # It's created using UserAccount("tom", "tom123", "tomn@email.com").
        # This instance is then passed to the User class constructor when creating a new User object.
        user_account = UserAccount("tom", "tom123", "tomn@email.com") 
        # user_account = UserAccount(username, password, f"{username}@example.com")
        if user_account.authenticate(username, password):
            user = User(user_account)
            print("✅ Login successful!")
            break
        else:
            print("❌ Invalid username or password. Please try again.")

    # Deposit funds
    while True:
        try:
            deposit_amount = float(input("Enter the amount you want to deposit 💰: "))
            user_account.deposit_funds(deposit_amount)
            break
        except ValueError:
            print("❗️ Invalid input. Please enter a valid amount.")
    
    payment_processor = Payment()
    
    while True:
        print("\n*********__MENU Options__🖌️_*********\n")
        print("1. Display available books")
        print("2. Search for a book")
        print("3. Add book to cart")
        print("4. Remove book from cart")
        print("5. View cart")
        print("6. Checkout")
        print("7. Write a review")
        print("8. Add book to wishlist")
        print("9. Enter home address")
        print("10. Select shipping method")
        print("11. Exit")
        print("\n*************__FOOTER__*************\n")

        choice = input("Enter your choice: 👉 ")

        if choice == "1":
            bookstore.display_books()

        elif choice == "2":
            title = input("Enter the title of the book you want to search for: ")
            bookstore.search_book(title)

        elif choice == "3":
            title = input("Enter the title of the book you want to add to the 🛒: ")
            for book in bookstore.books:
                if title.lower() in book.title.lower():
                    user.shopping_cart.add_to_cart(book)
                    print(f"{book.title} added to the 🛒.")
                    break
            else:
                print("Book not found in the store 🔴")

        elif choice == "4":
            title = input("Enter the title of the book you want to remove from the cart: ")
            for book in user.shopping_cart.items:
                if title.lower() in book.title.lower():
                    user.shopping_cart.remove_from_cart(book)
                    print(f"{book.title} removed from cart 🚫")
                    break
            else:
                print("Book not found in the cart 🔴")

        elif choice == "5":
            user.shopping_cart.view_cart()

        elif choice == "6":
            total_price = sum(book.price for book in user.shopping_cart.items)
            if total_price > 0:
                order = Order(user, user.shopping_cart.items)
                order_summary = order.generate_order_summary()
                print(order_summary)
                user.shopping_cart.checkout()
                payment_processor.process_payment(user.user_account, total_price)
            else:
                print("Your cart is empty 🗑️\n Please add items to proceed with checkout.")

        elif choice == "7":
            review_book_title = input("Enter the title of the book you want to review: ")
            for book in bookstore.books:
                if review_book_title.lower() in book.title.lower():
                    rating = int(input("Enter your rating (1-5): "))
                    comment = input("Enter your comment 🖊️: ")
                    review = Review(user.user_account.username, book.title, rating, comment)
                    print("Review submitted successfully ✅")
                    break
            else:
                print("Book not found in the store 🔴")
        
        elif choice == "8":
            wishlist_book_title = input("Enter the title of the book you want to add to the wishlist 💚: ")
            for book in bookstore.books:
                if wishlist_book_title.lower() in book.title.lower():
                    # user.shopping_cart.add_to_wishlist(book)
                    user.add_to_wishlist(book)  # Call the method on the user instance
                    print(f"✅ {book.title} added to wishlist.")
                    break
            else:
                print("Book not found in the store 🔴")
        
        elif choice == "9":
            address = input("Enter your home address: 🏠")
            user.shipping_info.enter_address(address)
            print("Home address saved successfully 🟢")

        elif choice == "10":
            print("Select a shipping method:")
            print("1. Standard Shipping 🐌")
            print("2. Express Shipping 🚀")
            shipping_choice = input("Enter your choice: ")
            if shipping_choice == "1":
                user.shipping_info.select_shipping_method("Standard Shipping")
                print("Standard Shipping selected 🐌")
            elif shipping_choice == "2":
                user.shipping_info.select_shipping_method("Express Shipping")
                print("Express Shipping selected 🚀")
            else:
                print("🔴 Invalid choice. Please enter 1 or 2.")
        
        elif choice == "11":
            print("Exiting program 🖐️")
            break

        else:
            print("⛔️ Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()

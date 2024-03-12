from wishlist import Wishlist
from shipping import Shipping
from shopping_cart import ShoppingCart


class User:
    def __init__(self, user_account):
        self.user_account = user_account
        self.shopping_cart = ShoppingCart()
        self.wishlist = Wishlist()  # Add wishlist attribute to the User class
        self.shipping_info = Shipping() # Add shipping_info attribute to the User class

    def add_to_wishlist(self, book):
        self.wishlist.add_to_wishlist(book)

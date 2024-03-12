class Shipping:
    def __init__(self):
        self.address = None
        self.shipping_method = None

    def enter_address(self, address):
        self.address = address

    def select_shipping_method(self, method):
        self.shipping_method = method

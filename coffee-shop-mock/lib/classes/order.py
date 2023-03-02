
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.add_order_to_all(self)

    @classmethod
    def add_order_to_all(cls, order):
        cls.all.append(order)

    def get_customer(self):
        return self._customer

    def set_customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer

    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee

    def set_coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    coffee = property(get_coffee, set_coffee)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if isinstance(price, (int, float,)) and (1 <= price <= 10):
            self._price = price

    price = property(get_price, set_price)

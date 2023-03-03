
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.price = price
        self.customer = customer
        self.coffee = coffee
        Order.all.append(self)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price = price

    price = property(get_price, set_price)

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
        from classes.coffee import Coffee  # import Coffee class from the coffee.py file
        # checking to make sure coffee is an instance of the Coffee class
        if isinstance(coffee, Coffee):
            # assign _coffee private attribute to the coffee object/coffee instance
            self._coffee = coffee

    coffee = property(get_coffee, set_coffee)

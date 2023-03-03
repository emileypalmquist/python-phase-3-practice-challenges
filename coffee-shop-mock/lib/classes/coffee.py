from classes.order import Order


class Coffee:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not hasattr(self, "_name") and isinstance(name, str):
            self._name = name

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        coffees_customers = []
        for order in self.orders():
            if not order.customer in coffees_customers:
                coffees_customers.append(order.customer)
        return coffees_customers

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / self.num_orders()

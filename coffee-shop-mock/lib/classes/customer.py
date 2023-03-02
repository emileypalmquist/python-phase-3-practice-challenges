from classes.order import Order


class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15):
            self._name = name

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        unique_coffees = []
        for order in self.orders():
            if not order.coffee in unique_coffees:
                unique_coffees.append(order.coffee)

        return unique_coffees

    def create_order(self, coffee, price):
        Order(self, coffee, price)

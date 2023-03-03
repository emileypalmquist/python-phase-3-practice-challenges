from classes.order import Order


class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("not a string or not a valid length")

    name = property(get_name, set_name)

    def orders(self):
        customers_orders = []
        for order in Order.all:
            if order.customer == self:
                customers_orders.append(order)
        return customers_orders

        # [order for order in Order.all if order.customer == self]

    def coffees(self):
        customers_coffees = []
        for order in self.orders():
            if not order.coffee in customers_coffees:
                customers_coffees.append(order.coffee)
        return customers_coffees

    def create_order(self, coffee, price):
        Order(self, coffee, price)

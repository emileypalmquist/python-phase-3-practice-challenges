#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    emiley = Customer("Emiley")
    flat_white = Coffee("Flat White")
    mocha = Coffee("Mocha")

    order_1 = Order(emiley, flat_white, 5)
    order_2 = Order(emiley, flat_white, 5)
    order_3 = Order(emiley, mocha, 5)

    ipdb.set_trace()

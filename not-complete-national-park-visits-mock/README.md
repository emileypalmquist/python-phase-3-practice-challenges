# Object Relations Code Challenge - National Park Visits

For this assignment, we'll be working with a national park planner-style domain.

We have three models: `NationalPark`, `Visitor`, and `Trip`.

For our purposes, a `NationalPark` has many `Trip`s, a `Visitor` has many
`Trip`s, and a `Trip` belongs to a `Visitor` and to a `NationalPark`.

`NationalPark` - `Visitor` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Visitor

- `Visitor __init__(self, name)`
  - Visitor should be initialized with a name
- `Visitor property name`
  - Return name
  - Names must be of type `str`
  - Names must be between 1 and 15 characters, inclusive

#### NationalPark

- `NationalPark __init__(self, name)`
  - NationalParks should be initialized with a name, as a string
- `NationalPark property name`
  - Returns the NationalPark's name
  - Should not be able to change after the NationalPark is created
  - hint: hasattr()

#### Trip

- `Trip __init__(self, visitor, national_park, start_date, end_date)`
  - Trips should be initialized with a visitor, national_park, start_date, end_date (a number)
- `Trip property price`
  - Returns the price for a coffee
  - Price must be a number between 1 and 10, inclusive

### Object Relationship Methods and Properties

#### Order

- `Order property customer`
  - Returns the customer object for that order
  - Must be of type `Customer`
- `Order property coffee`
  - Returns the coffee object for that order
  - Must be of type `Coffee`

#### Coffee

- `Coffee orders()`
  - Returns a list of all orders for that coffee
  - orders must be of type `Order`
- `Coffee customers()`
  - Returns a **unique** list of all customers who have ordered a particular coffee.
  - Customers must be of type `Customer`

#### Customer

- `Customer orders()`
  - Returns a list of all orders a customer has ordered
  - orders must be of type `Order`
- `Customer coffees()`
  - Returns a **unique** list of all coffees a customer has ordered
  - Coffees must be of type `Coffee`

### Aggregate and Association Methods

#### Customer

- `Customer create_order(coffee, price)`
  - given a **coffee object** and a price(as an integer), creates a
    new order and associates it with that customer and coffee.

#### Coffee

- `Coffee num_orders()`
  - Returns the total number of times that coffee has been ordered
- `Coffee average_price()`
  - Returns the average price for a coffee based on its orders
  - Reminder: you can calculate the average by adding up all the orders prices and
    dividing by the number of orders

### Bonus: For any invalid inputs raise an `Exception`.

Uncomment the following lines in the test files:

#### customer_tests.py

- lines 37 - 45

#### coffee_tests.py

- lines 26 - 30

#### order_tests.py

- lines 20 - 30

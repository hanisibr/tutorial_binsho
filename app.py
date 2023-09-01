from item import Item

# from phone import Phone
# from keyboard import Keyboard

from flask import Flask

app = Flask(__name__)


@app.route("/")
def output():
    item1 = Item("MacBook Pro M1", 7520, 3)
    return Item.apply_discount(item1)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("5000"))


# Polymorphism
# The ability for my programs to have different scenarios
# A single function that able to handle different kinds of objects as expected

# item1 = Keyboard("jscKeyboard", 1000, 3)

# item1.apply_discount()

# print(item1.price)

# Inheritance
# Reusing code across all classes (name, price, quantity)

# item1 = Phone("jscPhone", 1000, 3)

# item1.apply_increment(0.2)

# print(item1.price)

# Abstraction
# Abstract the information that is unnecessary to call / access it
# from my instances

# item1 = Item("MyItem", 750, 6)

# item1.send_email()


# Encapsulation
# Don't allow direct access to the price attribute
# Instead, modify this attribute by using methods

# item1 = Item("MyItem", 750, 2)

# item1.apply_increment(0.2)
# item1.apply_discount()

# print(item1.price)

# item1.name = "OtherItemmmmm"

# print(item1.name)

# item1.name = "OtherItem"

# print(item1.read_only_name)

# Item.instantiate_from_csv()
# print(Item.all)

# phone1 = Phone("jscPhonev10", 500, 5, 1)

# print(Item.all)
# print(Phone.all)

# print(phone1.calculate_total_price())
# phone2 = Phone("jscPhonev20", 700, 5, 1)


# print(Item.is_integer(7.0))

# Item.instantiate_from_csv()
# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
# item1.apply_discount()
# print(item1.price)

# All the attributes for Class level
# print(Item.__dict__)
# All the attributes for instance level
# print(item1.__dict__)

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

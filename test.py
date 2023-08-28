import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity")),
                )

    @staticmethod
    def is_integer(num):
        # Count out the floats that are point zero
        # For e.g.: 5.0, 10.0

        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(7.0))

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

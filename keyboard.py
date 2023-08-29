from item import Item


# Polymorphism (+ Inheritance)
class Keyboard(Item):
    pay_rate = 0.7

    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Assign to self object
        # self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)

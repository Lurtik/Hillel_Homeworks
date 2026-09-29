from os import name


class Item:

    def __init__(self, name, price, description, dimensions: tuple ):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.description} \nРозмір: {self.dimensions}\nЦіна: {self.price}"

class User:

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname} - {self.phone_number}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, count):
        self.products[item] = count

    def get_total(self):
        self.total = sum(
            item.price * count
            for item, count in self.products.items()
        )
        return self.total

    def __str__(self):
        result = f"Замовлення покупця: {self.user}\n"
        result += "Товари:\n"

        for item, count in self.products.items():
            result += (
                f"- {item.name} | "
                f"Кількість: {count} | "
                f"Ціна за одиницю: {item.price} грн | "
                f"Сума: {item.price * count} грн\n"
            )

        result += f"Загальна вартість: {self.get_total()} грн"

        return result

box = Item("коробка", 100, "carton box", (100,100,100))
print(box)
lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40

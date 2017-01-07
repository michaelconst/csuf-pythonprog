class Item:
    def __init__(self, item_id, description, price):
        self.item_id = item_id
        self.desciption = description
        self.price = price


class Inventory:
    def __init__(self):
        self.items = {"12345": Item("12345", "Cutting board", 12.99)}

    def get_item(self, item_id):
        return self.items.get(item_id)


class Order:
    inventory = Inventory()
    instructions = 'leave at front door'

    def __init__(self, item_id, units=1):
        self.__item_id = item_id
        self.units = units

    @property
    def units(self):
        return self.__units

    @units.setter
    def units(self, value):
        if value > 0:
            self.__units = value
        else:
            raise ValueError("units must be > 0")

    def total(self):
        item_price = self.inventory.get_item(self._item_id).price
        return item_price * self.units


class Order2:
    def __init__(self, item_id, units=1):
        self.__item_id = item_id
        self.units = units

    @property
    def instructions(self):
        return 'leave by the side of the house'

    def get_units(self):
        return self.__units

    def set_units(self, value):
        if value > 0:
            self.__units = value
        else:
            raise ValueError("units must be > 0")

    def total(self):
        item_price = self.inventory.get_item(self._item_id).price
        return item_price * self.units

    units = property(get_units, set_units)


if __name__ == '__main__':
    # order = Order("12345", 5)
    # print(order.instructions)
    # order.instructions = 'leave by the side of the house'
    # print(order.instructions)

    order2 = Order2("12300", 5)
    print(order2.instructions)
    order2.instructions = 'will pickup at the postoffice'
    order2.__dict__['instructions'] = 'will pickup at the postoffice'
    print(order2.instructions)
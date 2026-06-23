class Cart:
    _cart = []

    def __init__(self):
        self.count = 0

    def add(self, obj):
        self.__class__._cart.append(obj)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):

        if self.count >= len(self.__class__._cart):
            raise StopIteration

        result = self.count
        self.count += 1
        return self.__class__._cart[result]

    def __len__(self):
        return len(self.__class__._cart)

    def __getitem__(self, key):
        return self.__class__._cart[key]

    @property
    def total(self):
        return sum(int(product._price) for product in self.__class__._cart)


class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price should not be negative")
        self._price = value


cart = Cart()


p1 = Product(name="Laptop", price=50000)

p2 = Product(name="Mouse", price=500)
cart.add(p1)
cart.add(p2)
cart[0]
print(cart.total)

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
# Since __maxprice is a private variable, modifications will not be reflected in the selling price.
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
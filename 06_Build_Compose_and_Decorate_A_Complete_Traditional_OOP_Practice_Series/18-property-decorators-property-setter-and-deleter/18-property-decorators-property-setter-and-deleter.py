#?18. Property Decorators: @property, @setter, and @deleter
#?Assignment:
#?Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# Define the Product class with property decorators
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute
    
    # Getter for price
    @property
    def price(self):
        return self._price
    
    # Setter for price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    # Deleter for price
    @price.deleter
    def price(self):
        del self._price

# Test property decorators
product = Product(100)
print(product.price)  # Output: 100
product.price = 200  # Update price
print(product.price)  # Output: 200
del product.price     # Delete price
try:
    print(product.price)  # !Raises AttributeError
except AttributeError:
    print("Price attribute deleted")
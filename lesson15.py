# Translating the tasks from the image, they are as follows:
# 1. Create a Person class, representing a person, with name and age attributes. Define an introduce method,
#    which will print a greeting with the person's name and age.
# 2. Create a Project class, representing a project in an online store. Implement methods for managing information
#    about products, such as adding products, and setting descriptions and prices.

# Let's implement these classes in Python with English variable names.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Product:
    def __init__(self, name, description="", price=0.0):
        self.name = name
        self.description = description
        self.price = price

class Project:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        self.products[product.name] = product
    
    def set_description(self, product_name, description):
        if product_name in self.products:
            self.products[product_name].description = description
        else:
            raise ValueError("Product not found.")
    
    def set_price(self, product_name, price):
        if product_name in self.products:
            self.products[product_name].price = price
        else:
            raise ValueError("Product not found.")

# Test the Person class
person = Person("Andre", 30)
introduction = person.introduce()

# Test the Project class with Product class
project = Project()
product = Product("Laptop", "High-performance laptop", 999.99)
project.add_product(product)
project.set_description("Laptop", "Updated description: Portable and powerful laptop")
project.set_price("Laptop", 1099.99)

# Verify the results
print(person.name, person.age, introduction,
 project.products["Laptop"].name,
 project.products["Laptop"].description,
 project.products["Laptop"].price)

# The task is to create a Book class representing a book in a library. 
# It must have the following attributes: title, author, publication_year, is_available.
# It also requires the following instance methods: checkout (sets is_available to False),
# checkin (sets is_available to True), and display_info which prints information about the book.

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True
    
    def checkout(self):
        if self.is_available:
            self.is_available = False
            return f"The book '{self.title}' has been checked out."
        return f"The book '{self.title}' is not available for checkout."
    
    def checkin(self):
        if not self.is_available:
            self.is_available = True
            return f"The book '{self.title}' has been returned."
        return f"The book '{self.title}' is already in the library."
    
    def display_info(self):
        availability = "available" if self.is_available else "not available"
        return (f"Title: {self.title}, Author: {self.author}, "
                f"Publication Year: {self.publication_year}, Availability: {availability}")

# Test the Book class
book = Book("War and Peace", "Leo Tolstoy", 1869)

# Checkout the book
checkout_message = book.checkout()

# Try to checkout again
checkout_again_message = book.checkout()

# Checkin the book
checkin_message = book.checkin()

# Display book info
book_info = book.display_info()

print(checkout_message, checkout_again_message, checkin_message, book_info)

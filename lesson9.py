# Task 1: Create a dictionary of students and display information by name, remove by name
students_info = {
    'Alice': {'age': 24, 'major': 'Biology'},
    'Bob': {'age': 19, 'major': 'Chemistry'},
    'Charlie': {'age': 22, 'major': 'History'}
}

def display_student(name):
    return students_info.get(name, "Student not found")

def remove_student(name):
    if name in students_info:
        del students_info[name]
        return f"{name} has been removed from the student dictionary."
    else:
        return "Student not found"

# Task 2: Create two sets and define functions for intersection and union
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

def intersection(set1, set2):
    return set1 & set2

def union(set1, set2):
    return set1 | set2

# Task 3: Create a dictionary representing an inventory of products in a store
inventory = {
    '001': {'name': 'pen', 'quantity': 100, 'price': 0.99},
    '002': {'name': 'notebook', 'quantity': 50, 'price': 2.99},
    '003': {'name': 'eraser', 'quantity': 150, 'price': 0.49}
}

def find_product(product_id):
    return inventory.get(product_id, "Product not found")

def calculate_total_value():
    return sum(product['quantity'] * product['price'] for product in inventory.values())

# Task 4: Create a dictionary representing a country-city mapping
country_city_map = {
    'France': ['Paris', 'Lyon', 'Marseille'],
    'Germany': ['Berlin', 'Hamburg', 'Munich'],
    'Italy': ['Rome', 'Milan', 'Naples']
}

# Display some student information
print(display_student('Alice'))

# Remove a student and print the result
print(remove_student('Bob'))

# Find the intersection and union of two sets
print("Intersection:", intersection(set_a, set_b))
print("Union:", union(set_a, set_b))

# Find a product in the inventory and print the result
print(find_product('001'))

# Calculate the total value of the inventory
print("Total inventory value:", calculate_total_value())

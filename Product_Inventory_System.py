# Product Inventory System using OOP

class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def category(self):
        if self.price >= 5000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print("\nProduct ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price        : ₹", self.price)
        print("Category     :", self.category())
        print("-" * 30)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self):
        product_id = int(input("Enter Product ID: "))
        product_name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))

        product = Product(product_id, product_name, price)
        self.products.append(product)

        print("Product added successfully!")

    def display_all(self):
        if len(self.products) == 0:
            print("\nNo products available.")
        else:
            print("\n------ Product Details ------")
            for product in self.products:
                product.display()


# Main Program
inventory = Inventory()

while True:
    print("\n===== Product Inventory System =====")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.display_all()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
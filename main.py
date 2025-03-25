#TODO (Althea): (Order Details Collection)
def get_price(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Kindly enter the original price.")

def get_quantity(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Kindly enter your desired quantity.")

def get_order_details():
    order_items = []
    while True:
        item = {}
        item['product_name'] = input("Enter Product Name: ")
        item['price'] = get_price("Enter Price: ")
        item['quantity'] = get_quantity("Enter Quantity: ")
        
        order_items.append(item)
        
        if input("Add another Item? (y/n): ").lower() != 'y':
            break
    return order_items

#TODO (Name): (Description)
def get_customer_detsils():
    pass

#TODO (Name): (Description)
def calculate_total():
    pass

#TODO (Name): (Description)
def display_receipt():
    pass

#TODO (Name): (Description)
def main():
    pass
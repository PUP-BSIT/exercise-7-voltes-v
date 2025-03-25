#TODO (Althea): Order Details Collection
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

#TODO (Precious): Function to get customer details
def get_customer_details():
    customer_name = input("Enter customer name: ")
    senior_id = input("Enter senior ID (leave blank if not senior): ")
    return customer_name, senior_id

#TODO (Dyanna): Function to calculate grand total with possible senior discount
def calculate_total(orders, senior_id):
    grand_total = sum(item['total'] for item in orders)
    discount = 0
    if senior_id:
        discount = grand_total * 0.10
    return grand_total - discount, discount 

#TODO (Daphne): Implement receipt display
def display_receipt(order_items, customer_name, subtotal, discount, grand_total):

    print("\n=== ORDER DETAILS ===")
    print("Product\t\tPrice\tQty\tTotal")
    for item in order_items:
        total = item['price'] * item['quantity']
        print(f"{item['product_name']}\t\t{item['price']:.2f}\t{item['quantity']}\t{total:.2f}")

    print("\n=== CUSTOMER INFORMATION ===")
    print(f"Customer Name: {customer_name['name']}")
    if customer_name['senior_id'].strip():
        print(f"Senior ID No.: {customer_name['senior_id']}")
        print("(10% Senior Citizen Discount Applied)")

    print("\n=== PAYMENT SUMMARY ===")
    print(f"Subtotal: {subtotal:.2f}")
    if discount > 0:
        print(f"Discount: -{discount:.2f}")
    print(f"Grand Total: {grand_total:.2f}")

#TODO (Name): (Description)
def main():
    pass
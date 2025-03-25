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

#TODO (JC): Main function to manage the order system
def main():
    order_items = []
    customer_name = ""
    senior_id = ""

    while True:
        print("\n=== ORDER MANAGEMENT SYSTEM ===")
        print("1. Collect Order Details")
        print("2. Get Customer Details")
        print("3. Calculate Grand Total")
        print("4. Display Receipt")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            order_items = get_order_details()
        
        elif choice == "2":
            customer_name, senior_id = get_customer_details()
        
        elif choice == "3":
            if not order_items:
                print("No orders available. Please collect order details first.")
            else:
                for item in order_items:
                    item['total'] = item['price'] * item['quantity']
                subtotal, discount = calculate_total(order_items, senior_id)
                print(
                    f"Subtotal: {subtotal:.2f}\n"
                    f"Discount: {discount:.2f}\n"
                    f"Grand Total: {subtotal - discount:.2f}"
                )
        
        elif choice == "4":
            if not order_items or not customer_name:
                print("Please complete order and customer details first.")
            else:
                subtotal, discount = calculate_total(order_items, senior_id)
                display_receipt(
                    order_items,
                    {"name": customer_name, "senior_id": senior_id},
                    subtotal,
                    discount,
                    subtotal - discount,
                )
        
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

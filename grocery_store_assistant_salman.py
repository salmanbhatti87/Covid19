# Smart Grocery Store Assistant

product_catalog = {
    "apple": (100, 10),
    "banana": (60, 20),
    "milk": (120, 4),
    "bread": (80, 7)
}

def display_products():
    print("\nAvailable Products:")
    for product, (price, stock) in product_catalog.items():
        stock_alert = " Low Stock!" if stock < 5 else ""
        print(f"{product.capitalize()} - Rs.{price}, In stock: {stock}{stock_alert}")
    print()

def add_or_update_product():
    product = input("Enter product name: ").lower()
    price = int(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    
    if product in product_catalog:
        current_price, current_stock = product_catalog[product]
        product_catalog[product] = (price, current_stock + stock)
        print(f"{product.capitalize()} updated successfully.\n")
    else:
        product_catalog[product] = (price, stock)
        print(f"{product.capitalize()} added successfully.\n")

def purchase_items():
    cart = {}
    while True:
        display_products()
        item = input("Enter product to purchase (or type 'done' to finish): ").lower()
        if item == 'done':
            break
        if item not in product_catalog:
            print("Item not found.")
            continue
        qty = int(input(f"Enter quantity for {item}: "))
        price, stock = product_catalog[item]
        if qty > stock:
            print(f"Only {stock} in stock. Try again.")
            continue
        cart[item] = (price, qty)
        product_catalog[item] = (price, stock - qty)
        print(f"{qty} {item}(s) added to cart.\n")

    generate_bill(cart)

def generate_bill(cart):
    if not cart:
        print("Cart is empty.\n")
        return
    print("\nPurchase Receipt")
    total = 0
    for item, (price, qty) in cart.items():
        subtotal = price * qty
        print(f"{item.capitalize():<10} Rs.{price} x {qty} = Rs.{subtotal}")
        total += subtotal
    print(f"{'-'*30}\nTotal: Rs.{total}\n")

def main():
    print("🛒 Welcome to the Smart Grocery Store Assistant")
    while True:
        print("\n1. View Products\n2. Add/Update Product\n3. Purchase Items\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_or_update_product()
        elif choice == '3':
            purchase_items()
        elif choice == '4':
            print("Thank you for using the assistant!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

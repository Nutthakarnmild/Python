products = []

while True:
    print("====================")
    print(" Menu Options")
    print("====================")
    print(" 1. Add Product")
    print(" 2. Sell Product")
    print(" 3. Display Products")
    print(" 4. Display Sales")
    print(" 5. Exit Program")
    print("====================")

    choice = input("Please select an option: ")

    if choice == "1":
        product_name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        product = {
            "name": product_name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)
        print("Added product:", product_name, "Price:", price, "Quantity:", quantity)
        print()

    elif choice == "2":
        product_name = input("Product name to sell: ")
        quantity_to_sell = int(input("Quantity to sell: "))

        found_product = False
        for product in products:
            if product["name"] == product_name:
                if product["quantity"] >= quantity_to_sell:
                    product["quantity"] -= quantity_to_sell
                    print("Sold product:", product_name, "Price:", product["price"], "Quantity:", quantity_to_sell)
                    found_product = True
                    break

        if not found_product:
            print("Product not found")
        print()

    elif choice == "3":
        print("Product List:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
        print()

    elif choice == "4":
        print("Sales List:")
        for product in products:
            if product["quantity"] < quantity_to_sell:
                print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {quantity_to_sell - product['quantity']}")
        print()

    elif choice == "5":
        print("Exit Program...")
        break

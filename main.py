from products import Product
from store import Store


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=400)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    google = Product("Google Pixel 7", price=500, quantity=250)

    store = Store([bose, mac, google])

    while True:
        print("\033[33m1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("\033[31mPlease choose a number: \033[0m")
        print()

        if choice == '1':
            all_products = store.get_all_products()
            for i, product in enumerate(all_products, start=1):
                print(f"{i}. {product.show()}")
                print("-------")
            print()

        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total quantity in store: { total_quantity}")
            print()

        elif choice == '3':
            print("------")
            all_products = store.get_all_products()
            for i, product in enumerate(all_products, start=1):
                print(f"{i}. {product.show()}")
            print("------")

            shopping_list = []
            while True:
                product_number = input("Enter product number  (or 'done' to finish): ")
                if product_number.lower() == 'done':
                    break
                try:
                    product_number = int(product_number)
                    if 1 <= product_number <= len(all_products):
                        selected_product = all_products[product_number - 1]
                        quantity = int(input("Enter quantity: "))
                        if quantity <= selected_product.quantity:
                            shopping_list.append((selected_product, quantity))
                            print("\033[33mProduct added to list!\033")
                        else:
                            print("\033[31mInsufficient quantity in stock!\033")
                    else:
                        print("\033[31mInvalid product number!\033")
                except ValueError:
                    print("\033[31mInvalid input! Please enter a number or 'done'.\033")

            order_price = store.order(shopping_list)
            print(f"\033[31m  > Order cost: {order_price} dollars. \033")
            print("     -----------")

        elif choice == '4':
            print("Bye!")
            break


if __name__ == "__main__":
    main()

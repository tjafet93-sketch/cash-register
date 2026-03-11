def register_sales():
    sales = {}
    daily_total = 0
    continue_selling = "yes"

    while continue_selling == "yes":
        print("\nSale Registration")
        product = input("Product name: ")
        price = float(input("Unit price: "))
        quantity = int(input("Quantity sold: "))
        sale_total = price * quantity
        daily_total += sale_total

        if product in sales:
            sales[product] += quantity
        else:
            sales[product] = quantity

        continue_selling = input("Do you want to register another sale? (yes/no): ").strip().lower()

    return sales, daily_total


def show_summary(sales, daily_total):
    print("\n====== DAILY SUMMARY ======")
    for product, quantity in sales.items():
        print(f"{product} - Quantity sold: {quantity}")
    print(f"\nTotal amount collected: ${daily_total:.2f}")


def main():
    sales, daily_total = register_sales()
    show_summary(sales, daily_total)


main()
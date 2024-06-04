# Let's keep track of your stocks!

def add_stock(stocks, name, amount):
    """Adds a stock to your portfolio."""
    stocks[name] = amount
    print(f"Added {amount} shares of {name} to your portfolio.")

def remove_stock(stocks, name):
    """Removes a stock from your portfolio."""
    if name in stocks:
        del stocks[name]
        print(f"Removed {name} from your portfolio.")
    else:
        print(f"{name} not found in your portfolio.")

def view_portfolio(stocks):
    """Shows you the current state of your portfolio."""
    if stocks:
        total_value = 0
        for name, amount in stocks.items():
            price = get_current_price(name)  # Imagine this gets the price from somewhere
            value = amount * price
            total_value += value
            print(f"{name}: {amount} shares at ${price:.2f} per share (${value:.2f} total)")
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    else:
        print("Your portfolio is currently empty.")

def get_current_price(name):
    """Pretend this gets the current price of a stock."""
    # In reality, this would use an API or other data source
    return 100.00  # Replace with actual price fetching logic

stocks = {}  # Your starting portfolio is empty

while True:
    print("\nWhat would you like to do?")
    print("1. Add a stock")
    print("2. Remove a stock")
    print("3. View your portfolio")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the stock name: ").upper()
        amount = int(input("Enter the number of shares: "))
        add_stock(stocks, name, amount)
    elif choice == "2":
        name = input("Enter the stock name to remove: ").upper()
        remove_stock(stocks, name)
    elif choice == "3":
        view_portfolio(stocks)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
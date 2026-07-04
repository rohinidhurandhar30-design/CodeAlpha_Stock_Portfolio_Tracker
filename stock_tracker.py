# CodeAlpha Task 2: Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("📊 STOCK PORTFOLIO TRACKER")
print("=" * 45)

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Update portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
print("\n" + "=" * 45)
print("📌 YOUR PORTFOLIO SUMMARY")
print("=" * 45)

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print("-" * 45)
print(f"💰 TOTAL INVESTMENT VALUE: ${total_investment}")
print("=" * 45)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=" * 30 + "\n")

    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        file.write(f"{stock}: {qty} shares = ${value}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment = ${total_investment}\n")

print("\n✅ Portfolio saved to portfolio.txt")

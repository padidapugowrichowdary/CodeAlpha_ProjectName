stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "WIPRO": 450,
    "RELIANCE": 2800,
    "HDFC": 1700,
    "ICICIBANK": 1250,
    "SBI": 850,
    "LT": 3800,
    "ITC": 430,
    "BHARTIARTL": 1800,
    "HCLTECH": 1650,
    "AXISBANK": 1200,
    "KOTAKBANK": 2100,
    "MARUTI": 12500,
    "TATAMOTORS": 720,
    "ADANIPORTS": 1450,
    "ASIANPAINT": 2500,
    "SUNPHARMA": 1750,
    "BAJFINANCE": 9200,
    "ULTRACEMCO": 11800
}

total_value = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        value = stock_prices[stock] * quantity
        total_value += value

        print(f"{stock} Value = ₹{value}")

    else:
        print("Stock not found!")

print("\nTotal Portfolio Value = ₹", total_value)
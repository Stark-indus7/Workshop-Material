import requests

def get_exchange_rates(api_key):
    """Fetch exchange rates from the exchangerate-api."""
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates.")
    data = response.json()
    if data['result'] != 'success':
        raise Exception("Error in exchange rate data.")
    return data['conversion_rates']

def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another."""
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    converted_amount = amount * rates[to_currency]
    return converted_amount

def main():
    """Main function to run the Currency Converter."""
    print("Currency Converter")
    
    # Replace 'YOUR_API_KEY' with your actual API key from exchangerate-api.com
    api_key = '88a8d64c205e546a89f46486'
    
    try:
        rates = get_exchange_rates(api_key)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount < 0:
                print("Amount must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue
        
        from_currency = input("From Currency (e.g., USD, EUR): ").upper()
        to_currency = input("To Currency (e.g., USD, EUR): ").upper()
        
        if from_currency not in rates or to_currency not in rates:
            print("Unsupported currency code. Please try again.\n")
            continue
        
        converted = convert_currency(amount, from_currency, to_currency, rates)
        print(f"{amount} {from_currency} = {converted:.2f} {to_currency}\n")
        
        again = input("Do you want to convert another amount? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
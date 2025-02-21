import requests
from bs4 import BeautifulSoup


def get_exchange_rate():
    """Fetch the latest USD to IRR exchange rate from tgju.org."""
    url = 'https://www.tgju.org'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        price_element = soup.select_one(".info-price span")
        if not price_element:
            raise ValueError("Exchange rate element not found on the page.")

        price_text = price_element.text.replace(",", "")
        return float(price_text)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
    except ValueError as e:
        print(f"Parsing error: {e}")

    return None


def get_user_amount():
    """Prompt user to enter amount in USD and validate input."""
    while True:
        user_input = input("How much money do you have in USD? ")
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main function to get user input, fetch exchange rate, and display the converted amount."""
    exchange_rate = get_exchange_rate()

    if exchange_rate is None:
        print("Could not retrieve exchange rate. Please try again later.")
        return

    user_amount = get_user_amount()
    total_irr = user_amount * exchange_rate

    print(f"{user_amount} USD is approximately {total_irr:,.0f} IRR")


if __name__ == "__main__":
    main()

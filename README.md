# Currency Converter

A Python script that fetches the latest exchange rate of USD to IRR from tgju.org and calculates the equivalent value for a given amount of money.

## Features
- Fetches real-time USD to IRR exchange rate using web scraping (BeautifulSoup).
- Takes user input for an amount in USD.
- Handles errors gracefully (invalid inputs, connection issues, etc.).
- Displays formatted output with thousands separator for better readability.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/fereshtehAhmadi/currency.git
   ```
2. Navigate to the project directory:
   ```bash
   cd currency
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using the following command:
```bash
python currency.py
```
Then, enter the amount of money in USD, and the script will return the equivalent amount in IRR based on the latest exchange rate.

## Notes
- The script scrapes data from `tgju.org`, so changes to the website structure might affect functionality.
- Error handling is included for invalid inputs and connection issues.
- Ensure you have an active internet connection for fetching exchange rates.

## License
This project is licensed under the MIT License.
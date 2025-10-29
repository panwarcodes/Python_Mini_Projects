# Multi-country Currency Converter by @panwarcodes/github
import sys
import requests
from datetime import date, timedelta

# API's basic overview is as follows:
# today_date = 2025-10-28 is API's date format 
# curr_1, curr_2 = currency names in shortcode eg. INR, JPY, USD, etc
# https://fxds-public-exchange-rates-api.oanda.com/cc-api/currencies?base={curr_1}&quote={curr_2}&data_type=general_currency_pair&start_date={yesterday_date}&end_date={today_date}

# Asking the user for curr_1, curr_2 and amount_to_convert
try:
    curr_1 = str(input("Enter the currency's shortcode you want to convert from\nFor example, [JPY,USD,INR or google the country's shortcode]: ")).upper()
    curr_2 = str(input("Enter the currency's shortcode you want to convert to\nFor example, [JPY,USD,INR or google the country's shortcode]: ")).upper()
    amount_to_convert = float(input("Enter the amount you want to convert: "))
except ValueError:
    print("Enter values in the correct format!")
    sys.exit()
print("Fetching live exchange rate...")
print()

# API - fetching live price logic 
def curr_converter(curr_1, curr_2):
    today = date.today()
    today_date = today.strftime("%Y-%m-%d")
    yesterday = today - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")
    try:
        dict1 = requests.get(f"https://fxds-public-exchange-rates-api.oanda.com/cc-api/currencies?base={curr_1}&quote={curr_2}&data_type=general_currency_pair&start_date={yesterday_date}&end_date={today_date}")
        datadict = dict1.json()
        datadict_response = datadict['response']
        access_0index = datadict_response[0]
        get_curr_2_liveprice = access_0index['average_bid']
        return float(get_curr_2_liveprice)
    except KeyError:
        print("Uh-Oh! Maybe you didn't enter correct country code.")
        sys.exit()
liveprice = curr_converter(curr_1, curr_2)

# Final output that multiplies curr_2's 1 unit price with amount_to_convert 
print(f"{curr_1} {amount_to_convert} is equivalent to {curr_2} {round(liveprice * amount_to_convert, 2)} today!")
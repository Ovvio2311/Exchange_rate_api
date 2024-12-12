import requests
import logging
import time

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/JPY"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        jpy_to_hkd = data['rates']['HKD']
        print(f"1 JPY = {jpy_to_hkd} HKD")
        logging.info(f"1 JPY = {jpy_to_hkd} HKD")
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"An error occurred: {req_err}")

def update_rate():
    while True:
        get_exchange_rate()
        time.sleep(60)  # Wait for 1 minute before fetching the rate again

# Start the rate update loop
update_rate()
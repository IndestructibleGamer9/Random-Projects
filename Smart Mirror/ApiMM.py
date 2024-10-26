import requests
import time
from datetime import datetime

"""
WEATHER API
"""

def Get_weather():
    start = time.perf_counter()
    api_key = ''
    city = 'Brisbane'   
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    description = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'], 0)
    feels_like = weather_data.json()['main']['feels_like']
    humidity = weather_data.json()['main']['humidity']
    icon_code = weather_data.json()['weather'][0]['icon']
    weatherForcast = {
        'Current Temperature' : temp,
        'description' : description,
        'feels like' : feels_like,
        'humidity' : humidity,
        'description' : description, 
        'icon' : icon_code,
    }
    f = time.perf_counter()
    print(f'Wether Data retuned in {f-start}s')
    return weatherForcast
"""
TIME API
"""

def ddt():
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%I:%M %p')
    day = now.strftime('%A')
    r_data = now.strftime('%Y-%m-%d %H:%M:%S')                    
    # print(f'date: {date} time: {time} day: {day}')
    dtInfo = {
        'date' : date,
        'time' : time,
        'day' : day,
        'r data' : r_data
    }
    return dtInfo
"""
STOCK API
"""


import requests
import time

def get_price_info(ticker, con=True):
    start = time.perf_counter()
    API_KEY = ''
    base_url = 'https://finnhub.io/api/v1'
    headers = {
        'X-Finnhub-Token': API_KEY
    }

    def get_data(endpoint, params=None):
        url = f"{base_url}/{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 429:
            print("Rate limit exceeded. Retrying after a short break.")
            time.sleep(60)
            return get_data(endpoint, params)
        response.raise_for_status()
        return response.json()
    
    try:
        # For stocks
        quote_data = get_data(f'quote', {'symbol': ticker})
        current_price = quote_data.get('c')
        previous_close = quote_data.get('pc')
        market_open = current_price != previous_close
    
        if current_price is None or previous_close is None:
            raise ValueError("Invalid ticker symbol or data unavailable.")
        
        percentage_change = ((current_price - previous_close) / previous_close) * 100
        percentage_change = round(percentage_change, 2)
        u = '#3EE765' if percentage_change > 0 else '#E73535'
        # Ensure this function is defined elsewhere

        f = time.perf_counter()
        print(f'Data for {ticker} returned in {f-start:.2f}s')
        bet = {
            'name': ticker,
            'current_price': current_price,
            'previous_close': previous_close,
            'percentage_change': percentage_change,
            'market_open': market_open,
            'up_down': u
        }
        return bet

    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}

def convertUS_AU(amount):
    date = 'latest'
    apiVersion = 'v1'
    endpoint = 'currencies/usd.json'
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}"
    response = requests.get(url)
    data = response.json()
    # print(data)
    conversion_rate = data["usd"]['aud']
    # print(conversion_rate)
    rate = conversion_rate
    return amount * rate

if __name__ == '__main__':
    stonks = [
        'TSLA',
        'AAPL',  # Corrected from 'APPL'
        'MSFT'
    ]
    start = time.perf_counter()
    for item in stonks:  
        price_info = get_price_info(item)
        if 'error' in price_info:
            print(f"Error for {item}: {price_info['error']}")
        else:
            print(price_info)
    finish = time.perf_counter()
    print(f'Operation finished in {round(finish-start, 2)} second(s)')

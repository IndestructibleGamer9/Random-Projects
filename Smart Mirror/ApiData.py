import requests
import time
from datetime import datetime

"""
WEATHER API
"""


def Get_weather():
    api_key = ''
    city = 'Brisbane'   
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    weather = weather_data.json()['weather'][0]['main']
    description = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'], 0)
    feels_like = weather_data.json()['main']['feels_like']
    humidity = weather_data.json()['main']['humidity']
    icon_code = weather_data.json()['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

    weatherForcast = {
        'Current Temperature' : temp,
        'description' : description,
        'feels like' : feels_like,
        'humidity' : humidity,
        'description' : description, 
        'icon' : icon_code
    }
    return weatherForcast

"""
TIME API
"""

def ddt():
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%I:%M %p')
    day = now.strftime('%A')
    # print(f'date: {date} time: {time} day: {day}')
    dtInfo = {
        'date' : date,
        'time' : time,
        'day' : day
    }
    return dtInfo

"""
STOCK API
"""


def get_price_info(ticker, con=True):
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
        # Fetch current price
        quote_data = get_data(f'quote?symbol={ticker}')
        
        current_price = quote_data.get('c')
        previous_close = quote_data.get('pc')
        
        if current_price is None or previous_close is None:
            raise ValueError("Invalid ticker symbol or data unavailable.")
        
        # Determine market status (if current price equals previous close, market might be closed)
        market_open = current_price != previous_close
        
        if market_open:
            percentage_change = ((current_price - previous_close) / previous_close) * 100
        else:
            # If market is closed, we use the previous day's close for percentage change
            percentage_change = ((previous_close - quote_data.get('o')) / quote_data.get('o')) * 100
        if percentage_change > 0: #positive
                percentage_change = round(percentage_change, 2)
                # percentage_change = '+' + str(percentage_change)   
                # print(percentage_change) 
                u = '#32431C'
        else:
            percentage_change = round(percentage_change, 2) 
            u = '#581515'
            # print(percentage_change)       
        if ticker != 'TSLA':
            current_price = convertUS_AU(current_price)

        return {
            'name' : ticker,
            'current_price': current_price,
            'previous_close': previous_close,
            'percentage_change': percentage_change,
            'market_open': market_open,
            'up down' : u
        }
        
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    except ValueError as ve:
        return {'error': str(ve)}

def get_stonks(stocks):
    start = time.perf_counter()
    
    for item in stocks:
        price_info = get_price_info(item)
        yield {item: price_info}
    
    finish = time.perf_counter()
    print(f'Operation finished in {round(finish-start, 2)} second(s)')


"""



"""
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
    # Example usage
    
    stonks = [
        'TSLA',
        'BINANCE:SOLUSDT',
        'BINANCE:BTCUSDT'
    ]
    

    start = time.perf_counter()
    
    for item in stonks:
        
        price_info = get_price_info(item)
        print(price_info)

    

    
    finish = time.perf_counter()
    print(f'Operation finished in {round(finish-start, 2)} second(s)')
    
    
    


    # print(Get_weather())
#     print(ddt())

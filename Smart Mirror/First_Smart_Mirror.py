import tkinter as tk
from PIL import Image, ImageTk
from ApiData import Get_weather, ddt, get_price_info
from PIL import Image
import multiprocessing as mp 

stuff = [
    'good morning!'
    'good night!'
]

HEIGHT = 1080
WIDTH = 1920

class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.news_articles = []
        self.weather = {}
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.configure(bg='black')



    """
            _____                            _____                        _____                            _____                            _____          
            /\    \                          /\    \                      /\    \                          /\    \                          /\    \         
            /::\    \                        /::\    \                    /::\    \                        /::\____\                        /::\    \        
        /::::\    \                      /::::\    \                   \:::\    \                      /:::/    /                       /::::\    \       
        /::::::\    \                    /::::::\    \                   \:::\    \                    /:::/    /                       /::::::\    \      
        /:::/\:::\    \                  /:::/\:::\    \                   \:::\    \                  /:::/    /                       /:::/\:::\    \     
        /:::/__\:::\    \                /:::/__\:::\    \                   \:::\    \                /:::/    /                       /:::/__\:::\    \    
        \:::\   \:::\    \              /::::\   \:::\    \                  /::::\    \              /:::/    /                       /::::\   \:::\    \   
    ___\:::\   \:::\    \            /::::::\   \:::\    \                /::::::\    \            /:::/    /      _____            /::::::\   \:::\    \  
    /\   \:::\   \:::\    \          /:::/\:::\   \:::\    \              /:::/\:::\    \          /:::/____/      /\    \          /:::/\:::\   \:::\____\ 
    /::\   \:::\   \:::\____\        /:::/__\:::\   \:::\____\            /:::/  \:::\____\        |:::|    /      /::\____\        /:::/  \:::\   \:::|    |
    \:::\   \:::\   \::/    /        \:::\   \:::\   \::/    /           /:::/    \::/    /        |:::|____\     /:::/    /        \::/    \:::\  /:::|____|
    \:::\   \:::\   \/____/          \:::\   \:::\   \/____/           /:::/    / \/____/          \:::\    \   /:::/    /          \/_____/\:::\/:::/    / 
    \:::\   \:::\    \               \:::\   \:::\    \              /:::/    /                    \:::\    \ /:::/    /                    \::::::/    /  
    \:::\   \:::\____\               \:::\   \:::\____\            /:::/    /                      \:::\    /:::/    /                      \::::/    /   
        \:::\  /:::/    /                \:::\   \::/    /            \::/    /                        \:::\__/:::/    /                        \::/____/    
        \:::\/:::/    /                  \:::\   \/____/              \/____/                          \::::::::/    /                          ~~          
        \::::::/    /                    \:::\    \                                                    \::::::/    /                                       
        \::::/    /                      \:::\____\                                                    \::::/    /                                        
            \::/    /                        \::/    /                                                     \::/____/                                         
            \/____/                          \/____/                                                       ~~                                               
                                                                                                                                                            

    """

    def setup(self):
        self.weather = Get_weather()
        self.dt_info = ddt()
        self.get_stocker()
        self.build_display()
        self.update()
        self.weather_update()
        self.stock_update()

    def get_stocker(self):
        self.tesla_stock_info = get_price_info('TSLA')
        self.solana_stock_info = get_price_info('BINANCE:SOLUSDT')
        self.bitcoin_stock_info = get_price_info('BINANCE:BTCUSDT')


    def Formatt(self, num):
        if num < 1000:
            return str(round(num, 2))
        elif num >= 1000 and num < 1000000:
            return f"{num/1000:.1f}K"
        elif num >= 1000000 and num < 1000000000:
            return f"{num/1000000:.1f}M"
        elif num >= 1000000000 and num < 1000000000000:
            return f"{num/1000000000:.1f}B"
        else:
            return f"{num/1000000000000:.1f}T"
            
    def day_position(self, day):
        if day == 'Monday' or day == 'Tuesday':
            return 1595
        elif day == 'Wednesday':
            return 1463
        elif day == 'Thursday' or day == 'Saturday':
            return 1540
        elif day == 'Friday':
            return 1652
        elif day == 'Sunday':
            return 1605
        else:
            print(f'no match for {day}')
            return "ERROR: Unknown day"
                    

    def build_display(self):
        self.day_display = tk.Label(self.root, 
                                    text=self.dt_info['day'].upper(), 
                                    fg='white', bg='black', font=('Anurati', 40))
        
        self.date_display = tk.Label(self.root, 
                                        text=(self.dt_info['date']), 
                                        fg='white', bg='black', font=('Exan', 30))

        self.temperature_display = tk.Label(self.root, 
                                            text=(f"{(self.weather['Current Temperature'])}°"), 
                                            fg='white', bg='black', font=('Ethnocentric Rg', 30))
        
        self.feels_like_display = tk.Label(self.root, 
                                            text=(f"{(self.weather['feels like'])}°"), 
                                            fg='white', bg='black', font=('Ethnocentric Rg', 10))
        
        self.humidity_display = tk.Label(self.root, 
                                            text=(f"{self.weather['humidity']}%"), 
                                            fg='white', bg='black', font=('Ethnocentric Rg', 10))
        
        image_path = self.icon_to_icon(self.weather['icon'])
        img = Image.open(image_path)
        img = img.resize((75, 75), Image.Resampling.LANCZOS)

        self.tkimage = ImageTk.PhotoImage(img)
        self.weather_icon_display = tk.Label(self.root, image=self.tkimage, bg='black')

        self.time_display = tk.Label(self.root,
                                        text=(str(self.dt_info['time'])),
                                        fg='white', bg='black', font=('Quantum', 80))   

        
        #stocks
        'name'

        self.stock_name1 = tk.Label(self.root,
                                    text=(f"{self.tesla_stock_info['name']}   {self.tesla_stock_info['percentage_change']}%"),
                                    fg=str(self.tesla_stock_info['up down']), bg='black', font=('Ethnocentric Rg', 20))    
        self.stock_name1_other = tk.Label(self.root,
                                    text=(f"Tesla Inc.       ${self.Formatt(self.tesla_stock_info['current_price'])}"),
                                    fg='white', bg='black', font=('Ethnocentric Rg', 12))
                                    
        self.stock_name2 = tk.Label(self.root,
                                    text=(f"SOL     {self.solana_stock_info['percentage_change']}%"),
                                    fg=str(self.solana_stock_info['up down']), bg='black', font=('Ethnocentric Rg', 20))   
        self.stock_name2_other = tk.Label(self.root, 
                                    text=(f"Solana.         ${self.Formatt(self.solana_stock_info['current_price'])}"),
                                    fg='white', bg='black', font=('Ethnocentric Rg', 12))
        self.stock_name3 = tk.Label(self.root,
                                    text=(f'BTC    {self.bitcoin_stock_info["percentage_change"]}%'),
                                    fg=str(self.bitcoin_stock_info['up down']), bg='black', font=('Ethnocentric Rg', 20))  
        self.stock_name3_other = tk.Label(self.root, 
                                    text=(f"Bitcoin.         ${self.Formatt(self.bitcoin_stock_info['current_price'])}"),
                                    fg='white', bg='black', font=('Ethnocentric Rg', 12))                        
        
        
        self.weather_icon_display.place(x=180, y=50)
        self.humidity_display.place(x=115, y=110)
        self.temperature_display.place(x=50, y=50)
        self.feels_like_display.place(x=50, y=110)

        self.day_display.place(x=(self.day_position(self.dt_info['day'])-20), y=170)
        self.date_display.place(x=1600, y=260)
        self.time_display.place(x=1400, y=25)

        self.stock_name1.place(x=50, y=800)
        self.stock_name1_other.place(x=50, y=840)

        self.stock_name2.place(x=50, y=860)
        self.stock_name2_other.place(x=50, y=900)

        self.stock_name3.place(x=50, y=920)
        self.stock_name3_other.place(x=50, y=960)
        
    def end_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.destroy()
        return "break"

    """
              _____                            _____                            _____                            _____                        _____                            _____          
         /\    \                          /\    \                          /\    \                          /\    \                      /\    \                          /\    \         
        /::\____\                        /::\    \                        /::\    \                        /::\    \                    /::\    \                        /::\    \        
       /:::/    /                       /::::\    \                      /::::\    \                      /::::\    \                   \:::\    \                      /::::\    \       
      /:::/    /                       /::::::\    \                    /::::::\    \                    /::::::\    \                   \:::\    \                    /::::::\    \      
     /:::/    /                       /:::/\:::\    \                  /:::/\:::\    \                  /:::/\:::\    \                   \:::\    \                  /:::/\:::\    \     
    /:::/    /                       /:::/__\:::\    \                /:::/  \:::\    \                /:::/__\:::\    \                   \:::\    \                /:::/__\:::\    \    
   /:::/    /                       /::::\   \:::\    \              /:::/    \:::\    \              /::::\   \:::\    \                  /::::\    \              /::::\   \:::\    \   
  /:::/    /      _____            /::::::\   \:::\    \            /:::/    / \:::\    \            /::::::\   \:::\    \                /::::::\    \            /::::::\   \:::\    \  
 /:::/____/      /\    \          /:::/\:::\   \:::\____\          /:::/    /   \:::\ ___\          /:::/\:::\   \:::\    \              /:::/\:::\    \          /:::/\:::\   \:::\    \ 
|:::|    /      /::\____\        /:::/  \:::\   \:::|    |        /:::/____/     \:::|    |        /:::/  \:::\   \:::\____\            /:::/  \:::\____\        /:::/__\:::\   \:::\____\
|:::|____\     /:::/    /        \::/    \:::\  /:::|____|        \:::\    \     /:::|____|        \::/    \:::\  /:::/    /           /:::/    \::/    /        \:::\   \:::\   \::/    /
 \:::\    \   /:::/    /          \/_____/\:::\/:::/    /          \:::\    \   /:::/    /          \/____/ \:::\/:::/    /           /:::/    / \/____/          \:::\   \:::\   \/____/ 
  \:::\    \ /:::/    /                    \::::::/    /            \:::\    \ /:::/    /                    \::::::/    /           /:::/    /                    \:::\   \:::\    \     
   \:::\    /:::/    /                      \::::/    /              \:::\    /:::/    /                      \::::/    /           /:::/    /                      \:::\   \:::\____\    
    \:::\__/:::/    /                        \::/____/                \:::\  /:::/    /                       /:::/    /            \::/    /                        \:::\   \::/    /    
     \::::::::/    /                          ~~                       \:::\/:::/    /                       /:::/    /              \/____/                          \:::\   \/____/     
      \::::::/    /                                                     \::::::/    /                       /:::/    /                                                 \:::\    \         
       \::::/    /                                                       \::::/    /                       /:::/    /                                                   \:::\____\        
        \::/____/                                                         \::/____/                        \::/    /                                                     \::/    /        
         ~~                                                                ~~                               \/____/                                                       \/____/         
                                                                                                                                                                                          
    """

    
    def update(self):
        self.dt_info = ddt()
        self.day_display.config(text=self.dt_info['day'].upper())
        self.date_display.config(text=(self.dt_info['date']))
        self.time_display.config(text=(str(self.dt_info['time'])))
        self.root.after(100, self.update)    

    def weather_update(self):
        print('Updateing weather info')
        self.weather = Get_weather() 
        self.temperature_display.config(text=(f"{(self.weather['Current Temperature'])}°"))
        self.humidity_display.config(text=(f"{self.weather['humidity']}%"))
        self.feels_like_display.config(text=(f"{(self.weather['feels like'])}°"))
        image_path = self.icon_to_icon(self.weather['icon'])
        img = Image.open(image_path)
        img = img.resize((75, 75), Image.Resampling.LANCZOS)
        self.tkimage = ImageTk.PhotoImage(img)
        self.weather_icon_display.config(image=self.tkimage)
        self.root.after(600000, self.weather_update)    

    def stock_update(self):
        print('Updateing stock info')
        self.tesla_stock_info = get_price_info('TSLA')
        self.solana_stock_info = get_price_info('BINANCE:SOLUSDT')
        self.bitcoin_stock_info = get_price_info('BINANCE:BTCUSDT')
        self.stock_name1.config(text=(f"{self.tesla_stock_info['name']}   {self.tesla_stock_info['percentage_change']}%"), fg=str(self.tesla_stock_info['up down']))
        self.stock_name1_other.config(text=(f"Tesla Inc.       ${self.Formatt(self.tesla_stock_info['current_price'])}"))
        self.stock_name2.config(text=(f"SOL     {self.solana_stock_info['percentage_change']}%"), fg=str(self.solana_stock_info['up down']))
        self.stock_name2_other.config(text=(f"Solana.         ${self.Formatt(self.solana_stock_info['current_price'])}"))
        self.stock_name3.config(text=(f'BTC    {self.bitcoin_stock_info["percentage_change"]}%'), fg=str(self.bitcoin_stock_info['up down']))
        self.stock_name3_other.config(text=(f"Bitcoin.         ${self.Formatt(self.bitcoin_stock_info['current_price'])}"))
        self.root.after(3000000, self.stock_update)
#time infinite
#wether 60 calls a minute 1 call every 10 minutes calls a month
#stocks




    """
             _______                       _____                            _____                            _____                            _____          
        /::\    \                     /\    \                          /\    \                          /\    \                          /\    \         
       /::::\    \                   /::\    \                        /::\____\                        /::\    \                        /::\    \        
      /::::::\    \                  \:::\    \                      /:::/    /                       /::::\    \                      /::::\    \       
     /::::::::\    \                  \:::\    \                    /:::/    /                       /::::::\    \                    /::::::\    \      
    /:::/~~\:::\    \                  \:::\    \                  /:::/    /                       /:::/\:::\    \                  /:::/\:::\    \     
   /:::/    \:::\    \                  \:::\    \                /:::/____/                       /:::/__\:::\    \                /:::/__\:::\    \    
  /:::/    / \:::\    \                 /::::\    \              /::::\    \                      /::::\   \:::\    \              /::::\   \:::\    \   
 /:::/____/   \:::\____\               /::::::\    \            /::::::\    \   _____            /::::::\   \:::\    \            /::::::\   \:::\    \  
|:::|    |     |:::|    |             /:::/\:::\    \          /:::/\:::\    \ /\    \          /:::/\:::\   \:::\    \          /:::/\:::\   \:::\____\ 
|:::|____|     |:::|    |            /:::/  \:::\____\        /:::/  \:::\    /::\____\        /:::/__\:::\   \:::\____\        /:::/  \:::\   \:::|    |
 \:::\    \   /:::/    /            /:::/    \::/    /        \::/    \:::\  /:::/    /        \:::\   \:::\   \::/    /        \::/   |::::\  /:::|____|
  \:::\    \ /:::/    /            /:::/    / \/____/          \/____/ \:::\/:::/    /          \:::\   \:::\   \/____/          \/____|:::::\/:::/    / 
   \:::\    /:::/    /            /:::/    /                            \::::::/    /            \:::\   \:::\    \                    |:::::::::/    /  
    \:::\__/:::/    /            /:::/    /                              \::::/    /              \:::\   \:::\____\                   |::|\::::/    /   
     \::::::::/    /             \::/    /                               /:::/    /                \:::\   \::/    /                   |::| \::/____/    
      \::::::/    /               \/____/                               /:::/    /                  \:::\   \/____/                    |::|  ~|          
       \::::/    /                                                     /:::/    /                    \:::\    \                        |::|   |          
        \::/____/                                                     /:::/    /                      \:::\____\                       \::|   |          
         ~~                                                           \::/    /                        \::/    /                        \:|   |          
                                                                       \/____/                          \/____/                          \|___|          
                                                                                                                                                         
    """


    def icon_to_icon(self, icon):
        icons = {
        'sunny': r'',
        'cloud': r'',
        'sunny clouds': r'',
        'rain': r'',
        'thunder': r'',
        'snow': r'',
        'mist': r'',
        'cloudy night': r'',
        'clear night': r'',
    }
        if icon == '01d':
            return icons['sunny']
        elif icon == '02d':
            return icons['sunny clouds']
        elif icon == '03d':
            return icons['cloud']
        elif icon == '04d':
            return icons['cloud']
        elif icon == '09d':
            return icons['rain']
        elif icon == '10d':
            return icons['rain']
        elif icon == '11d':
            return icons['thunder']
        elif icon == '13d':
            return icons['snow']
        elif icon == '50d':
            return icons['mist']
        elif icon == '01n':
            return icons['clear night']
        elif icon == '02n':
            return icons['cloudy night']
        elif icon == '03n':
            return icons['cloud']
        elif icon == '04n':
            return icons['cloud']
        elif icon == '09n':
            return icons['rain']
        elif icon == '10n':
            return icons['rain']
        elif icon == '11n':
            return icons['thunder']
        elif icon == '13n':
            return icons['snow']
        elif icon == '50n':
            return icons['mist']
        else:
            return None
           

    def main(self):
        self.setup()
        self.root.mainloop()
        

if __name__ == "__main__":
    disp = Display()
    disp.main()

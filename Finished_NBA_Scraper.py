from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk

class NBA_Scraper:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 5)  # Increasing from 12 to 20 seconds
        self.start_time = time.time()
        self.serise_data = []
        self.game_serise = []
        self.game_score = []
        self.team_name = []
        self.window = tk.Tk()
        self.window.title('Game Summary')
        self.window.geometry('500x800')

    def find_elements(self, search_method, value, data_array, description):
        elements = self.driver.find_elements(search_method, value)
        if elements:
            for element in elements:
                data_array.append(element.text)
        else:
            print(f'No {description} found.')

    def output(self):
        for i in range(0, len(self.team_name), 2):
            if len(self.game_score) > i:
                tk.Label(self.window, text=f'Game {i//2 + 1}: {self.team_name[i]} vs {self.team_name[i + 1]} - Score: {self.game_score[i]} to {self.game_score[i + 1]}', font=('Helvetica bold', 16)).pack()
                if self.serise_data:
                    tk.Label(self.window, text=f'This game was the {self.serise_data[min(i//2, len(self.serise_data)-1)]}.', font=('Helvetica bold', 16)).pack()
                if len(self.game_serise) > i//2:
                    tk.Label(self.window, text=f'this game resulted in {self.game_serise[i//2]}', font=('Helvetica bold', 16)).pack()
            else:
                tk.Label(self.window, text=f'Game {i//2 + 1}: {self.team_name[i]} vs {self.team_name[i + 1]} - Score data missing', font=('Helvetica bold', 16)).pack()
            tk.Label(self.window, text="").pack()  # Add spacing

    def run(self):
        self.driver.get('https://www.nba.com/games')
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
        self.find_elements(By.CLASS_NAME, 'GameCardMatchup_gamePlayoffRoundText__Sy2Tn', self.serise_data, 'playoff series data')
        self.find_elements(By.CLASS_NAME, 'GameCardMatchup_gameSeriesText__zqvUF', self.game_serise, 'game series data')
        self.find_elements(By.XPATH, "//p[@class='MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w']", self.game_score, 'game score data')
        self.find_elements(By.CLASS_NAME, 'MatchupCardTeamName_teamName__9YaBA', self.team_name, 'team name data')
        self.output()
        self.driver.quit()
        end_time = time.time()
        print(f'Operation took {end_time - self.start_time} seconds')
        self.window.mainloop()

if __name__ == '__main__':
    scraper = NBA_Scraper()
    scraper.run()

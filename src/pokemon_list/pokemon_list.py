'''
    Created by jrkinch
    Project for scrapping pokemon names.
    #pylint: disable=line-too-long.
    #Data source url is long.
    Data Source: "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
'''
import os
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class PokemonList():
    """
        Class for scrapping pokemon names.
    """
    def __init__(self):
        #pylint: disable=line-too-long.
        #list_url is long.
        self.list_url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
        if __name__ == "__main__":
            self.file_name = ".//data//pokemon_output.xlsx"
        else:
            self.file_name = ".//pokemon_list//data//pokemon_output.xlsx"
        self.pokemon_list = []

    def setup(self, driver="chrome"):
        """
            Setup the Selenium drivers.
        """
        #pylint: disable=attribute-defined-outside-init.
        #driver declared outside for multiple browsers.
        if driver == "chrome":
            options = ChromeOptions()
            options.add_argument("--ignore-certificate-errors") # For Chrome
            options.add_argument("--ignore-ssl-errors=yes")
            options.add_argument("--allow-insecure-localhost")
            #Optional: to suppress console logs, other add_argument not fixing unsecure ssl errors
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.acceptInsecureCerts = True
            self.driver = webdriver.Chrome(options=options)
        elif driver == "firefox":
            options = FirefoxOptions()
            options.set_capability("acceptInsecureCerts", True) # For Firefox:
            self.driver = webdriver.Firefox(options=options)

    def cleanup(self):
        """
            Close the Selenium drivers.
        """
        self.driver.close()

    def check_pokemon_data_file(self):
        '''
            Checks to see if the file exists and how many rows it has.
        '''
        #pylint: disable=no-else-return.
        #needed for file exist check and amount check against website listed number.
        if os.path.exists(self.file_name):
            df = pd.read_excel(self.file_name)
            return True, len(df)
        else:
            return False, 0

    def get_site_list_amount(self):
        '''
            Find and return the pokemon amount data from the website.
        '''
        found = ""
        text_list = self.driver.find_elements(by=By.TAG_NAME, value="p")
        for t in text_list:
            if "Pokémon in total." in t.text:
                match = re.search(r'\d+', t.text)
                if match:
                    found = match.group(0)

        return int(found)

    def get_site_pokemon_list_data(self):
        '''
            This grabs the table with all of the pokemon text info 
            but 'src' image data is not included in cell row. Getting 
            src image text through 'link' variable and attaching to the 
            blank cell because it is the only cell the cell.text returns blank.
        '''
        tables = self.driver.find_elements(by=By.CLASS_NAME, value="roundy")
        for table in tables:
            rows  = table.find_elements(by=By.XPATH, value='.//tr')
            for _ , r in enumerate(rows):
                cells = r.find_elements(by=By.XPATH, value='.//td')
                pokemon_row = []
                for cell in cells:
                    link = r.find_element(by=By.TAG_NAME, value="img")
                    #cell.text doesn't get img src so this attachs
                    #src image text to only cell that doesn't have text
                    if cell.text == "":
                        pokemon_row.append(link.get_attribute("src"))
                    else:
                        pokemon_row.append(cell.text)
                try:
                    if '#' in pokemon_row[0]:
                        self.pokemon_list.append(pokemon_row)
                except (IndexError, IOError) as e:
                    print("Error: ", e)

    def save_to_file(self):
        '''
            Put data to file.
        '''
        df = pd.DataFrame(self.pokemon_list, columns=['Pokedex', 'Image', 'Name', 'Type1', 'Type2'])
        df.to_excel(self.file_name, index=False)

    def get_and_set_data(self):
        '''
            Functions to call when needing a new/updated pokemon list.
        '''
        #Grab Pokemon info.
        self.get_site_pokemon_list_data()

        #Put data to file.
        self.save_to_file()

    def check_file_and_get_latest(self):
        '''
            This check if file exists, is up to date or gets data.
        '''
        #setup the webdriver.
        self.setup()

        #Open the pokemon website.
        self.driver.get(self.list_url)

        #Checks to see if data file exists and either updates or confirms data is up to date.
        file_exists, file_amount = self.check_pokemon_data_file()
        if file_exists:
            #Checking data file and site for same amount number.
            site_amount = self.get_site_list_amount()
            if file_amount == site_amount:
                print("Pokémon list data is up to date.")
            else:
                #get info again
                print("Pokémon list data is different, needs to update...")
                print("Updating Pokémon list data...")
                self.get_and_set_data()
                print("Pokémon list data completed.")
        else:
            print("Retrieving Pokémon list data...")
            self.get_and_set_data()
            print("Pokémon list data completed.")

        #close the webdriver.
        self.cleanup()

if __name__ == "__main__":
    #init class.
    pl = PokemonList()

    #checks for data file and gets latest data.
    pl.check_file_and_get_latest()

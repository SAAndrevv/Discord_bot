import csv
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

def chart():

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(10)
        browser.get("https://spotifycharts.com/regional/")

        download = browser.find_element(By.CSS_SELECTOR, "a.header-csv")
        link = download.get_attribute("href")
        r = requests.get(link)
        with open("chart.csv", "wb") as code:
            code.write(r.content)

        composition = []
        with open("chart.csv") as f:
            track = csv.reader(f)
            for song in track:
                try:
                    int(song[0])
                    s = song[0] + ") " + song[1] + " - "  + song[2]
                    composition.append(s)
                except:
                    continue

        
        del composition[25:]
        return composition

    except:
        print("Error")
        return False

    finally:
        browser.quit()



if __name__ == "__main__":
    print("This module is intended for import")
    

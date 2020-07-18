import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def chart():

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(10)
        browser.get('https://music.apple.com/gb/playlist/the-official-chart-top-40/pl.be74e21c4d4a419f85f0e0df0e0b10f7')
        WebDriverWait(browser, 7).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "html.hydrated"))
    )
        songs = browser.find_elements(By.CSS_SELECTOR, ".song-name.typography-label")
        singers = browser.find_elements(By.CSS_SELECTOR, ".by-line.typography-caption")
    
        sound = []
        for i in range(len(songs)):
            composition = singers[i].text + " - " + songs[i].text
            sound.append(composition)
        
        return sound

    except:
        print("Error")
        return False

    finally:
        browser.quit()



if __name__ == "__main__":
    print("This module is intended for import")



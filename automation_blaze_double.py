from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get('https://blaze.com/pt/games/double')


first = True


while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    flag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "roulette-slider"))).get_attribute("class")

    if flag == 'start' and first == True:
        entries_div = soup.find("div", {"class": "entries main"})
        entrys = entries_div.find_all("div", {"class": "roulette-tile"})
        
        entrys = entrys[0:5]
        box_list = []
        
        for entry in entrys:
            if 'red' in entry.__str__():
                box_list.append(('red',entry.text))
            elif 'black' in entry.__str__():
                box_list.append(('black',entry.text))
            else:
                box_list.append(('white'))
        first = False
        print(*box_list,sep=' ')
    
    elif flag == 'start' and first == False:
        pass
    else:
        first = True
    
    time.sleep(1)     
    





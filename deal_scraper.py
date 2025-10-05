import time
import pandas as pd
import os
from selenium import webdriver #to control the web browser automatically
from selenium.webdriver.common.by import By #to select html elements(CSS selector, XPATH, id...)
from selenium.webdriver.chrome.service import Service #to start chrome and pass optios
from selenium.webdriver.chrome.options import Options


def top_deals_csv():
    '''
    Scrapes product data (title, price, link) from Bol.com deals page,
    handles scrolling, and saves the result to a CSV file.
    '''
    options = Options() #chrome start
    options.add_argument('--headless')                 
    options.add_argument('--disable-dev-shm-usage')           
    options.add_argument('--window-size=1920,1080') 

    
    driver = webdriver.Chrome(service=Service(), options=options) #ChromeDriver

    base_url = 'https://www.bol.com/nl/nl/deals'
    driver.get(base_url)
    time.sleep(3)

    #cookie 
    try:
        accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Alles accepteren')]")
        accept_button.click()
        time.sleep(2)
    except:
        pass


    #lazy + infinite scroll
    previous_count = 0 #product count from previous iteration
    same_count_repeats = 0 

    while True:
        products = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='product']") #product box
        count = len(products)

        if count == previous_count:
            same_count_repeats += 1
        else:
            same_count_repeats = 0
            previous_count = count

        if same_count_repeats >= 5: #break if no new products appear for 5 cycles
            break

        if products:
            driver.execute_script("arguments[0].scrollIntoView(true);", products[-1]) #scroll with JavaScript
            driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(3)

    #print(previous_count)
   

    #data
    titles=list()
    prices=list()
    links = list()


    for product in products:
        title=product.find_element(By.CSS_SELECTOR, 'a>p').text
        #print(title)
        titles.append(title)

        link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        links.append(link)

        price_first= product.find_element(By.CSS_SELECTOR, 'span.row-span-2').text

        try:
            price_middle= product.find_element(By.CSS_SELECTOR, 'span.row-start-1.col-start-2.row-span-2.text-16').text
        except:
            price_middle=''

        try:
            price_sec= product.find_element(By.CSS_SELECTOR, "span[class*='translate-x-[27%]'], span[class*='translate-x-[25%]']").text
        except:
            price_sec=''

        price = price_first + price_middle + price_sec
        #print(price)
        prices.append(price)

        
    df = pd.DataFrame({'Name': titles, 'Price': prices, 'Link': links})
    os.makedirs("data", exist_ok=True)
    df.to_csv('data/topdeals.csv', index=False, encoding='utf-8-sig')

    driver.quit()



from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime

baseUrl = 'https://www.amazon.com/gp/offer-listing/B07PHQ93TV/ref=olp_twister_all?ie=UTF8&mv_color_name=all&mv_configuration=all&mv_digital_storage_capacity=all&mv_style_name=all&qid=1582751867&sr=8-12'
driver = webdriver.Chrome()
count = 0
while True:
    now = datetime.now()
    print("now date and time : " + str(now))
    driver.get(baseUrl)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    bowl = soup.find_all("div", class_='a-column a-span2 olpPriceColumn')
    for i in bowl:
        a = i.find("span", class_='a-size-large a-color-price olpOfferPrice a-text-bold').text
        price = a.replace("$", "")
        price = price.strip()
        price = float(price)
        rprice = round(price)
        if rprice < 50:
            print(rprice)
            driver.close()
        else:
            count = count + 1
            print("Not yet", count)
    time.sleep(10)
driver.close()
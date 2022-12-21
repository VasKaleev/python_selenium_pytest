from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
""" browser.get("https://www.wildberries.by/catalog/38947926/detail.aspx?targetUrl=MI")
time.sleep(5)
button1 = browser.find_element(By.CSS_SELECTOR,".sizes-list__item:nth-child(3) .sizes-list__size")
#.sizes-list__item:nth-child(4) > .j-size
button1.click()
time.sleep(5)
button2 = browser.find_element(By.CSS_SELECTOR,".product-page__order-container > .order .hide-mobile")
#.product-page__order-container > .order .hide-mobile
time.sleep(5)
button2.click()
time.sleep(5) """
browser.get("https://www.mvideo.ru")
time.sleep(10)
button1 = browser.find_element(By.CSS_SELECTOR,".input input").send_keys("телевизоры samsung")
button2 = browser.find_element(By.CSS_SELECTOR,"body > mvid-root > div > mvid-primary-layout > mvid-layout > div > div.layout__header > mvid-header-container > mvid-header > header > div.app-header-middle.app-header-columns.ng-tns-c218-1.ng-star-inserted > div > div.search-container.ng-tns-c218-1 > form > mvid-input > div > div > div > div")
#body > mvid-root > div > mvid-primary-layout > mvid-layout > div > div.layout__header > mvid-header-container > mvid-header > header > div.app-header-middle.app-header-columns.ng-tns-c218-1.ng-star-inserted > div > div.search-container.ng-tns-c218-1 > form > mvid-input > div > div > div > div
button2.click() 
print(button2.text)
time.sleep(5)
browser.close()
browser.quit()

 

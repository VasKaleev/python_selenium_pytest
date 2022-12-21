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
browser.get("https://www.wildberries.by")
time.sleep(2)
button1 = browser.find_element(By.CSS_SELECTOR,".search-catalog__input").send_keys("джинсы мужские")
button2 = browser.find_element(By.CSS_SELECTOR,"button#applySearchBtn")
button2.click() 
#applySearchBtn
time.sleep(5)
browser.close()
browser.quit()

 

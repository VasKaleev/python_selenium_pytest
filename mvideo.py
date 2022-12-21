from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
browser.implicitly_wait(15)
caps = DesiredCapabilities.CHROME
caps["pageLoadStrategy"] = "none"
browser.get("https://www.mvideo.ru")

#Поиск на главной странице сайта
 
#button1 = browser.find_element(By.CSS_SELECTOR,".input input").send_keys("телевизоры samsung")
button1 = browser.find_element(By.XPATH, '//input[@id="1"]').send_keys("телевизоры samsung")
#button2 = browser.find_element(By.CSS_SELECTOR,".search-icon-wrap mvid-icon").click()
button2 = browser.find_element(By.XPATH,'//div[@class="search-icon-wrap ng-star-inserted"]').click()

html = browser.find_element(By.TAG_NAME, "html")
for i in range(5):
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  
elems = browser.find_element(By.CSS_SELECTOR, "div.plp__card-grid").find_elements(By.CSS_SELECTOR, "a.product-title__text")
print("Сюда мы попали")
for elem in elems:
    print(elem.text)
    print("Сюда мы попали1")
print("Сюда мы попали2") 


#Поиск на главной странице сайта селектора локации(Москва)
#location-text top-navbar-link ng-tns-c218-1
""" time.sleep(10)
print("Сюда мы попали3")
button3 = browser.find_element(By.CSS_SELECTOR,".location-text.top-navbar-link")
print(button3.text)
print(button3)
button3.click()
print("Сюда мы попали4")
time.sleep(10) """

#Поиск на главной странице сайта селектора локации(Москва)
#/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/div[1]/mvid-header-container/mvid-header/header/div[1]/div/div[1]/span
#time.sleep(10)
#print("Сюда мы попали5")
#button3 = browser.find_element(By.XPATH, '/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/div[1]/mvid-header-container/mvid-header/header/div[1]/div/div[1]/span')
#button3 = browser.find_element(By.XPATH, '//span[@class="location-text top-navbar-link ng-tns-c218-1"]')
#print(button3.text)
#print(button3)
#button3.click()
#print("Сюда мы попали6")
#time.sleep(10)

browser.close()
browser.quit()

 

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_potions=webdriver.ChromeOptions()
chrome_potions.add_experimental_option("detach",True)

driver: Chrome=webdriver.Chrome(options=chrome_potions)
driver.get("https://www.flipkart.com/ruvido-caso-one-piece-anime-cosplay-monkey-d-luffys-straw-hat/p/itm058f477e765a7?pid=HATHGVRFGRGHQNHG&lid=LSTHATHGVRFGRGHQNHGCWEBTX&marketplace=FLIPKART&q=mugiwara+hat&store=search.flipkart.com&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=0d477907-2f1c-4726-9774-bf1780ce9484.HATHGVRFGRGHQNHG.SEARCH&ppt=sp&ppn=sp&ssid=y8px6wjoqo0000001774280548846&qH=86a49a4abd210946&ov_redirect=true")
driver.maximize_window()
time.sleep(4)

price_element=driver.find_element(By.CSS_SELECTOR,value=".v1zwn21k.v1zwn20._1psv1zeb9._1psv1ze0")
price=price_element.text
only_num=price.split("₹")[1]
print(only_num)
# time.sleep(4)
#
# screrch=driver.find_element(By.CSS_SELECTOR,value=".grid-column-3 div div a")
# screrch.click()

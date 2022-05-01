import time
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service_object = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.platt.com/platt-electric-supply/Electric-Boxes-and-Electric-Enclosures/search.aspx?SectionID=2&navPage=1_15_0')
catnum =driver.find_elements(By.XPATH,"//strong[@itemprop='name']")

p_names=[]
for num in catnum:
    num.click()
    product_name=driver.find_element(By.ID,"ctl00_ctl00_MainContent_uxProduct_lblProdHeadline")
    print(product_name.text)
    p_names.append(product_name.text)
    driver.back()
    time.sleep(2)
print(p_names)

price = driver.find_elements(By.XPATH,"//span[@itemprop='price']")

names=[]
prices=[]

for name in catnum:
    # print(name.text)
    names.append(name.text)

for amount in price:
    # print(amu.text)
    prices.append(amount.text)

listdata=zip(names,prices)

wb=Workbook()
sh1=wb.active

for x in list(listdata):
    sh1.append(x)

wb.save("data1.xlsx")

driver.close()
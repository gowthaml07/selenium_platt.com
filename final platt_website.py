from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service_object = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_object)

driver.get(
    'https://www.platt.com/platt-electric-supply/Electric-Boxes-and-Electric-Enclosures/search.aspx?SectionID=2'
    '&navPage=1_15_0')
get_CatNumber = driver.find_elements(By.XPATH, "//a[@itemprop='url']")
get_price = driver.find_elements(By.XPATH, "//span[@itemprop='price']")

list_Catnum= []
list_prices = []

for num in get_CatNumber:
    # print(num.text)
    list_Catnum.append(num.text)

for amount in get_price:
    # print(amount.text)
    list_prices.append(amount.text)

product_URL = []
for i in range(len(get_CatNumber)):
    product_URL.append(get_CatNumber[i].get_attribute('href'))

product_names = []
for link in product_URL:
    driver.get(link)
    product_name = driver.find_element(By.ID, "ctl00_ctl00_MainContent_uxProduct_lblProdHeadline")
    # print(product_name.text)
    product_names.append(product_name.text)

# print(product_names)
# print(product_URL)
driver.close()

listdata = zip(list_Catnum, product_names, list_prices)

wb = Workbook()
sh1 = wb.active

for x in list(listdata):
    sh1.append(x)

wb.save("data.xlsx")

print('pass')

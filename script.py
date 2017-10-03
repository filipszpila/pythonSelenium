import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.google.com")

f = open("./plik.csv", "r")
reader = csv.reader(f)

for row in reader:
	for col in row:
		elem = driver.find_element_by_xpath("//*[@id='lst-ib']")
		elem.clear()
		elem.send_keys(col)
		elem.send_keys(Keys.RETURN)

f.close()

driver.close()

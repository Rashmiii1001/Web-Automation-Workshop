from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

Path = "C:\\webAutomation\\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get('https://www.irctc.co.in/nget/train-search')
sleep(5)

ok_field = driver.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button')
ok_field.click();
sleep(5)

from_field = driver.find_element_by_xpath('//*[@id="origin"]/span/input')
from_field.send_keys("C SHIVAJI MAH T - CSMT")
from_field.send_keys(Keys.TAB)
sleep(5)

to_field = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
to_field.send_keys("PATNA JN - PNBE")
to_field.send_keys(Keys.TAB)
sleep(5)

date_field = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
date_field.click()
sleep(5)

date_field1 = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/div/table/tbody/tr[3]/td[6]/a')
date_field1.click()
sleep(5)

class_field = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[3]')
class_field.click();
sleep(5)

class1_field = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[4]/div/ul/li[3]/span')
class1_field.click();
sleep(5)

find_field = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button')
find_field.click()
sleep(5)

passenger_field = driver.find_element_by_xpath('//*[@id="numberOfPassengers"]/div/label')
passenger_field.click()
sleep(5)

select_three = driver.find_element_by_xpath('//*[@id="numberOfPassengers"]/div/div[4]/div/ul/li[4]')
select_three.click()
sleep(5)

class_field1 = driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/label')
class_field1.click()
sleep(5)

class1_field1 = driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/div[4]/div/ul/li[7]/span')
class1_field1.click()
sleep(5)

modify_search = driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[6]/button')
modify_search.click()
sleep(5)

check_avail = driver.find_element_by_xpath('//*[@id="check-availability"]')
check_avail.click();
sleep(10)

book_now = driver.find_element_by_xpath('//*[@id="ui-panel-1-content"]/div/div/div/table/tbody/tr/td[1]/div/div[3]/button')
book_now.click()
sleep(5)
#sometimes line 68 throws an exception, increasing the delay works else click on book now manually

agree = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[1]/div/div[3]/p-footer/div/button[2]/span[2]')
agree.click()
sleep(5)

username_field = driver.find_element_by_xpath('//*[@id="userId"]')
# enter your username between ''
username_field.send_keys('')
sleep(5)

password_field = driver.find_element_by_xpath('//*[@id="pwd"]')
# enter your password between ''
password_field.send_keys('')
sleep(5)

captcha = driver.find_element_by_xpath('//*[@id="nlpAnswer"]')
# enter the given captcha
sleep(15)

sign_in = driver.find_element_by_xpath('//*[@id="login_header_disable"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button')
sign_in.click()

driver.quit()

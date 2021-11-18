from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "YOUR DRIVER"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
AMOUNT = input("enter amount of bill in format xx.xx: " )

driver.get("https://secure8.i-doxs.net/CityOfPhiladelphiaWRB/SignIn.aspx")
time.sleep(2)

user = driver.find_element_by_id('main_UID')
user.send_keys(USERNAME)

passw = driver.find_element_by_id("main_PWD")
passw.send_keys(PASSWORD)

signin = driver.find_element_by_xpath('//*[@id="main_btnSubmit"]')
signin.click()
time.sleep(20)

make_payment = driver.find_element_by_xpath('//*[@id="main_lnkMakePayment"]')
make_payment.click()
time.sleep(5)

pay_amount = driver.find_element_by_xpath('//*[@id="main_rptPayments_txtRptPaymentsAmount_0"]')
pay_amount.send_keys(AMOUNT)
next_button = driver.find_element_by_xpath('//*[@id="main_btnNext"]')
next_button.click()

pay_review = driver.find_element_by_xpath('//*[@id="main_lnkContinue"]')
pay_review.click()

final_pay = driver.find_element_by_xpath('//*[@id="main_btnPay"]')
final_pay.click()
driver.quit()
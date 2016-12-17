import argparse
from selenium import webdriver

def duke():
    driver = webdriver.Firefox()
    url = "https://www.duke-energy.com/home"
    driver.get(url)
    driver.find_element_by_id("login-username").send_keys("jdliauw@gmail.com")
    driver.find_element_by_id("login-password").send_keys("")
    driver.find_element_by_xpath("//input[@class='btn-medium btn-reverse']").click()
    driver.implicitly_wait(5)
    balance = driver.find_element_by_id("ctl00__BodyRegion_lblAccountBalance").text
    driver.close()
    balance = balance.replace("$", "")
    return float(balance)

def ocfl():
	driver = webdriver.Firefox()
	url = "https://utilities.ocfl.net/OCUD/?uname=jdliauw@gmail.com"
	driver.get(url)
	driver.find_element_by_xpath("//input[@type='password']").send_keys("")
	driver.find_element_by_xpath("//input[@type='submit']").click()
	balance = driver.find_element_by_id("ctl00_MainContentPlaceHolder_lblCurrentBalance").text
	driver.close()
	balance = balance.replace("$", "")
	return float(balance)

def brighthouse():
	driver = webdriver.Firefox()
	driver.get("https://pay.brighthouse.com/billpay/app/")
	driver.find_element_by_xpath("//input[contains(@id,'Username')]").send_keys("jdliauw@gmail.com")
	driver.implicitly_wait(5)
	driver.find_element_by_xpath("//input[@type='password']").send_keys("")
	driver.find_element_by_xpath("//a[contains(@id,btnSignIn) and contains(@class,sign-in-btn)]").click()

	# driver.implicitly_wait(5)

	# tried clicking and going to url with info that displays once already logged in (verified manually)
	# driver.get("https://easypayr.brighthouse.com/res/WSC/SSOAccountOverview")
	# balance = driver.find_element_by_xpath("//div[contains(text(),'Current Balance')]")
	driver.close()
	# balance = balance.trim().replace("$", "")
	# return float(balance)

# Parse command line arguments
def get_args():
	parser = argparse.ArgumentParser(
		description="Choose utility balance to check"
	)

	parser.add_argument('-b', action="store_true", help="Check balance for Brighthouse")
	parser.add_argument('-d', action="store_true", help="Check balance for Duke Energy")
	parser.add_argument('-o', action="store_true", help="Check balance for OCFL")
	parser.add_argument('-a', action="store_true", help="Check balance for all utilities")

	return parser.parse_args()

if __name__ == "__main__":
	args = get_args()

	if args.a:
		print 'Duke balance:', duke()
		print 'OCFL balance:', ocfl()
		# print 'Brighthouse balance:', brighthouse()
	if args.b:
		print 'Work In Progress :-('
		# print brighthouse()
	if args.d:
		print duke()
	if args.o:
		print ocfl()

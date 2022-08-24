from selenium import webdriver
from selenium.webdriver.chrome.options import Options


PROXY = "1.255.134.136:3128"


profile = r"C:\Users\abdel\AppData\Local\Google\Chrome\User Data"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument(
    "user-data-dir=C:\\Users\\abdel\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(
    executable_path=r'D:/SeleniumDrivers/chromedriver.exe', chrome_options=options)


driver.get("http://whatismyipaddress.com")
